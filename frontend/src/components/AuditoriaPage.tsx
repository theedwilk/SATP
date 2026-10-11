import React, { useState, useEffect } from 'react';
import ApiService, { AuditoriaResponse, OrgaosData } from '../services/api';
import { OrgaosApiService } from '../services/orgaosApi';
import { OrgaoMap, FiltrosOrgaos as FiltrosType } from '../types/orgaos';
import MapaOrgaos from './MapaOrgaos';
import FiltrosOrgaos from './FiltrosOrgaos';

const AuditoriaPage: React.FC = () => {
  // Estado unificado para filtros
  const [filters, setFilters] = useState<FiltrosType>({
    esfera: '',
    poder: '',
    orgao: '',
    municipio: '',
    raio_km: undefined
  });

  // Novos estados para dimensões
  const [dimensoesDisponiveis, setDimensoesDisponiveis] = useState<string[]>([]);
  const [dimensoesSelecionadas, setDimensoesSelecionadas] = useState<string[]>([]);
  const [mostrarFiltrosDimensoes, setMostrarFiltrosDimensoes] = useState(false);
  const [carregandoDimensoes, setCarregandoDimensoes] = useState(false);

  // Dados e loading
  const [orgaosData, setOrgaosData] = useState<OrgaosData>({});
  const [orgaosParaMapa, setOrgaosParaMapa] = useState<OrgaoMap[]>([]);
  const [orgaosLoading, setOrgaosLoading] = useState(true);
  const [isLoading, setIsLoading] = useState(false);
  const [resultados, setResultados] = useState<AuditoriaResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [progress, setProgress] = useState(0);
  const [statusMessage, setStatusMessage] = useState('');

  // NOVO: Estado para debug
  const [debugInfo, setDebugInfo] = useState<{
    apiUrl: string;
    tentativas: number;
    ultimoErro: string | null;
  }>({
    apiUrl: '',
    tentativas: 0,
    ultimoErro: null
  });

  // Funções para o componente FiltrosOrgaos
  const onFilterChange = (filterName: keyof FiltrosType, value: string | number | undefined) => {
    setFilters(prev => ({
      ...prev,
      [filterName]: value
    }));
  };

  const onResetFilters = () => {
    setFilters({
      esfera: '',
      poder: '',
      orgao: '',
      municipio: '',
      raio_km: undefined
    });
    setDimensoesSelecionadas([]);
  };

  // MELHORADO: Função para testar conexão com a API
  const testarConexaoAPI = async () => {
    try {
      console.log('🔍 Testando conexão com a API...');
      
      // Primeiro, vamos verificar o health check
      const healthStatus = await ApiService.verificarStatus();
      console.log('✅ Health check passou:', healthStatus);
      
      // Depois verificar as informações da API
      const apiInfo = await ApiService.obterInfoAPI();
      console.log('✅ Info da API:', apiInfo);
      
      return true;
    } catch (error: any) {
      console.error('❌ Falha na conexão com a API:', error);
      setDebugInfo(prev => ({
        ...prev,
        ultimoErro: error.message
      }));
      return false;
    }
  };

  // MELHORADO: Carregar dados dos órgãos com melhor tratamento de erro
  useEffect(() => {
    const carregarDados = async () => {
      try {
        setOrgaosLoading(true);
        setError(null);
        
        // Atualizar info de debug
        const apiUrl = process.env.REACT_APP_API_URL || window.location.origin;
        setDebugInfo(prev => ({
          ...prev,
          apiUrl,
          tentativas: prev.tentativas + 1
        }));
        
        console.log('🚀 Iniciando carregamento de dados...');
        console.log('📍 API URL:', apiUrl);
        
        // Testar conexão primeiro
        const conexaoOK = await testarConexaoAPI();
        if (!conexaoOK) {
          throw new Error('Falha na conexão com a API');
        }
        
        // Carregar dados para dropdowns
        console.log('📦 Carregando dados dos órgãos...');
        const dataDropdowns = await ApiService.obterOrgaos();
        console.log('✅ Dados dos órgãos carregados:', Object.keys(dataDropdowns));
        setOrgaosData(dataDropdowns);
        
        // Carregar dados para mapa
        try {
          console.log('🗺️ Carregando dados do mapa...');
          const resultadoBusca = await OrgaosApiService.buscarOrgaosMapa({});
          setOrgaosParaMapa(resultadoBusca.orgaos);
          console.log('📍 Dados do mapa carregados:', resultadoBusca.orgaos.length, 'órgãos');
        } catch (mapaError) {
          console.warn('⚠️ Erro ao carregar dados do mapa:', mapaError);
          // Não falha o carregamento geral se só o mapa falhar
        }
        
        setError(null);
        
      } catch (err: any) {
        console.error('❌ Erro ao carregar dados:', err);
        
        // Melhor tratamento de erros específicos
        let errorMessage = 'Erro desconhecido ao carregar dados';
        
        if (err.code === 'ECONNREFUSED') {
          errorMessage = 'Não foi possível conectar ao servidor. Verifique se o backend está rodando.';
        } else if (err.response?.status === 404) {
          errorMessage = 'Endpoint da API não encontrado. Verifique se o backend tem a rota /api/orgaos-para-auditoria';
        } else if (err.response?.status === 500) {
          errorMessage = 'Erro interno do servidor. Verifique os logs do backend.';
        } else if (err.message) {
          errorMessage = err.message;
        }
        
        setError(errorMessage);
        setDebugInfo(prev => ({
          ...prev,
          ultimoErro: errorMessage
        }));
        
      } finally {
        setOrgaosLoading(false);
      }
    };
    
    carregarDados();
  }, []);

  // Resto do código permanece igual...
  // (mantendo todas as outras funções como estavam)

  // Carregar dimensões quando poder mudar
  useEffect(() => {
    const carregarDimensoes = async () => {
      if (filters.poder && filters.esfera) {
        try {
          setCarregandoDimensoes(true);
          const response = await ApiService.obterDimensoesDisponiveis(filters.poder, filters.esfera);
          setDimensoesDisponiveis(response.dimensoes);
          setDimensoesSelecionadas([]);
          console.log('📋 Dimensões carregadas:', response.dimensoes.length);
        } catch (err) {
          console.error('Erro ao carregar dimensões:', err);
          setDimensoesDisponiveis([]);
        } finally {
          setCarregandoDimensoes(false);
        }
      } else {
        setDimensoesDisponiveis([]);
        setDimensoesSelecionadas([]);
      }
    };
    carregarDimensoes();
  }, [filters.poder, filters.esfera]);

  // Opções para os dropdowns
  const opcoesEsfera = Object.keys(orgaosData);
  const opcoesPoder = filters.esfera ? Object.keys(orgaosData[filters.esfera]) : [];
  const opcoesOrgao = filters.esfera && filters.poder ? Object.keys(orgaosData[filters.esfera][filters.poder]) : [];

  // Resto dos useEffects e funções permanecem iguais...

  return (
    <div className="flex flex-col h-full bg-gray-100">
      <header className="bg-white shadow-md p-6">
        <h1 className="text-3xl font-bold text-blue-800 text-center">
          Sistema de Avaliação de Portais de Transparência
        </h1>
        <p className="text-gray-600 text-center mt-2">
          Selecione os critérios para iniciar a auditoria de um órgão.
        </p>
      </header>

      <div className="flex-1 p-8 overflow-y-auto">
        {/* NOVO: Seção de Debug quando há erro */}
        {error && (
          <div className="card mb-8 border-l-4 border-red-500 bg-red-50">
            <h2 className="text-xl font-bold text-red-800 mb-4">
              🚨 Erro de Conexão
            </h2>
            <div className="space-y-2 text-sm">
              <p className="text-red-700 font-medium">
                <strong>Erro:</strong> {error}
              </p>
              <div className="bg-white p-3 rounded border border-red-200">
                <h4 className="font-medium text-red-800 mb-2">Informações de Debug:</h4>
                <ul className="space-y-1 text-red-600">
                  <li><strong>API URL:</strong> {debugInfo.apiUrl}</li>
                  <li><strong>Tentativas:</strong> {debugInfo.tentativas}</li>
                  <li><strong>Último erro:</strong> {debugInfo.ultimoErro}</li>
                </ul>
              </div>
              <div className="bg-yellow-50 p-3 rounded border border-yellow-200">
                <h4 className="font-medium text-yellow-800 mb-2">Possíveis soluções:</h4>
                <ul className="space-y-1 text-yellow-700 text-xs">
                  <li>• Verifique se o backend está rodando na porta 8000</li>
                  <li>• Confirme se a rota /api/orgaos-para-auditoria existe</li>
                  <li>• Verifique se não há problemas de CORS</li>
                  <li>• Teste manualmente: curl http://localhost:8000/api/orgaos-para-auditoria</li>
                </ul>
              </div>
              <button
                onClick={() => window.location.reload()}
                className="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700 transition"
              >
                🔄 Tentar Novamente
              </button>
            </div>
          </div>
        )}

        <div className="card mb-8">
          <h2 className="text-2xl font-bold text-blue-800 mb-4">
            Selecionar Órgão para Avaliação
          </h2>

          {orgaosLoading ? (
            <div className="text-center py-8">
              <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mb-4"></div>
              <p className="text-gray-600">Carregando opções de órgãos...</p>
              <p className="text-xs text-gray-500 mt-2">
                Conectando com: {debugInfo.apiUrl}
              </p>
            </div>
          ) : error && !Object.keys(orgaosData).length ? (
            <p className="text-red-600">❌ Não foi possível carregar as opções de órgãos.</p>
          ) : (
            <div>
              <FiltrosOrgaos
                filters={filters}
                onFilterChange={onFilterChange}
                opcoesEsfera={opcoesEsfera}
                opcoesPoder={opcoesPoder}
                opcoesOrgao={opcoesOrgao}
                isLoading={isLoading}
                onResetFilters={onResetFilters}
              />
              
              {/* Resto do componente permanece igual... */}
            </div>
          )}
        </div>
        
        {/* Resto do JSX permanece igual... */}
      </div>
    </div>
  );
};

export default AuditoriaPage;