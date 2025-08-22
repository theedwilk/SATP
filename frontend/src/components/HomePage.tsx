// Conteúdo do arquivo: src/components/HomePage.tsx

import React, { useState, useEffect, useMemo } from 'react';
import { MapContainer, TileLayer, Marker, Popup, useMap } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import 'leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.webpack.css';
import 'leaflet-defaulticon-compatibility';

import ApiService from '../services/api';
import { OrgaoMap } from '../types/orgaos';

// Componente auxiliar para ajustar o mapa automaticamente
const MapUpdater: React.FC<{ orgaos: OrgaoMap[]; selectedMunicipality?: string | null }> = ({ orgaos, selectedMunicipality }) => {
  const map = useMap();

  useEffect(() => {
    if (orgaos.length > 0) {
      let latLngs: L.LatLngTuple[] = [];
      if (selectedMunicipality) {
        // Se um município está selecionado, foca apenas nos órgãos dele
        latLngs = orgaos
          .filter(org => org.municipio === selectedMunicipality)
          .map(org => [org.latitude, org.longitude] as L.LatLngTuple);
      } else {
        // Caso contrário, considera todos os órgãos
        latLngs = orgaos.map(org => [org.latitude, org.longitude] as L.LatLngTuple);
      }

      if (latLngs.length > 0) {
        // Ajusta o mapa para mostrar todos os marcadores relevantes
        const bounds = L.latLngBounds(latLngs);
        map.fitBounds(bounds, { padding: [50, 50] });
      } else {
        // Se não houver órgãos relevantes, centraliza no Amazonas
        map.setView([-3.4168, -65.8561], 7); // Centro do Amazonas
      }
    } else {
      // Se nenhum órgão foi carregado, centraliza no Amazonas
      map.setView([-3.4168, -65.8561], 7); // Centro do Amazonas
    }
  }, [orgaos, map, selectedMunicipality]); // Dependências para re-executar o efeito

  return null; // Este componente não renderiza nada diretamente
};

