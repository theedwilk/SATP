// Conteúdo do arquivo: src/services/orgaosApi.ts

import axios from 'axios';
import { OrgaoMap, EstatisticasMapa, FiltrosOrgaos, ResultadoBusca } from '../types/orgaos'; // Importações corrigidas

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
});

export class OrgaosApiService {
  static async buscarOrgaosMapa(filters: FiltrosOrgaos): Promise<ResultadoBusca> {
    const params = new URLSearchParams();
    if (filters.esfera) params.append('esfera', filters.esfera);
    if (filters.poder) params.append('poder', filters.poder);
    if (filters.municipio) params.append('municipio', filters.municipio);
    if (filters.raio_km) params.append('raio_km', filters.raio_km.toString()); // raio_km adicionado

    const response = await api.get<OrgaoMap[]>(`/api/orgaos-mapa?${params}`);
    
    // Simulação de estatísticas, você precisará que sua API retorne isso
    const estatisticas: EstatisticasMapa = {
      totalOrgaos: response.data.length,
      totalMunicipios: new Set(response.data.map(o => o.municipio)).size,
    };

    return {
      orgaos: response.data,
      estatisticas: estatisticas,
    };
  }

  // Outros métodos da API que você possa ter
}
