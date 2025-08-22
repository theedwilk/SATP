// Conteúdo do arquivo: src/components/MapaOrgaos.tsx

import React, { useEffect, useMemo } from 'react';
import { MapContainer, TileLayer, Marker, Popup, useMap } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
// Importa o CSS e o JS para garantir que o ícone padrão do Leaflet funcione corretamente com Webpack
import 'leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.webpack.css';
import 'leaflet-defaulticon-compatibility';

import { OrgaoMap, FiltrosOrgaos } from '../types/orgaos';

// Define as propriedades (props) que o componente MapaOrgaos espera receber
interface MapaOrgaosProps {
  orgaos: OrgaoMap[]; // Uma lista de objetos OrgaoMap para exibir no mapa
  selectedFilters: FiltrosOrgaos; // Os filtros atualmente selecionados
  className?: string; // Classe CSS opcional para estilização
}

// Componente auxiliar para ajustar o mapa automaticamente
// Ele usa o hook `useMap` que só pode ser chamado dentro de um componente filho de `MapContainer`
const MapUpdater: React.FC<{ orgaos: OrgaoMap[] }> = ({ orgaos }) => {
  const map = useMap();

  useEffect(() => {
    if (orgaos.length > 0) {
      // Cria uma lista de coordenadas para todos os órgãos
      const latLngs = orgaos.map(org => [org.latitude, org.longitude] as L.LatLngTuple);
      // Calcula os limites que englobam todos os marcadores
      const bounds = L.latLngBounds(latLngs);
      // Ajusta o mapa para exibir todos os marcadores dentro dos limites, com um padding
      map.fitBounds(bounds, { padding: [50, 50] });
    } else {
      // Se não houver órgãos, centraliza em Manaus (ou outra localização padrão)
      map.setView([-3.10719, -60.02173], 10); // Coordenadas de Manaus
    }
  }, [orgaos, map]); // Re-executa quando a lista de órgãos ou a instância do mapa mudam

  return null; // Este componente não renderiza nada diretamente
};

const MapaOrgaos: React.FC<MapaOrgaosProps> = ({ orgaos, selectedFilters, className }) => {
  // Coordenadas padrão para Manaus e zoom inicial
  const defaultCenter: L.LatLngTuple = [-3.10719, -60.02173];
  const defaultZoom = 10;

  // Filtra os órgãos com base nos `selectedFilters` usando `useMemo` para otimização
  const filteredOrgaos = useMemo(() => {
    return orgaos.filter(orgao => {
      let matches = true;
      if (selectedFilters.esfera && orgao.esfera !== selectedFilters.esfera) {
        matches = false;
      }
      if (selectedFilters.poder && orgao.poder !== selectedFilters.poder) {
        matches = false;
      }
      if (selectedFilters.orgao && orgao.nome !== selectedFilters.orgao) {
        matches = false;
      }
      // O filtro 'tipo' foi adicionado em orgaos.ts, mas o SAPT.tsx não o usa diretamente para filtrar
      // Se você tiver um filtro de 'tipo' direto na UI, pode adicioná-lo aqui.
      // Ex: if (selectedFilters.tipo && orgao.tipo !== selectedFilters.tipo) { matches = false; }
      return matches;
    });
  }, [orgaos, selectedFilters]); // Re-calcula apenas se 'orgaos' ou 'selectedFilters' mudarem

  return (
    <div className={className}>
      <MapContainer
        center={defaultCenter}
        zoom={defaultZoom}
        scrollWheelZoom={true} // Permite zoom com a roda do mouse
        className="h-full w-full rounded-lg" // Garante que o mapa preencha o contêiner
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        {/* Adiciona o componente que ajusta o mapa */}
        <MapUpdater orgaos={filteredOrgaos} />

        {/* Renderiza um marcador para cada órgão filtrado */}
        {filteredOrgaos.map(orgao => (
          <Marker key={orgao.id} position={[orgao.latitude, orgao.longitude]}>
            <Popup>
              <h4 className="font-bold">{orgao.nome}</h4>
              <p><strong>Endereço:</strong> {orgao.endereco}</p>
              <p><strong>Esfera:</strong> {orgao.esfera}</p>
              <p><strong>Poder:</strong> {orgao.poder}</p>
              {orgao.site && <p><a href={orgao.site} target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline">Site</a></p>}
              {orgao.transparencia && <p><a href={orgao.transparencia} target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline">Transparência</a></p>}
            </Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
};

export default MapaOrgaos;
