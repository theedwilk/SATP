export interface Coordenadas {
  latitude: number;
  longitude: number;
}

export interface OrgaoMap {
  id: string;
  nome: string;
  endereco: string;
  latitude: number;
  longitude: number;
  site: string;
  transparencia: string;
  tipo: string;
  esfera: string;
  poder: string;
  distancia_manaus?: number;
}

export interface EstatisticasMapa {
  total_orgaos: number;
  por_esfera: Record<string, number>;
  por_poder: Record<string, number>;
  distancia_media_manaus: number;
  orgao_mais_distante: number;
  orgao_mais_proximo: number;
}

export interface FiltrosOrgaos {
  esfera?: string;
  poder?: string;
  orgao?: string;
  raio_km?: number;
}

export interface ResultadoBusca {
  termo_pesquisado: string;
  total_encontrados: number;
  resultados: OrgaoMap[];
}
