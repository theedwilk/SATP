import axios from 'axios';
import { OrgaoMap, EstatisticasMapa, FiltrosOrgaos, ResultadoBusca } from '../types/orgaos';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
});

// Interceptor para tratamento de erros
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('Erro na API:', error);
    throw new Error(error.response?.data?.detail || 'Erro de conexão com a API');
  }
);

export class OrgaosApiService {
  static async fetchOrgaos(filters: FiltrosOrgaos = {}): Promise<OrgaoMap[]> {
    const params = new URLSearchParams();
    
    if (filters.esfera) params.append('esfera', filters.esfera);
    if (filters.poder) params.append('poder', filters.poder);
    if (filters.raio_km) params.append('raio_km', filters.raio_km.toString());
    
    const response = await api.get<OrgaoMap[]>(`/api/orgaos-mapa?${params}`);
    return response.data;
  }

  static async fetchEstatisticas(): Promise<EstatisticasMapa> {
    const response = await api.get<EstatisticasMapa>('/api/estatisticas-mapa');
    return response.data;
  }

  static async fetchOrgaoDetalhes(orgaoId: string): Promise<OrgaoMap> {
    const response = await api.get<OrgaoMap>(`/api/orgao/${orgaoId}`);
    return response.data;
  }

  static async buscarOrgaos(termo: string, filters: FiltrosOrgaos = {}): Promise<ResultadoBusca> {
    const params = new URLSearchParams({ termo });
    
    if (filters.esfera) params.append('esfera', filters.esfera);
    if (filters.poder) params.append('poder', filters.poder);
    
    const response = await api.get<ResultadoBusca>(`/api/buscar-orgaos?${params}`);
    return response.data;
  }
}
