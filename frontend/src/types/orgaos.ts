// Conteúdo do arquivo: src/types/orgaos.ts

export interface OrgaoMap {
  id: string;
  nome: string; // Nome do órgão
  endereco: string;
  latitude: number;
  longitude: number;
  site?: string;
  transparencia?: string;
  tipo?: string; // Ex: "Estadual - Executivo"
  esfera: string;
  poder: string;
  municipio: string; // Adicionado para identificar o município
  distancia_manaus?: number;
}

export interface FiltrosOrgaos {
  esfera?: string;
  poder?: string;
  orgao?: string;
  tipo?: string;
  municipio?: string;
  raio_km?: number; // Adicionado novamente para o filtro de raio
}

// Interface para as estatísticas gerais do mapa ou busca
export interface EstatisticasMapa {
  totalOrgaos: number;
  totalMunicipios: number;
  // Adicione outras estatísticas relevantes aqui, se houver
}

// Interface para o resultado completo de uma busca de órgãos
export interface ResultadoBusca {
  orgaos: OrgaoMap[];
  estatisticas: EstatisticasMapa;
}
