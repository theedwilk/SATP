// MapaPrincipal.tsx
import React from 'react';

interface MunicipalityInfo {
  id: string;
  name: string;
  // Você pode adicionar outras informações relevantes do município aqui, como coordenadas, população, etc.
}

// Dados de municípios de exemplo (em uma aplicação real, viriam de uma API ou arquivo JSON)
const mockMunicipalities: MunicipalityInfo[] = [
  { id: '1', name: 'Manaus' },
  { id: '2', name: 'Parintins' },
  { id: '3', name: 'Itacoatiara' },
  { id: '4', name: 'Manacapuru' },
  { id: '5', name: 'Coari' },
  // ... adicione os outros 57 municípios do Amazonas aqui
];

const MapaPrincipal: React.FC = () => {
  const handleMunicipalityClick = (municipality: MunicipalityInfo) => {
    alert(`Você clicou no município de ${municipality.name}. Aqui você veria as informações dos órgãos deste município.`);
    // Em uma aplicação real, isso poderia navegar para uma página de detalhes do município,
    // abrir um modal com informações, ou filtrar dados em outra seção.
  };

  return (
    <div className="p-8 bg-gray-100 flex-1">
      <h1 className="text-3xl font-bold text-blue-800 mb-6">Mapa do Estado do Amazonas</h1>
      <p className="text-gray-700 mb-8">
        Explore os municípios do Amazonas para visualizar informações dos órgãos de transparência.
      </p>

      <div className="bg-white rounded-lg shadow-md p-6 h-[600px] flex items-center justify-center text-gray-500 text-lg relative">
        <p className="text-center">
          <span className="font-semibold">Mapa interativo do Amazonas aqui.</span><br />
          (Integração com biblioteca de mapas como Leaflet ou Mapbox)<br />
          Cada um dos 62 municípios seria clicável.
        </p>
        {/* Exemplo de municípios clicáveis (simplificado para ilustração) */}
        <div className="absolute bottom-8 right-8 bg-blue-50 p-4 rounded-lg shadow-inner">
          <h4 className="font-semibold mb-2 text-blue-800">Municípios (Exemplo):</h4>
          <div className="flex flex-wrap gap-2">
            {mockMunicipalities.slice(0, 5).map(muni => (
              <button
                key={muni.id}
                onClick={() => handleMunicipalityClick(muni)}
                className="px-3 py-1 bg-blue-200 text-blue-800 rounded-full text-sm hover:bg-blue-300 transition-colors"
              >
                {muni.name}
              </button>
            ))}
            <span className="text-sm text-gray-600">... e mais 57</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MapaPrincipal;
