const API_BASE_URL = 'http://localhost:8000/api';

export interface AuditoriaRequest {
  transparencia_url: string;
  orgao_nome: string;
  site_url?: string;
  esfera: string;
  poder: string;
}

export interface CriterioResponse {
  dimensao: string;
  id_criterio: string;
  criterio: string;
  classificacao: string;
  fundamentacao_legal: string;
  disponivel: boolean;
  link_evidencia: string;
  texto_evidencia: string;
  metodo_encontrado: string;
  timestamp: string;
  observacoes: string;
}

export interface AuditoriaResponse {
  orgao: string;
  url_analisada: string;
  timestamp_auditoria: string;
  tempo_auditoria_segundos: number;
  metricas_conformidade: {
    criterios_conformes: number;
    total_criterios: number;
    percentual_geral: number;
  };
  criterios_verificados: CriterioResponse[];
  links_evidencia: Array<{
    id_criterio: string;
    criterio: string;
    link: string;
    texto_evidencia: string;
  }>;
}

class ApiService {
  async obterOrgaos(): Promise<any> {
    try {
      const response = await fetch(`${API_BASE_URL}/orgaos`);
      if (!response.ok) throw new Error('Falha ao obter órgãos');
      return await response.json();
    } catch (error) {
      console.error('Erro ao obter órgãos:', error);
      throw error;
    }
  }

  async iniciarAuditoria(dadosAuditoria: AuditoriaRequest): Promise<{ status: string; resultado: AuditoriaResponse }> {
    try {
      const response = await fetch(`${API_BASE_URL}/auditoria/iniciar`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(dadosAuditoria)
      });
      
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Falha ao iniciar auditoria');
      }
      
      return await response.json();
    } catch (error) {
      console.error('Erro ao iniciar auditoria:', error);
      throw error;
    }
  }
}

export default new ApiService();
