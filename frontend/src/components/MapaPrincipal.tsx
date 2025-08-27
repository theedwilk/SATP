import React, { useEffect, useRef, useState } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import orgaosRanking2024 from '../data/orgaos_amazonas_ranking_2024.json';
import amazonasGeoJSONData from '../data/AM_Municipios_2024.json';
import { Feature, Geometry, GeoJsonProperties, FeatureCollection } from 'geojson';

// Fix para ícones do Leaflet
delete (L.Icon.Default.prototype as any)._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-2x.png',
  iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
});

// Interfaces para tipagem
export interface GeoJSONFeature extends Feature<Geometry, GeoJsonProperties> {
  properties: {
    NM_MUNICIP?: string;
    name?: string;
    [key: string]: any;
  };
}
export interface GeoJSONFeatureCollection extends FeatureCollection<Geometry, GeoJsonProperties> {}

interface OrgaoRanking {
  nome: string;
  valor: number;
  municipio: string;
  poder: string;
  essenciais_final: number;
  nivel_final: string;
}

interface MunicipalityInfo {
  name: string;
  orgaos: OrgaoRanking[];
  totalOrgaos: number;
  mediaGeral: number;
  melhorNivel: string;
  posicaoRanking: number;
  centroid?: L.LatLngExpression;
}

// Enum para os tipos de poder
const PODER_LABELS: { [key: string]: string } = {
  'E': 'Executivo',
  'L': 'Legislativo',
  'J': 'Judiciário',
  'M': 'Ministério Público',
  'D': 'Defensoria',
  'T': 'Tribunal de Contas'
};

// Cores baseadas no melhor nível do município
const getNivelColor = (nivel: string): string => {
  switch (nivel) {
    case 'Diamante': return '#0891b2'; // Teal
    case 'Ouro': return '#d97706'; // Amber
    case 'Elevado': return '#059669'; // Green (Seu verde da região)
    case 'Intermediário': return '#2563eb'; // Blue
    case 'Básico': return '#ea580c'; // Orange
    case 'Inicial': return '#dc2626'; // Red
    case 'Inexistente': return '#6b7280'; // Gray
    default: return '#22c55e'; // Verde claro padrão para municípios sem dados específicos
  }
};

