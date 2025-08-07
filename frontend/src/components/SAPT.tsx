import React, { useState, useEffect } from 'react';
import ApiService, { AuditoriaResponse } from '../services/api';

interface OrgaosData {
  [esfera: string]: {
    [poder: string]: {
      [orgao: string]: {
        site: string;
        transparencia: string;
      };
    };
  };
}

const SAPT: React.FC = () => {
  // Estados principais
  const [esfera, setEsfera] = useState('');
  const [poder, setPoder] = useState('');
  const [orgao, setOrgao] = useState('');
  
  // Dados e loading
  const [orgaosData, setOrgaosData] = useState<OrgaosData>({});
  const [orgaosLoading, setOrgaosLoading] = useState(true);
  const [isLoading, setIsLoading] = useState(false);
  const [resultados, setResultados] = useState<AuditoriaResponse | null>(null);
  
  // Interface e feedback
  const [view, setView] = useState<'filtros' | 'resultados'>('filtros');
  const [statusMessage, setStatusMessage] = useState('');
  const [progress, setProgress] = useState(0);
  const [error, setError] = useState<string | null>(null);

  // Opções dinâmicas dos dropdowns
  const [opcoesPoder, setOpcoesPoder] = useState<string[]>([]);
  const [opcoesOrgao, setOpcoesOrgao] = useState<string[]>([]);

  // Carregar dados dos órgãos na inicialização
  useEffect(() => {
    const carregarOrgaos = async () => {
      try {
        setOrgaosLoading(true);
        console.log('Carregando dados dos órgãos...');
        const data = await ApiService.obterOrgaos();
        setOrgaosData(data);
        setError(null);
        console.log('Dados carregados:', Object.keys(data));
      } catch (error: any) {
        setError(error.message);
        console.error('Erro ao carregar órgãos:', error);
      } finally {
        setOrgaosLoading(false);
      }
    };

    carregarOrgaos();
  }, []);

  // Atualizar poderes quando esfera muda
  useEffect(() => {
    setPoder('');
    setOrgao('');
    
    if (esfera && orgaosData[esfera]) {
      setOpcoesPoder(Object.keys(orgaosData[esfera]));
      console.log(`Poderes disponíveis para ${esfera}:`, Object.keys(orgaosData[esfera]));
    } else {
      setOpcoesPoder([]);
    }
  }, [esfera, orgaosData]);

  // Atualizar órgãos quando poder muda
  useEffect(() => {
    setOrgao('');
    
    if (esfera && poder && orgaosData[esfera] && orgaosData[esfera][poder]) {
      setOpcoesOrgao(Object.keys(orgaosData[esfera][poder]));
      console.log(`Órgãos disponíveis para ${poder}:`, Object.keys(orgaosData[esfera][poder]));
    } else {
      setOpcoesOrgao([]);
    }
  }, [esfera, poder, orgaosData]);

  // Função para iniciar auditoria
const handleBuscar = async () => {
  if (!esfera || !poder || !orgao) {
    alert('Por favor, selecione todos os campos!');
    return;
  }

  setIsLoading(true);
  setResultados(null);
  setProgress(0);
  setStatusMessage('Preparando auditoria...');
  setView('resultados');

  try {
    const orgaoData = orgaosData[esfera][poder][orgao];
    const dadosAuditoria = {
      transparencia_url: orgaoData.transparencia,
      orgao_nome: orgao,
      site_url: orgaoData.site,
      esfera: esfera,
      poder: poder
    };

    console.log('🚀 Iniciando auditoria:', dadosAuditoria);
    setStatusMessage('🚀 Conectando com o backend...');
    
    // ✅ FETCH DIRETO (funciona garantido)
    const response = await fetch('http://localhost:8000/api/auditoria/iniciar', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dadosAuditoria)
    });

    if (!response.ok) {
      throw new Error('Falha ao iniciar auditoria');
    }

    const result = await response.json();
    
    if (result.status !== 'started') {
      throw new Error(result.message || 'Erro ao iniciar auditoria');
    }

    // ===== ETAPA 2: POLLING PARA PROGRESSO =====
    const session_id = result.session_id;
    console.log(`📊 Acompanhando progresso da sessão: ${session_id}`);
    setStatusMessage('📡 Auditoria iniciada, monitorando progresso...');

    // Polling a cada 1 segundo
    const pollInterval = setInterval(async () => {
      try {
        const progressResponse = await fetch(`http://localhost:8000/api/progress/${session_id}`);
        
        if (!progressResponse.ok) {
          console.warn('Erro ao buscar progresso:', progressResponse.status);
          return;
        }
        
        const progressData = await progressResponse.json();
        console.log('📊 Progresso recebido:', progressData);

        // ===== ATUALIZAR UI COM PROGRESSO =====
        const percentage = progressData.percentage || 0;
        setProgress(percentage);
        setStatusMessage(progressData.status || 'Processando...');

        // ===== VERIFICAR SE CONCLUIU =====
        if (progressData.completed) {
          console.log('✅ Auditoria concluída!');
          clearInterval(pollInterval);
          
          if (progressData.resultado) {
            setResultados(progressData.resultado);
            setStatusMessage('🎉 Auditoria concluída com sucesso!');
            console.log('📋 Resultado final:', progressData.resultado);
          } else {
            setStatusMessage('⚠️ Auditoria concluída, mas sem resultado.');
          }
          
          setIsLoading(false);
        }
        
      } catch (pollError) {
        console.error('❌ Erro no polling:', pollError);
      }
    }, 1000);

    // ===== TIMEOUT DE SEGURANÇA (5 minutos) =====
    setTimeout(() => {
      if (isLoading) {
        console.warn('⏰ Timeout da auditoria');
        clearInterval(pollInterval);
        setStatusMessage('⏰ Timeout - auditoria demorou mais que 5 minutos');
        setIsLoading(false);
      }
    }, 300000);

  } catch (error: any) {
    console.error('❌ Erro na auditoria:', error);
    setStatusMessage(`❌ Erro: ${error.message}`);
    setIsLoading(false);
  }
};


  // Tela de loading inicial
  if (orgaosLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-100">
        <div className="text-center">
          <div className="animate-spin rounded-full h-16 w-16 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600 text-lg">Carregando dados dos órgãos...</p>
          <p className="text-gray-500 text-sm mt-2">Conectando com o backend...</p>
        </div>
      </div>
    );
  }

  // Tela de erro
  if (error && !orgaosData || Object.keys(orgaosData).length === 0) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-100">
        <div className="card max-w-md text-center">
          <div className="text-red-600 text-4xl mb-4">⚠️</div>
          <h2 className="text-xl font-bold text-red-600 mb-2">Erro de Conexão</h2>
          <p className="text-gray-600 mb-4">
            Não foi possível carregar os dados dos órgãos. 
            Verifique se o backend está rodando em http://localhost:8000
          </p>
          <p className="text-sm text-gray-500 mb-4">
            Erro: {error}
          </p>
          <button 
            onClick={() => window.location.reload()} 
            className="btn-primary"
          >
            Tentar Novamente
          </button>
        </div>
      </div>
    );
  }

  // Tela principal de filtros
  if (view === 'filtros') {
    return (
      <div className="min-h-screen p-4 flex flex-col items-center bg-gray-100">
        <div className="card max-w-xl w-full">
          <h1 className="text-2xl md:text-3xl font-bold text-blue-800 text-center mb-8">
            Sistema de Avaliação de Portais de Transparência
          </h1>

          <div className="text-sm text-gray-600 text-center mb-6">
            Dados carregados: {Object.keys(orgaosData).length} esferas disponíveis
          </div>

          {/* Filtro Esfera */}
          <div className="mb-5">
            <label className="block mb-1 font-medium text-gray-700">
              Selecione a Esfera:
            </label>
            <select
              className="input-field"
              value={esfera}
              onChange={e => {
                setEsfera(e.target.value);
                console.log('Esfera selecionada:', e.target.value);
              }}
            >
              <option value="">Selecione uma esfera...</option>
              {Object.keys(orgaosData).map(esferaOption => (
                <option key={esferaOption} value={esferaOption}>
                  {esferaOption}
                </option>
              ))}
            </select>
          </div>

          {/* Filtro Poder */}
          <div className="mb-5">
            <label className="block mb-1 font-medium text-gray-700">
              Poder:
            </label>
            <select
              className="input-field"
              value={poder}
              onChange={e => {
                setPoder(e.target.value);
                console.log('Poder selecionado:', e.target.value);
              }}
              disabled={!esfera}
            >
              <option value="">
                {!esfera ? 'Selecione a esfera primeiro...' : 'Selecione um poder...'}
              </option>
              {opcoesPoder.map(poderOption => (
                <option key={poderOption} value={poderOption}>
                  {poderOption}
                </option>
              ))}
            </select>
            {esfera && opcoesPoder.length === 0 && (
              <p className="text-sm text-gray-500 mt-1">
                Nenhum poder disponível para esta esfera.
              </p>
            )}
          </div>

          {/* Filtro Órgão */}
          <div className="mb-8">
            <label className="block mb-1 font-medium text-gray-700">
              Órgão:
            </label>
            <select
              className="input-field"
              value={orgao}
              onChange={e => {
                setOrgao(e.target.value);
                console.log('Órgão selecionado:', e.target.value);
              }}
              disabled={!poder}
            >
              <option value="">
                {!poder ? 'Selecione o poder primeiro...' : 'Selecione um órgão...'}
              </option>
              {opcoesOrgao.map(orgaoOption => (
                <option key={orgaoOption} value={orgaoOption}>
                  {orgaoOption}
                </option>
              ))}
            </select>
            {poder && opcoesOrgao.length === 0 && (
              <p className="text-sm text-gray-500 mt-1">
                Nenhum órgão disponível para este poder.
              </p>
            )}
          </div>

          {/* Botão Iniciar Auditoria */}
          <button
            className={`w-full py-3 text-lg font-bold rounded transition-all duration-200 ${
              (!esfera || !poder || !orgao || isLoading)
                ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
                : 'bg-blue-600 hover:bg-blue-700 text-white hover:shadow-lg transform hover:-translate-y-0.5'
            }`}
            disabled={isLoading || !esfera || !poder || !orgao}
            onClick={handleBuscar}
          >
            {isLoading ? (
              <div className="flex items-center justify-center">
                <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
                Iniciando Auditoria...
              </div>
            ) : (
              'Iniciar Auditoria'
            )}
          </button>

          {/* Debug Info */}
          <div className="mt-6 text-xs text-gray-400 space-y-1">
            <p>Esfera: {esfera || 'Não selecionada'}</p>
            <p>Poder: {poder || 'Não selecionado'}</p>
            <p>Órgão: {orgao || 'Não selecionado'}</p>
          </div>
        </div>
      </div>
    );
  }

  // Tela de resultados (será implementada no próximo passo)
  return (
    <div className="min-h-screen bg-gray-100 py-8 px-4">
      <div className="max-w-7xl mx-auto">
        <button
          onClick={() => {
            setView('filtros');
            setResultados(null);
            setProgress(0);
            setError(null);
          }}
          className="mb-4 text-blue-700 hover:underline flex items-center text-lg"
        >
          <span className="mr-2">←</span> Voltar aos Filtros
        </button>

        <div className="card">
          <h2 className="text-2xl font-bold text-blue-800 mb-4">
            Resultado da Auditoria
          </h2>
          
          {/* Status e Progress */}
          <div className="mb-6 p-4 bg-gray-50 rounded-lg">
            <p className="mb-3">
              <span className="font-semibold">Esfera:</span> {esfera}<br />
              <span className="font-semibold">Poder:</span> {poder}<br />
              <span className="font-semibold">Órgão:</span> {orgao}
            </p>

            {/* Barra de Progresso */}
            {isLoading && (
              <div className="space-y-3">
                <div className="flex justify-between items-center">
                  <span className="text-sm font-medium text-blue-700">
                    {statusMessage}
                  </span>
                  <span className="text-sm font-medium text-blue-700">
                    {Math.round(progress)}%
                  </span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-3">
                  <div
                    className="bg-blue-600 h-3 rounded-full transition-all duration-500 ease-out"
                    style={{ width: `${progress}%` }}
                  ></div>
                </div>
                <button
                  onClick={() => {
                    setIsLoading(false);
                    setStatusMessage('Auditoria cancelada pelo usuário.');
                  }}
                  className="mt-3 px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700 transition text-sm"
                >
                  Cancelar Auditoria
                </button>
              </div>
            )}

            {/* Status Final */}
            {!isLoading && statusMessage && (
              <div className={`p-3 rounded-lg ${
                statusMessage.includes('Erro') 
                  ? 'bg-red-50 text-red-700 border border-red-200' 
                  : 'bg-green-50 text-green-700 border border-green-200'
              }`}>
                <p className="font-medium">{statusMessage}</p>
              </div>
            )}
          </div>

          {/* Resultados Completos */}
{resultados && (
  <div className="space-y-6">
    {/* Métricas */}
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div className="bg-blue-50 p-4 rounded-lg border border-blue-200">
        <div className="text-2xl font-bold text-blue-800">
          {resultados.metricas_conformidade.percentual_geral.toFixed(1)}%
        </div>
        <div className="text-sm text-blue-600">Conformidade Geral</div>
        <div className="text-xs text-blue-500">
          {resultados.metricas_conformidade.criterios_conformes} de{' '}
          {resultados.metricas_conformidade.total_criterios} critérios
        </div>
      </div>
      
      <div className="bg-green-50 p-4 rounded-lg border border-green-200">
        <div className="text-2xl font-bold text-green-800">
          {resultados.metricas_conformidade.criterios_conformes}
        </div>
        <div className="text-sm text-green-600">Critérios Conformes</div>
        <div className="text-xs text-green-500">
          Atendidos pela instituição
        </div>
      </div>

      <div className="bg-gray-50 p-4 rounded-lg border border-gray-200">
        <div className="text-2xl font-bold text-gray-800">
          {resultados.tempo_auditoria_segundos.toFixed(1)}s
        </div>
        <div className="text-sm text-gray-600">Tempo de Auditoria</div>
        <div className="text-xs text-gray-500">
          Duração total da análise
        </div>
      </div>
    </div>

    {/* Tabela de Critérios */}
    <div className="bg-white rounded-lg shadow">
      <div className="px-6 py-4 border-b border-gray-200">
        <h3 className="text-xl font-bold text-gray-900">
          Resultados Detalhados por Critério ({resultados.criterios_verificados.length} critérios)
        </h3>
      </div>
      
      <div className="overflow-x-auto">
        <table className="w-full text-sm">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-4 py-3 text-left font-medium text-gray-900">Dimensão</th>
              <th className="px-4 py-3 text-left font-medium text-gray-900">ID</th>
              <th className="px-4 py-3 text-left font-medium text-gray-900">Critério</th>
              <th className="px-4 py-3 text-center font-medium text-gray-900">Classificação</th>
              <th className="px-4 py-3 text-center font-medium text-gray-900">Status</th>
              <th className="px-4 py-3 text-center font-medium text-gray-900">Evidência</th>
              <th className="px-4 py-3 text-center font-medium text-gray-900">Método</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200">
            {resultados.criterios_verificados.map((item, index) => (
              <tr key={index} className={index % 2 === 0 ? 'bg-white' : 'bg-gray-50'}>
                <td className="px-4 py-3 text-gray-900">{item.dimensao}</td>
                <td className="px-4 py-3 font-medium text-blue-600">{item.id_criterio}</td>
                <td className="px-4 py-3 text-gray-700 max-w-xs">
                  <div className="truncate" title={item.criterio}>
                    {item.criterio}
                  </div>
                </td>
                <td className="px-4 py-3 text-center">
                  <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${
                    item.classificacao === 'Essencial' 
                      ? 'bg-red-100 text-red-800' 
                      : item.classificacao === 'Obrigatória' 
                      ? 'bg-yellow-100 text-yellow-800' 
                      : 'bg-green-100 text-green-800'
                  }`}>
                    {item.classificacao}
                  </span>
                </td>
                <td className="px-4 py-3 text-center">
                  <span className={`inline-flex items-center px-2 py-1 rounded-full text-xs font-medium ${
                    item.disponivel 
                      ? 'bg-green-100 text-green-800' 
                      : 'bg-red-100 text-red-800'
                  }`}>
                    {item.disponivel ? '✅ Conforme' : '❌ Não Conforme'}
                  </span>
                </td>
                <td className="px-4 py-3 text-center">
                  {item.link_evidencia ? (
                    <a
                      href={item.link_evidencia}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-blue-600 hover:text-blue-800 hover:underline"
                    >
                      🔗 Ver
                    </a>
                  ) : (
                    <span className="text-gray-400">N/A</span>
                  )}
                </td>
                <td className="px-4 py-3 text-gray-600 text-xs max-w-32">
                  <div className="truncate" title={item.metodo_encontrado}>
                    {item.metodo_encontrado}
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>

    {/* Ações */}
    <div className="flex flex-col sm:flex-row gap-4 justify-between">
      <button
        onClick={() => {
          setView('filtros');
          setResultados(null);
          setProgress(0);
          setError(null);
        }}
        className="btn-secondary"
      >
        🔄 Nova Auditoria
      </button>
      
      <div className="flex gap-2">
        <button
          onClick={() => {
            alert('Funcionalidade de exportação em desenvolvimento');
          }}
          className="btn-primary"
        >
          📊 Exportar Excel
        </button>
        
        <button
          onClick={() => {
            window.print();
          }}
          className="btn-primary"
        >
          🖨️ Imprimir
        </button>
      </div>
    </div>
  </div>
)}
          
        </div>
      </div>
    </div>
  );
};

export default SAPT;
