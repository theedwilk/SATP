// Conteúdo do arquivo: src/services/api.ts

import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
});

// Interface para os dados de órgãos usados nos dropdowns da AuditoriaPage
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

// Interfaces para a resposta da auditoria
export interface CriterioVerificado {
  dimensao: string;
  id_criterio: string;
  criterio: string;
  classificacao: 'Essencial' | 'Obrigatória' | 'Recomendada';
  disponivel: boolean;
  link_evidencia?: string;
  metodo_encontrado: string;
}

export interface MetricasConformidade {
  total_criterios: number;
  criterios_conformes: number;
  percentual_geral: number;
}

export interface AuditoriaResponse {
  orgao_auditado: string;
  url_site: string;
  url_transparencia?: string;
  data_auditoria: string;
  tempo_auditoria_segundos: number;
  metricas_conformidade: MetricasConformidade;
  criterios_verificados: CriterioVerificado[];
  // Adicione outros campos se sua API retornar
}

class ApiService {
  /**
   * Obtém uma lista hierárquica de órgãos para preencher os dropdowns de filtro.
   * Na vida real, esta função faria uma chamada à sua API.
   */
  static async obterOrgaos(): Promise<OrgaosData> {
    try {
      // Exemplo de chamada real à API:
      // const response = await api.get<OrgaosData>('/api/orgaos-para-auditoria');
      // return response.data;
      
      // Dados mockados para simular o retorno da API enquanto a API real não está pronta
      const mockData: OrgaosData = {
        'Federal': {
          'Executivo': {
            'Presidência da República': { site: 'http://www.gov.br', transparencia: 'http://www.gov.br/transparencia' },
            'Ministério da Fazenda': { site: 'http://www.fazenda.gov.br', transparencia: 'http://www.fazenda.gov.br/acesso-a-informacao' },
            'Ministério da Saúde': { site: 'http://www.saude.gov.br', transparencia: 'http://www.saude.gov.br/acesso-a-informacao' },
          },
          'Legislativo': {
            'Câmara dos Deputados': { site: 'http://www.camara.leg.br', transparencia: 'http://www.camara.leg.br/transparencia' },
            'Senado Federal': { site: 'http://www.senado.leg.br', transparencia: 'http://www.senado.leg.br/transparencia' },
          },
          'Judiciário': {
            'Supremo Tribunal Federal': { site: 'http://www.stf.jus.br', transparencia: 'http://www.stf.jus.br/portal/transparencia' },
          },
        },
        'Estadual': {
          'Executivo': {
            'Governo do Amazonas': { site: 'http://www.amazonas.am.gov.br', transparencia: 'http://www.amazonas.am.gov.br/transparencia' },
            'Secretaria de Saúde do AM': { site: 'http://www.saude.am.gov.br', transparencia: 'http://www.saude.am.gov.br/transparencia' },
          },
          'Legislativo': {
            'Assembleia Legislativa do AM': { site: 'http://www.aleam.gov.br', transparencia: 'http://www.aleam.gov.br/transparencia' },
          },
        },
        'Municipal': {
          'Executivo': {
            'Prefeitura de Manaus': { site: 'http://www.manaus.am.gov.br', transparencia: 'http://www.manaus.am.gov.br/transparencia' },
          },
        },
      };
      return mockData;
    } catch (error) {
      console.error('Erro ao obter dados de órgãos:', error);
      throw new Error('Não foi possível carregar os dados dos órgãos.');
    }
  }

  /**
   * Realiza uma auditoria em um site e/ou portal de transparência.
   * Na vida real, esta função faria uma chamada POST para sua API de auditoria.
   */
  static async realizarAuditoria(siteUrl: string, transparenciaUrl?: string): Promise<AuditoriaResponse> {
    try {
      // Exemplo de chamada real à API:
      // const response = await api.post<AuditoriaResponse>('/api/auditoria', { siteUrl, transparenciaUrl });
      // return response.data;

      // Simulação de uma resposta de auditoria para fins de desenvolvimento
      await new Promise(resolve => setTimeout(resolve, 2000)); // Simula delay da API

      const mockResultados: CriterioVerificado[] = [
        {
          dimensao: 'Acesso à Informação',
          id_criterio: 'AI-001',
          criterio: 'Disponibilização de informações sobre a estrutura organizacional.',
          classificacao: 'Essencial',
          disponivel: true,
          link_evidencia: `${siteUrl}/estrutura`,
          metodo_encontrado: 'Análise de conteúdo web',
        },
        {
          dimensao: 'Acesso à Informação',
          id_criterio: 'AI-002',
          criterio: 'Publicação de dados sobre despesas e receitas.',
          classificacao: 'Obrigatória',
          disponivel: Math.random() > 0.3, // Aleatório para simular falhas
          link_evidencia: Math.random() > 0.3 ? `${transparenciaUrl}/orcamento` : undefined,
          metodo_encontrado: 'Verificação de links e palavras-chave',
        },
        {
          dimensao: 'Governança de Dados',
          id_criterio: 'GD-001',
          criterio: 'Política de privacidade clara e acessível.',
          classificacao: 'Recomendada',
          disponivel: Math.random() > 0.1,
          link_evidencia: Math.random() > 0.1 ? `${siteUrl}/privacidade` : undefined,
          metodo_encontrado: 'Busca por termos específicos',
        },
        {
          dimensao: 'Usabilidade',
          id_criterio: 'US-001',
          criterio: 'Navegação intuitiva no portal de transparência.',
          classificacao: 'Recomendada',
          disponivel: Math.random() > 0.5,
          link_evidencia: undefined,
          metodo_encontrado: 'Análise heurística (simulada)',
        },
        {
          dimensao: 'Transparência Ativa',
          id_criterio: 'TA-001',
          criterio: 'Publicação de informações sobre licitações e contratos.',
          classificacao: 'Essencial',
          disponivel: Math.random() > 0.2,
          link_evidencia: Math.random() > 0.2 ? `${transparenciaUrl}/licitacoes` : undefined,
          metodo_encontrado: 'Verificação de links e estrutura de menu',
        },
      ];

      const conformes = mockResultados.filter(c => c.disponivel).length;
      const total = mockResultados.length;
      const percentual = total > 0 ? (conformes / total) * 100 : 0;

      const response: AuditoriaResponse = {
        orgao_auditado: siteUrl, // Ou o nome do órgão
        url_site: siteUrl,
        url_transparencia: transparenciaUrl,
        data_auditoria: new Date().toISOString(),
        tempo_auditoria_segundos: 5 + Math.random() * 10, // Simula tempo
        metricas_conformidade: {
          total_criterios: total,
          criterios_conformes: conformes,
          percentual_geral: parseFloat(percentual.toFixed(1)),
        },
        criterios_verificados: mockResultados,
      };

      return response;

    } catch (error) {
      console.error('Erro ao realizar auditoria:', error);
      throw new Error('Falha ao comunicar com o serviço de auditoria.');
    }
  }
}

export default ApiService;