const MapaPrincipal: React.FC = () => {
  const mapRef = useRef<HTMLDivElement>(null);
  const mapInstanceRef = useRef<L.Map | null>(null);
  const geoJsonLayerRef = useRef<L.GeoJSON | null>(null);
  const [selectedMunicipalityName, setSelectedMunicipalityName] = useState<string | null>(null);
  const [selectedMunicipalityDetails, setSelectedMunicipalityDetails] = useState<MunicipalityInfo | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [municipalitiesData, setMunicipalitiesData] = useState<{ [key: string]: MunicipalityInfo }>({});

  // Processa os dados dos órgãos para criar informações por município
  useEffect(() => {
    const processData = () => {
      const municipalitiesMap: { [key: string]: MunicipalityInfo } = {};
      const dadosRanking: OrgaoRanking[] = orgaosRanking2024;

      dadosRanking.forEach((orgao) => {
        if (!municipalitiesMap[orgao.municipio]) {
          municipalitiesMap[orgao.municipio] = {
            name: orgao.municipio,
            orgaos: [],
            totalOrgaos: 0,
            mediaGeral: 0,
            melhorNivel: 'Inexistente',
            posicaoRanking: 0
          };
        }
        municipalitiesMap[orgao.municipio].orgaos.push(orgao);
      });

      const niveisOrdem = ['Diamante', 'Ouro', 'Elevado', 'Intermediário', 'Básico', 'Inicial', 'Inexistente'];
      const sortedMunicipalities = Object.values(municipalitiesMap).sort((a, b) => {
        if (b.mediaGeral !== a.mediaGeral) {
          return b.mediaGeral - a.mediaGeral;
        }
        return niveisOrdem.indexOf(a.melhorNivel) - niveisOrdem.indexOf(b.melhorNivel);
      });

      sortedMunicipalities.forEach((data, index) => {
        data.totalOrgaos = data.orgaos.length;
        data.mediaGeral = data.orgaos.reduce((acc, org) => acc + org.valor, 0) / data.orgaos.length;
        
        data.melhorNivel = data.orgaos.reduce((melhor, orgao) => {
          const nivelAtualIndex = niveisOrdem.indexOf(orgao.nivel_final);
          const melhorNivelIndex = niveisOrdem.indexOf(melhor);
          return nivelAtualIndex < melhorNivelIndex ? orgao.nivel_final : melhor;
        }, 'Inexistente');
        
        data.posicaoRanking = index + 1;
      });

      setMunicipalitiesData(municipalitiesMap);
      setIsLoading(false);
    };

    processData();
  }, []);

  // Efeito para atualizar os detalhes do município selecionado para o painel
  useEffect(() => {
    if (selectedMunicipalityName && municipalitiesData[selectedMunicipalityName]) {
      setSelectedMunicipalityDetails(municipalitiesData[selectedMunicipalityName]);
    } else {
      setSelectedMunicipalityDetails(null);
    }
  }, [selectedMunicipalityName, municipalitiesData]);

  // Função para fechar o painel de detalhes e limpar a seleção
  const closeDetails = () => {
    setSelectedMunicipalityName(null);
    if (geoJsonLayerRef.current) {
      // Reseta o estilo de todas as camadas
      geoJsonLayerRef.current.eachLayer((layer: any) => {
        if (layer.feature && geoJsonLayerRef.current) {
          geoJsonLayerRef.current.resetStyle(layer);
        }
      });
    }
  };

  // Função para obter o estilo do polígono
  const getStyle = (feature: GeoJSONFeature | undefined) => {
    if (!feature || !feature.properties) {
      return {
        fillColor: '#22c55e', // Verde claro padrão
        weight: 1,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
      };
    }

    const municipioNome = feature.properties.NM_MUNICIP || feature.properties.name || 'Desconhecido';
    const info = municipalitiesData[municipioNome];
    
    // VERDE CLARO como cor padrão para todos os municípios
    const baseColor = info ? getNivelColor(info.melhorNivel) : '#22c55e';

    // Verifica se este município é o que está atualmente selecionado
    const isSelected = municipioNome === selectedMunicipalityName;

    return {
      fillColor: isSelected ? '#047857' : baseColor, // Verde escuro para selecionado, cor base caso contrário
      weight: isSelected ? 3 : 1,
      opacity: 1,
      color: isSelected ? '#374151' : 'white',
      dashArray: '3',
      fillOpacity: isSelected ? 0.9 : 0.7
    };
  };

  // Função para criar conteúdo do tooltip com dados dos órgãos
  const createTooltipContent = (municipioNome: string, info: MunicipalityInfo | null) => {
    if (!info) {
      return `
        <div style="font-family: sans-serif; padding: 8px; max-width: 300px;">
          <h4 style="margin: 0 0 8px 0; color: #333; font-size: 14px; font-weight: bold;">${municipioNome}</h4>
          <p style="margin: 0; font-size: 12px; color: #666;">Nenhum dado disponível</p>
        </div>
      `;
    }

    const orgaosAtivos = info.orgaos.filter(orgao => orgao.valor > 0);
    const orgaosInativos = info.orgaos.filter(orgao => orgao.valor === 0);

    return `
      <div style="font-family: sans-serif; padding: 8px; max-width: 300px;">
        <h4 style="margin: 0 0 8px 0; color: #333; font-size: 14px; font-weight: bold;">${info.name}</h4>
        
        <div style="margin-bottom: 8px; padding: 6px; background: #f8f9fa; border-radius: 4px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 12px; color: #555;">Média Geral:</span>
            <span style="font-size: 13px; font-weight: bold; color: #2563eb;">${info.mediaGeral.toFixed(1)}%</span>
          </div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 12px; color: #555;">Nível:</span>
            <span style="font-size: 13px; font-weight: bold; color: ${getNivelColor(info.melhorNivel)};">${info.melhorNivel}</span>
          </div>
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <span style="font-size: 12px; color: #555;">Órgãos:</span>
            <span style="font-size: 13px; font-weight: bold; color: #555;">${orgaosAtivos.length} ativos</span>
          </div>
        </div>

        ${orgaosAtivos.length > 0 ? `
          <div style="margin-bottom: 6px;">
            <p style="margin: 0 0 4px 0; font-size: 11px; color: #666; font-weight: bold;">Órgãos Ativos:</p>
            ${orgaosAtivos.slice(0, 3).map(orgao => `
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px; padding: 3px 0; border-bottom: 1px solid #eee;">
                <span style="font-size: 11px; color: #444;">${orgao.nome.split(' de ')[0]}</span>
                <span style="font-size: 11px; font-weight: bold; color: ${getNivelColor(orgao.nivel_final)};">${orgao.valor.toFixed(1)}%</span>
              </div>
            `).join('')}
            ${orgaosAtivos.length > 3 ? `
              <p style="margin: 2px 0 0 0; font-size: 10px; color: #666; font-style: italic;">+${orgaosAtivos.length - 3} outros órgãos</p>
            ` : ''}
          </div>
        ` : ''}

        ${orgaosInativos.length > 0 ? `
          <div style="margin-top: 6px; padding-top: 6px; border-top: 1px dashed #ddd;">
            <p style="margin: 0 0 4px 0; font-size: 11px; color: #999; font-weight: bold;">Órgãos Inativos:</p>
            <p style="margin: 0; font-size: 10px; color: #999;">${orgaosInativos.length} órgãos sem dados</p>
          </div>
        ` : ''}

        <div style="margin-top: 8px; text-align: center;">
          <p style="margin: 0; font-size: 10px; color: #888;">Clique para ver detalhes completos</p>
        </div>
      </div>
    `;
  };

  // Inicialização e atualização do mapa
  useEffect(() => {
    if (!mapRef.current) return;

    if (!mapInstanceRef.current) {
      mapInstanceRef.current = L.map(mapRef.current, {
        center: [-3.4168, -65.8561],
        zoom: 6,
        minZoom: 5,
        maxZoom: 12,
        zoomControl: false
      });

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(mapInstanceRef.current);

      L.control.zoom({ position: 'topright' }).addTo(mapInstanceRef.current);
    }

    if (!municipalitiesData || Object.keys(municipalitiesData).length === 0) return;

    // Remove a camada GeoJSON existente se houver
    if (geoJsonLayerRef.current) {
      mapInstanceRef.current.removeLayer(geoJsonLayerRef.current);
    }

    // Adiciona a camada GeoJSON dos municípios
    const geoJsonLayer = L.geoJSON(amazonasGeoJSONData as GeoJSONFeatureCollection, {
      style: getStyle,
      onEachFeature: (feature: GeoJSONFeature, layer) => {
        if (!feature.properties) return;
        
        const municipioNome = feature.properties.NM_MUNICIP || feature.properties.name || 'Desconhecido';
        const info = municipalitiesData[municipioNome];

        // Tooltip com informações do município
        const tooltipContent = createTooltipContent(municipioNome, info || null);
        layer.bindTooltip(tooltipContent, {
          permanent: false,
          direction: 'auto',
          className: 'custom-tooltip',
          offset: [0, 0],
          opacity: 0.9
        });

        if (info) {
          const popupContent = `
            <div style="font-family: sans-serif; padding: 5px;">
              <h4 style="margin: 0 0 5px 0; color: #333; font-size: 1.1em;">${info.name}</h4>
              <p style="margin: 0; font-size: 0.9em; color: #555;">Média Geral: <strong>${info.mediaGeral.toFixed(1)}%</strong></p>
              <p style="margin: 0; font-size: 0.9em; color: #555;">Nível: <strong style="color: ${getNivelColor(info.melhorNivel)};">${info.melhorNivel}</strong></p>
              <p style="margin: 0; font-size: 0.9em; color: #555;">Órgãos Avaliados: <strong>${info.orgaos.length}</strong></p>
            </div>
          `;
          layer.bindPopup(popupContent);
        } else {
          // Popup para municípios sem dados específicos
          const popupContent = `
            <div style="font-family: sans-serif; padding: 5px;">
              <h4 style="margin: 0 0 5px 0; color: #333; font-size: 1.1em;">${municipioNome}</h4>
              <p style="margin: 0; font-size: 0.9em; color: #555;">Nenhum dado disponível</p>
            </div>
          `;
          layer.bindPopup(popupContent);
        }

        // Armazena o nome do município no layer para acesso posterior
        (layer as any).municipioNome = municipioNome;

        layer.on({
          click: (e) => {
            if (!feature.properties) return;
            const clickedMunicipioNome = feature.properties.NM_MUNICIP || feature.properties.name || 'Desconhecido';

            if (selectedMunicipalityName === clickedMunicipioNome) {
              setSelectedMunicipalityName(null);
            } else {
              setSelectedMunicipalityName(clickedMunicipioNome);
            }

            // Atualiza o estilo de TODOS os layers manualmente
            if (geoJsonLayerRef.current) {
              geoJsonLayerRef.current.eachLayer((layer: any) => {
                if (layer.setStyle) {
                  const featureMunicipio = layer.municipioNome;
                  const isThisSelected = featureMunicipio === clickedMunicipioNome && selectedMunicipalityName !== clickedMunicipioNome;
                  
                  if (isThisSelected) {
                    layer.setStyle({
                      fillColor: '#047857',
                      weight: 3,
                      color: '#374151',
                      fillOpacity: 0.9
                    });
                  } else {
                    // Reseta o estilo para o padrão
                    const originalStyle = getStyle(layer.feature);
                    layer.setStyle(originalStyle);
                  }
                }
              });
            }
          },
          mouseover: (e) => {
            if (!feature.properties) return;
            const layer = e.target;
            const hoveredMunicipioNome = feature.properties.NM_MUNICIP || feature.properties.name || 'Desconhecido';

            // Aplica estilo de hover apenas se não for o município atualmente selecionado
            if (hoveredMunicipioNome !== selectedMunicipalityName) {
              layer.setStyle({
                weight: 3,
                color: '#666',
                dashArray: '',
                fillOpacity: 0.9
              });
            }
            layer.bringToFront();
          },
          mouseout: (e) => {
            const layer = e.target;
            const hoveredMunicipioNome = (layer as any).municipioNome;
            
            // Reseta o estilo apenas se não for o município selecionado
            if (hoveredMunicipioNome !== selectedMunicipalityName) {
              const originalStyle = getStyle((layer as any).feature);
              layer.setStyle(originalStyle);
            }
          }
        });
      },
    }).addTo(mapInstanceRef.current);

    geoJsonLayerRef.current = geoJsonLayer;

    if (geoJsonLayer.getBounds().isValid()) {
      mapInstanceRef.current.fitBounds(geoJsonLayer.getBounds());
    }

    setIsLoading(false);
  }, [mapInstanceRef.current, municipalitiesData, selectedMunicipalityName]);

  return (
    <div className="relative h-screen w-full flex">
      {isLoading && (
        <div className="absolute inset-0 flex items-center justify-center bg-gray-100 bg-opacity-75 z-50">
          <p className="text-lg text-gray-700">Carregando dados do mapa...</p>
        </div>
      )}
      <div ref={mapRef} className="flex-1 h-full z-10"></div>

      {/* Painel de Detalhes do Município */}
      {selectedMunicipalityDetails && (
        <div className="absolute right-0 top-0 h-full w-96 bg-white shadow-lg z-20 flex flex-col">
          <div className="p-4 border-b border-gray-200 bg-gray-50">
            <div className="flex justify-between items-start">
              <div className="flex-1">
                <h2 className="text-xl font-bold text-gray-900 mb-1">
                  {selectedMunicipalityDetails.name}
                </h2>
                <div className="space-y-1">
                  <div className="text-sm text-gray-600">
                    Órgãos Avaliados: <span className="font-medium">{selectedMunicipalityDetails.orgaos.length}</span>
                  </div>
                  <div className="text-sm text-gray-600">
                    Média Geral: <span className="font-medium">{selectedMunicipalityDetails.mediaGeral.toFixed(1)}%</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <span
                      className="w-3 h-3 rounded-full"
                      style={{ backgroundColor: getNivelColor(selectedMunicipalityDetails.melhorNivel) }}
                    ></span>
                    <span className="text-sm font-medium">{selectedMunicipalityDetails.melhorNivel}</span>
                  </div>
                </div>
              </div>
              <button
                onClick={closeDetails}
                className="text-gray-500 hover:text-gray-700 p-1"
              >
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
          </div>

          <div className="flex-1 overflow-y-auto p-4">
            <h3 className="text-lg font-semibold mb-4 text-gray-800">
              Órgãos Avaliados ({selectedMunicipalityDetails.orgaos.length})
            </h3>
            <div className="space-y-3">
              {selectedMunicipalityDetails.orgaos
                .sort((a, b) => b.valor - a.valor)
                .map((orgao, index) => (
                  <div
                    key={`${orgao.nome}-${index}`}
                    className="bg-gray-50 rounded-lg p-4 border border-gray-200 hover:shadow-md transition-shadow"
                  >
                    <div className="flex justify-between items-start mb-2">
                      <h4 className="font-semibold text-gray-900 text-sm leading-tight">
                        {orgao.nome}
                      </h4>
                      <span className="text-lg font-bold text-blue-600">
                        {orgao.valor.toFixed(1)}%
                      </span>
                    </div>
                    <div className="flex justify-between items-center text-xs text-gray-600">
                      <span className="bg-blue-100 text-blue-800 px-2 py-1 rounded-full">
                        {PODER_LABELS[orgao.poder] || orgao.poder}
                      </span>
                      <div className="flex items-center gap-1">
                        <span
                          className="w-2 h-2 rounded-full"
                          style={{ backgroundColor: getNivelColor(orgao.nivel_final) }}
                        ></span>
                        <span className="font-medium">{orgao.nivel_final}</span>
                      </div>
                    </div>
                    <div className="mt-2 text-xs text-gray-500">
                      Essenciais: {orgao.essenciais_final.toFixed(1)}%
                    </div>
                  </div>
                ))}
            </div>
          </div>

          <div className="p-4 border-t border-gray-200 bg-gray-50">
            <div className="grid grid-cols-2 gap-4 text-center text-sm">
              <div>
                <div className="font-semibold text-gray-800">Melhor Órgão</div>
                <div className="text-blue-600 font-bold">
                  {Math.max(...selectedMunicipalityDetails.orgaos.map(o => o.valor)).toFixed(1)}%
                </div>
              </div>
              <div>
                <div className="font-semibold text-gray-800">Média Essenciais</div>
                <div className="text-green-600 font-bold">
                  {(selectedMunicipalityDetails.orgaos.reduce((acc, org) => acc + org.essenciais_final, 0) / selectedMunicipalityDetails.orgaos.length).toFixed(1)}%
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default MapaPrincipal;