import axios from 'axios';

// Configuração da API baseada no ambiente
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 60000, // 60 segundos para auditorias que podem demorar
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptors para debug em desenvolvimento
if (process.env.NODE_ENV === 'development') {
  api.interceptors.request.use((config) => {
    console.log(`🚀 API Request: ${config.method?.toUpperCase()} ${config.url}`);
    return config;
  });

  api.interceptors.response.use(
    (response) => {
      console.log(`✅ API Response: ${response.status} ${response.config.url}`);
      return response;
    },
    (error) => {
      console.error(`❌ API Error: ${error.response?.status} ${error.config?.url}`, error.response?.data);
      return Promise.reject(error);
    }
  );
}

// Interfaces existentes mantidas
export interface OrgaosData {
  [esfera: string]: {
    [poder: string]: {
      [orgao: string]: {
        site: string;
        transparencia: string;
      };
    };
  };
}

export interface DimensoesResponse {
  dimensoes: string[];
  total_dimensoes: number;
}

export interface AuditoriaRequestFrontend {
  transparencia_url: string;
  orgao_nome: string;
  site_url?: string;
  esfera: string;
  poder: string;
  dimensoes_selecionadas?: string[];
}

// Interface atualizada para corresponder ao backend real
export interface CriterioVerificado {
  dimensao: string;
  id_criterio: string;
  criterio: string;
  classificacao: 'Essencial' | 'Obrigatória' | 'Recomendada';
  fundamentacao_legal: string;
  disponivel: boolean;
  link_evidencia: string;
  texto_evidencia: string;
  metodo_encontrado: string;
  timestamp: string;
  observacoes: string;
}

export interface MetricasConformidade {
  criterios_conformes: number;
  total_criterios: number;
  percentual_geral: number;
}

// Interface atualizada para corresponder à resposta real do backend
export interface AuditoriaResponse {
  orgao: string;
  url_analisada: string;
  timestamp_auditoria: string;
  tempo_auditoria_segundos: number;
  metricas_conformidade: MetricasConformidade;
  criterios_verificados: CriterioVerificado[];
  links_evidencia: Array<{
    id_criterio: string;
    criterio: string;
    link: string;
    texto_evidencia: string;
  }>;
  filtro_aplicado?: {
    dimensoes_selecionadas?: string[];
    total_criterios_filtrados: number;
    auditoria_completa: boolean;
  };
}

// Interface para dados do mapa
export interface OrgaoMapa {
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
  municipio: string;
  distancia_manaus: number;
}

class ApiService {
  /**
   * Obtém dados dos órgãos para dropdowns da auditoria
   */
  static async obterOrgaos(): Promise<OrgaosData> {
    try {
      const response = await api.get<OrgaosData>('/api/orgaos-para-auditoria');
      return response.data;
    } catch (error) {
      console.error('Erro ao obter dados de órgãos:', error);
      throw new Error('Não foi possível carregar os dados dos órgãos.');
    }
  }

  /**
   * Obtém órgãos para o mapa com filtros opcionais
   */
  static async obterOrgaosMapa(filtros?: {
    esfera?: string;
    poder?: string;
    municipio?: string;
    raio_km?: number;
  }): Promise<OrgaoMapa[]> {
    try {
      const response = await api.get<OrgaoMapa[]>('/api/orgaos-mapa', {
        params: filtros
      });
      return response.data;
    } catch (error) {
      console.error('Erro ao obter dados do mapa:', error);
      throw new Error('Não foi possível carregar os dados do mapa.');
    }
  }

  /**
   * Obtém as dimensões disponíveis para um poder específico
   */
  static async obterDimensoesDisponiveis(poder: string, esfera: string = ""): Promise<DimensoesResponse> {
    try {
      const response = await api.get<DimensoesResponse>('/api/dimensoes-disponiveis', {
        params: { poder, esfera }
      });
      return response.data;
    } catch (error) {
      console.error('Erro ao obter dimensões:', error);
      throw new Error('Não foi possível carregar as dimensões disponíveis.');
    }
  }

  /**
   * Realiza auditoria real usando a API do backend
   */
  static async realizarAuditoria(request: AuditoriaRequestFrontend): Promise<AuditoriaResponse> {
    try {
      const response = await api.post<{
        status: string;
        resultado: AuditoriaResponse;
      }>('/api/auditoria/iniciar', request);

      if (response.data.status === 'completed') {
        return response.data.resultado;
      } else {
        throw new Error('Auditoria não foi concluída com sucesso');
      }
    } catch (error: any) {
      console.error('Erro ao realizar auditoria:', error);
      
      // Tratamento específico de erros
      if (error.response?.status === 400) {
        throw new Error(error.response.data?.detail || 'Dados da requisição inválidos');
      } else if (error.response?.status === 500) {
        throw new Error('Erro interno do servidor durante a auditoria');
      } else if (error.code === 'ECONNABORTED') {
        throw new Error('Auditoria demorou mais que o esperado. Tente novamente.');
      } else {
        throw new Error('Falha ao comunicar com o serviço de auditoria.');
      }
    }
  }

  /**
   * Método de conveniência para manter compatibilidade com código existente
   */
  static async realizarAuditoriaLegacy(siteUrl: string, transparenciaUrl?: string): Promise<AuditoriaResponse> {
    const request: AuditoriaRequestFrontend = {
      transparencia_url: transparenciaUrl || siteUrl,
      orgao_nome: new URL(siteUrl).hostname,
      site_url: siteUrl,
      esfera: "Municipal",
      poder: "Executivo"
    };

    return this.realizarAuditoria(request);
  }

  /**
   * Health check da API
   */
  static async verificarStatus(): Promise<{ status: string; environment?: string }> {
    try {
      const response = await api.get('/health');
      return response.data;
    } catch (error) {
      console.error('Erro no health check:', error);
      throw new Error('API não está respondendo');
    }
  }

  /**
   * Obter informações gerais da API
   */
  static async obterInfoAPI(): Promise<{ message: string; version: string }> {
    try {
      const response = await api.get('/');
      return response.data;
    } catch (error) {
      console.error('Erro ao obter info da API:', error);
      throw new Error('Não foi possível obter informações da API');
    }
  }
}

export default ApiService;