const HomePage: React.FC = () => {
  const [allOrgaosForMap, setAllOrgaosForMap] = useState<OrgaoMap[]>([]);
  const [orgaosLoading, setOrgaosLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedMunicipality, setSelectedMunicipality] = useState<string | null>(null);

  // Carregar todos os dados dos órgãos para o mapa na inicialização
  useEffect(() => {
    const carregarOrgaos = async () => {
      try {
        setOrgaosLoading(true);
        const data = await ApiService.obterOrgaos(); // Obtém os dados dos órgãos para os dropdowns
        
        // --- SIMULAÇÃO: Gerar dados OrgaoMap para o mapa com municípios e coordenadas ---
        // ATENÇÃO: Esta é uma SIMULAÇÃO. Você precisará que seu ApiService ou um endpoint
        // específico retorne dados de latitude, longitude, endereço e, crucialmente,
        // o município para cada órgão para que o mapa seja preciso.
        // A lista de municípios abaixo é apenas para fins de demonstração.
        const amazonMunicipalities = [
          "Manaus", "Parintins", "Itacoatiara", "Manacapuru", "Coari", "Tabatinga",
          "Tefé", "Manicoré", "Humaitá", "Lábrea", "Borba", "Maués", "São Gabriel da Cachoeira",
          "Benjamin Constant", "Eirunepé", "Envira", "Barreirinha", "Autazes", "Careiro",
          "Rio Preto da Eva", "Presidente Figueiredo", "Novo Airão", "Silves", "Urucurituba",
          "Nhamundá", "Santa Isabel do Rio Negro", "Barcelos", "Novo Aripuanã", "Boca do Acre",
          "Canutama", "Juruá", "Tapauá", "Caapiranga", "Codajás", "Anori", "Maraã", "Uarini",
          "Alvarães", "Japurá", "Tonantins", "Santo Antônio do Içá", "Amaturá", "Atalaia do Norte",
          "Carauari", "Guajará", "Ipixuna", "Itamarati", "Jutaí", "Nova Olinda do Norte",
          "Pauini", "São Paulo de Olivença", "Urucará", "Fonte Boa", "Beruri", "Boa Vista do Ramos",
          "Apuí", "Iranduba", "Maraã", "Novo Airão", "São Sebastião do Uatumã"
        ];

        const generatedMapData: OrgaoMap[] = [];
        let idCounter = 1;
        for (const esferaKey in data) {
          for (const poderKey in data[esferaKey]) {
            for (const orgaoKey in data[esferaKey][poderKey]) {
              const orgaoDetails = data[esferaKey][poderKey][orgaoKey];
              // Atribui um município aleatório para a simulação
              const randomMunicipality = amazonMunicipalities[Math.floor(Math.random() * amazonMunicipalities.length)];

              generatedMapData.push({
                id: `org-${idCounter++}`,
                nome: orgaoKey,
                endereco: `Endereço Fictício de ${orgaoKey}, ${randomMunicipality}`,
                // Coordenadas aleatórias dentro de uma área ampla do Amazonas para simulação
                latitude: -3.4168 + (Math.random() - 0.5) * 5, 
                longitude: -65.8561 + (Math.random() - 0.5) * 5, 
                site: orgaoDetails.site,
                transparencia: orgaoDetails.transparencia,
                tipo: `${esferaKey} - ${poderKey}`,
                esfera: esferaKey,
                poder: poderKey,
                municipio: randomMunicipality, // O município atribuído
                distancia_manaus: Math.floor(Math.random() * 500) + 50, // Distância fictícia
              });
            }
          }
        }
        setAllOrgaosForMap(generatedMapData);
        setError(null);
        // --- FIM DA SIMULAÇÃO ---

      } catch (err: any) {
        setError(err.message);
        console.error('Erro ao carregar órgãos para o mapa:', err);
      } finally {
        setOrgaosLoading(false);
      }
    };
    carregarOrgaos();
  }, []); // Executa apenas uma vez ao montar o componente

  // Agrupa os órgãos por município para exibir no popup
  const organsByMunicipality = useMemo(() => {
    return allOrgaosForMap.reduce((acc, orgao) => {
      if (!acc[orgao.municipio]) {
        acc[orgao.municipio] = [];
      }
      acc[orgao.municipio].push(orgao);
      return acc;
    }, {} as { [municipio: string]: OrgaoMap[] });
  }, [allOrgaosForMap]);

  // Função para obter uma coordenada representativa para um município
  // (para o marcador do município)
  const getMunicipalityCoords = (municipio: string) => {
    const organsInMunicipality = organsByMunicipality[municipio];
    if (organsInMunicipality && organsInMunicipality.length > 0) {
      // Retorna as coordenadas do primeiro órgão encontrado naquele município
      return [organsInMunicipality[0].latitude, organsInMunicipality[0].longitude] as L.LatLngTuple;
    }
    // Fallback para uma coordenada central do Amazonas se não houver órgãos
    return [-3.4168 + (Math.random() - 0.5) * 5, -65.8561 + (Math.random() - 0.5) * 5] as L.LatLngTuple;
  };

  // Lida com o clique no marcador de um município
  const handleMunicipalityClick = (municipio: string) => {
    setSelectedMunicipality(municipio);
  };

  // Limpa a seleção do município, mostrando todos os marcadores novamente
  const handleClearSelection = () => {
    setSelectedMunicipality(null);
  };

  return (
    <div className="flex flex-col h-full w-full">
      <div className="flex-1 relative">
        {/* Indicador de carregamento */}
        {orgaosLoading && (
          <div className="absolute inset-0 bg-gray-200 bg-opacity-75 flex items-center justify-center z-10">
            <p className="text-lg text-gray-800">Carregando mapa e dados dos órgãos...</p>
          </div>
        )}
        {/* Mensagem de erro */}
        {error && (
          <div className="absolute inset-0 bg-red-100 bg-opacity-75 flex items-center justify-center z-10">
            <p className="text-lg text-red-800">Erro ao carregar dados: {error}</p>
          </div>
        )}

        <MapContainer
          center={[-3.4168, -65.8561]} // Centro do Amazonas
          zoom={7} // Nível de zoom inicial para o estado
          scrollWheelZoom={true} // Permite zoom com a roda do mouse
          className="h-full w-full" // Garante que o mapa preencha o contêiner
        >
          <TileLayer
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          {/* Componente para ajustar o mapa com base nos órgãos */}
          <MapUpdater orgaos={allOrgaosForMap} selectedMunicipality={selectedMunicipality} />

          {/* Renderiza marcadores */}
          {Object.keys(organsByMunicipality).map(municipio => {
            const organsInMun = organsByMunicipality[municipio];
            const coords = getMunicipalityCoords(municipio);

            // Se nenhum município estiver selecionado, mostra um marcador por município
            if (!selectedMunicipality) {
              return (
                <Marker key={`mun-${municipio}`} position={coords}>
                  <Popup>
                    <h4 className="font-bold text-lg">{municipio}</h4>
                    <p className="text-sm mb-2">Total de Órgãos: {organsInMun.length}</p>
                    <button
                      onClick={() => handleMunicipalityClick(municipio)}
                      className="px-3 py-1 bg-blue-600 text-white rounded-md text-sm hover:bg-blue-700 transition-colors"
                    >
                      Ver Órgãos
                    </button>
                  </Popup>
                </Marker>
              );
            } 
            // Se um município estiver selecionado, mostra os marcadores individuais dos órgãos daquele município
            else if (selectedMunicipality === municipio) {
              return organsInMun.map(orgao => (
                <Marker key={orgao.id} position={[orgao.latitude, orgao.longitude]}>
                  <Popup>
                    <h4 className="font-bold">{orgao.nome}</h4>
                    <p><strong>Município:</strong> {orgao.municipio}</p>
                    <p><strong>Endereço:</strong> {orgao.endereco}</p>
                    <p><strong>Esfera:</strong> {orgao.esfera}</p>
                    <p><strong>Poder:</strong> {orgao.poder}</p>
                    {orgao.site && <p><a href={orgao.site} target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline">Site</a></p>}
                    {orgao.transparencia && <p><a href={orgao.transparencia} target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline">Transparência</a></p>}
                  </Popup>
                </Marker>
              ));
            }
            return null; // Não renderiza nada para outros municípios quando um está selecionado
          })}
        </MapContainer>

        {/* Botão para limpar a seleção do município */}
        {selectedMunicipality && (
          <div className="absolute top-4 left-4 z-10 bg-white p-3 rounded-lg shadow-md flex items-center space-x-2">
            <span className="font-semibold text-blue-800">Município Selecionado: {selectedMunicipality}</span>
            <button
              onClick={handleClearSelection}
              className="px-3 py-1 bg-red-500 text-white rounded-md text-sm hover:bg-red-600 transition-colors"
            >
              Limpar Seleção
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default HomePage;
