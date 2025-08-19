import React, { useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { OrgaoMap, FiltrosOrgaos } from '../types/orgaos';
import { useOrgaos } from '../hooks/useOrgaos';

// Fix dos ícones do Leaflet para React
delete (L.Icon.Default.prototype as any)._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

interface MapaOrgaosProps {
  onOrgaoSelect?: (orgao: OrgaoMap) => void;
  selectedFilters?: FiltrosOrgaos;
  className?: string;
}

const MapaOrgaos: React.FC<MapaOrgaosProps> = ({ 
  onOrgaoSelect, 
  selectedFilters = {},
  className = ''
}) => {
  const { orgaos, loading, error } = useOrgaos(selectedFilters);
  const [mapCenter] = useState<[number, number]>([-3.1190, -60.0217]); // Manaus

  const createCustomIcon = (tipo: string): L.DivIcon => {
    const colors: Record<string, string> = {
      'Estadual - Poder Executivo': '#ef4444',
      'Estadual - Poder Legislativo': '#3b82f6',
      'Estadual - Poder Judiciário': '#a855f7',
      'Estadual - Tribunal de Contas': '#f59e0b',
      'Estadual - Ministério Público': '#10b981',
      'Municipal - Poder Executivo': '#f97316',
      'Municipal - Poder Legislativo': '#6b7280',
    };

    const color = colors[tipo] || '#9ca3af';
    const letter = tipo.includes('Executivo') ? 'E' : 
                   tipo.includes('Legislativo') ? 'L' : 
                   tipo.includes('Judiciário') ? 'J' : 
                   tipo.includes('Tribunal') ? 'T' : 
                   tipo.includes('Ministério') ? 'M' : 'O';
    
    return L.divIcon({
      className: 'custom-marker',
      html: `
        <div class="w-6 h-6 rounded-full border-2 border-white shadow-lg flex items-center justify-center text-white text-xs font-bold" 
             style="background-color: ${color}">
          ${letter}
        </div>
      `,
      iconSize: [24, 24],
      iconAnchor: [12, 12],
    });
  };

  if (loading) {
    return (
      <div className={`relative ${className}`}>
        <div className="absolute inset-0 flex items-center justify-center bg-gray-100 z-50">
          <div className="bg-white p-6 rounded-lg shadow-lg">
            <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mx-auto mb-4"></div>
            <p className="text-gray-600">Carregando mapa dos órgãos...</p>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className={`relative ${className}`}>
        <div className="absolute inset-0 flex items-center justify-center bg-gray-100 z-50">
          <div className="bg-white p-6 rounded-lg shadow-lg text-center">
            <div className="text-red-500 text-4xl mb-4">⚠️</div>
            <p className="text-red-600 font-semibold">Erro ao carregar mapa</p>
            <p className="text-gray-600 text-sm mt-2">{error}</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className={`relative ${className}`}>
      <MapContainer
        center={mapCenter}
        zoom={7}
        scrollWheelZoom={true}
        className="h-full w-full z-0"
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        
        {orgaos.map((orgao) => (
          <Marker
            key={orgao.id}
            position={[orgao.latitude, orgao.longitude]}
            icon={createCustomIcon(orgao.tipo)}
            eventHandlers={{
              click: () => onOrgaoSelect?.(orgao),
            }}
          >
            <Popup className="custom-popup">
              <div className="min-w-[250px] p-2">
                <h4 className="text-lg font-semibold text-gray-800 mb-2 border-b pb-1">
                  {orgao.nome}
                </h4>
                
                <div className="space-y-2 text-sm">
                  <div>
                    <span className="font-medium text-gray-600">Tipo:</span>
                    <span className="ml-1 text-gray-800">{orgao.tipo}</span>
                  </div>
                  
                  <div>
                    <span className="font-medium text-gray-600">Endereço:</span>
                    <span className="ml-1 text-gray-800">{orgao.endereco}</span>
                  </div>
                  
                  {orgao.distancia_manaus && (
                    <div>
                      <span className="font-medium text-gray-600">Distância de Manaus:</span>
                      <span className="ml-1 text-gray-800">{orgao.distancia_manaus} km</span>
                    </div>
                  )}
                </div>

                <div className="flex space-x-2 mt-4">
                  {orgao.site && (
                    <a 
                      href={orgao.site} 
                      target="_blank" 
                      rel="noopener noreferrer"
                      className="inline-flex items-center px-3 py-1 bg-blue-500 text-white text-xs rounded hover:bg-blue-600 transition-colors"
                    >
                      🌐 Site
                    </a>
                  )}
                  {orgao.transparencia && (
                    <a 
                      href={orgao.transparencia} 
                      target="_blank" 
                      rel="noopener noreferrer"
                      className="inline-flex items-center px-3 py-1 bg-green-500 text-white text-xs rounded hover:bg-green-600 transition-colors"
                    >
                      📊 Transparência
                    </a>
                  )}
                </div>
              </div>
            </Popup>
          </Marker>
        ))}
      </MapContainer>
      
      {/* Contador de órgãos e legenda */}
      <div className="absolute top-4 right-4 z-10 bg-white rounded-lg shadow-lg p-3">
        <div className="text-sm font-medium text-gray-700 mb-2">
          Total: {orgaos.length} órgãos
        </div>
        <div className="space-y-1 text-xs text-gray-600">
          <div className="flex items-center">
            <div className="w-3 h-3 bg-red-500 rounded-full mr-2"></div>
            Executivo
          </div>
          <div className="flex items-center">
            <div className="w-3 h-3 bg-blue-500 rounded-full mr-2"></div>
            Legislativo
          </div>
          <div className="flex items-center">
            <div className="w-3 h-3 bg-purple-500 rounded-full mr-2"></div>
            Judiciário
          </div>
        </div>
      </div>
    </div>
  );
};

export default MapaOrgaos;
