import React, { useState, useEffect } from 'react';
import ApiService, { AuditoriaResponse, OrgaosData } from '../services/api';
import { OrgaosApiService } from '../services/orgaosApi';
import { OrgaoMap } from '../types/orgaos';
import MapaOrgaos from './MapaOrgaos';

const AuditoriaPage: React.FC = () => {
  // Estados principais para os filtros
  const [esfera, setEsfera] = useState('');
  const [poder, setPoder] = useState('');
  const [orgao, setOrgao] = useState('');

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

  // Carregar dados dos órgãos para os dropdowns na inicialização
  useEffect(() => {
    const carregarDados = async () => {
      try {
        setOrgaosLoading(true);

        // Carregar dados para dropdowns
        const dataDropdowns = await ApiService.obterOrgaos();
        setOrgaosData(dataDropdowns);

        // Carregar dados para mapa
        try {
          const resultadoBusca = await OrgaosApiService.buscarOrgaosMapa({});
          setOrgaosParaMapa(resultadoBusca.orgaos);
          console.log('📍 Dados do mapa carregados:', resultadoBusca.orgaos.length, 'órgãos');
        } catch (mapaError) {
          console.warn('⚠️ Erro ao carregar dados do mapa:', mapaError);
        }

        setError(null);
      } catch (err: any) {
        setError(err.message);
        console.error('Erro ao carregar dados:', err);
      } finally {
        setOrgaosLoading(false);
      }
    };
    carregarDados();
  }, []);

  // Carregar dimensões quando poder mudar
  useEffect(() => {
    const carregarDimensoes = async () => {
      if (poder && esfera) {
        try {
          setCarregandoDimensoes(true);
          const response = await ApiService.obterDimensoesDisponiveis(poder, esfera);
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
  }, [poder, esfera]);

  // Opções para os dropdowns
  const opcoesEsfera = Object.keys(orgaosData);
  const opcoesPoder = esfera ? Object.keys(orgaosData[esfera]) : [];
  const opcoesOrgao = esfera && poder ? Object.keys(orgaosData[esfera][poder]) : [];

  // Resetar poder e órgão quando a esfera muda
  useEffect(() => {
    setPoder('');
    setOrgao('');
  }, [esfera]);

  // Resetar órgão quando o poder muda
  useEffect(() => {
    setOrgao('');
  }, [poder]);

  // Atualizar mapa quando filtros mudam
  useEffect(() => {
    const atualizarMapa = async () => {
      if (esfera || poder || orgao) {
        try {
          const filtros: any = {};

          if (esfera) filtros.esfera = esfera;
          if (poder) filtros.poder = poder;

          if (esfera === 'Municipal' && orgao) {
            if (orgao.includes('Prefeitura de ')) {
              filtros.municipio = orgao.replace('Prefeitura de ', '');
            } else if (orgao.includes('Câmara Municipal de ')) {
              filtros.municipio = orgao.replace('Câmara Municipal de ', '');
            }
          }

          const resultadoBusca = await OrgaosApiService.buscarOrgaosMapa(filtros);
          setOrgaosParaMapa(resultadoBusca.orgaos);
          console.log('🔄 Mapa atualizado:', resultadoBusca.orgaos.length, 'órgãos encontrados');
        } catch (err) {
          console.error('Erro ao atualizar mapa:', err);
        }
      }
    };

    if (esfera || poder || orgao) {
      atualizarMapa();
    }
  }, [esfera, poder, orgao]);

  // Função para toggle de dimensões
  const toggleDimensao = (dimensao: string) => {
    setDimensoesSelecionadas(prev => {
      if (prev.includes(dimensao)) {
        return prev.filter(d => d !== dimensao);
      } else {
        return [...prev, dimensao];
      }
    });
  };

  // Função handleBuscar atualizada
  const handleBuscar = async () => {
    if (!esfera || !poder || !orgao) {
      setError('Por favor, selecione Esfera, Poder e Órgão.');
      return;
    }

    setIsLoading(true);
    setResultados(null);
    setError(null);
    setProgress(0);
    setStatusMessage('Preparando auditoria...');

    try {
      const orgaoData = orgaosData[esfera][poder][orgao];
      const dadosAuditoria = {
        transparencia_url: orgaoData.transparencia,
        orgao_nome: orgao,
        site_url: orgaoData.site,
        esfera: esfera,
        poder: poder,
        dimensoes_selecionadas: dimensoesSelecionadas.length > 0 ? dimensoesSelecionadas : undefined
      };

      console.log('🚀 Iniciando auditoria:', dadosAuditoria);

      if (dimensoesSelecionadas.length > 0) {
        setStatusMessage(`🎯 Auditoria seletiva: ${dimensoesSelecionadas.length} dimensões selecionadas`);
      } else {
        setStatusMessage('🚀 Conectando com o backend...');
      }

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

      if (result.status === 'completed') {
        console.log('✅ Auditoria concluída diretamente!');
        setResultados(result.resultado);
        setStatusMessage('🎉 Auditoria concluída com sucesso!');
        setProgress(100);
        setIsLoading(false);
        return;
      }

      if (result.status !== 'started') {
        throw new Error(result.message || 'Erro ao iniciar auditoria');
      }

      // Polling para progresso
      const session_id = result.session_id;
      console.log(`📊 Acompanhando progresso da sessão: ${session_id}`);
      setStatusMessage('📡 Auditoria iniciada, monitorando progresso...');

      const pollInterval = setInterval(async () => {
        try {
          const progressResponse = await fetch(`http://localhost:8000/api/progress/${session_id}`);
          if (!progressResponse.ok) {
            console.warn('Erro ao buscar progresso:', progressResponse.status);
            return;
          }

          const progressData = await progressResponse.json();
          console.log('📊 Progresso recebido:', progressData);

          const percentage = progressData.percentage || 0;
          setProgress(percentage);
          setStatusMessage(progressData.status || 'Processando...');

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

      // Timeout de segurança (5 minutos)
      setTimeout(() => {
        if (isLoading) {
          console.warn('⏰ Timeout da auditoria');
          clearInterval(pollInterval);
          setStatusMessage('⏰ Timeout - auditoria demorou mais que 5 minutos');
          setIsLoading(false);
        }
      }, 300000);

    } catch (err: any) {
      console.error('❌ Erro na auditoria:', err);
      setStatusMessage(`❌ Erro: ${err.message}`);
      setIsLoading(false);
    }
  };

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
        <div className="card mb-8">
          <h2 className="text-2xl font-bold text-blue-800 mb-4">
            Selecionar Órgão para Avaliação
          </h2>
          {orgaosLoading ? (
            <p className="text-gray-600">Carregando opções de órgãos...</p>
          ) : error && !Object.keys(orgaosData).length ? (
            <p className="text-red-600">Erro ao carregar opções: {error}</p>
          ) : (
            <div>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                <div>
                  <label htmlFor="esfera" className="block text-sm font-medium text-gray-700 mb-1">
                    Esfera
                  </label>
                  <select
                    id="esfera"
                    value={esfera}
                    onChange={(e) => setEsfera(e.target.value)}
                    className="form-select"
                    disabled={isLoading}
                  >
                    <option value="">Selecione a Esfera</option>
                    {opcoesEsfera.map((opt) => (
                      <option key={opt} value={opt}>
                        {opt}
                      </option>
                    ))}
                  </select>
                </div>
                <div>
                  <label htmlFor="poder" className="block text-sm font-medium text-gray-700 mb-1">
                    Poder
                  </label>
                  <select
                    id="poder"
                    value={poder}
                    onChange={(e) => setPoder(e.target.value)}
                    className="form-select"
                    disabled={isLoading || !esfera}
                  >
                    <option value="">Selecione o Poder</option>
                    {opcoesPoder.map((opt) => (
                      <option key={opt} value={opt}>
                        {opt}
                      </option>
                    ))}
                  </select>
                </div>
                <div>
                  <label htmlFor="orgao" className="block text-sm font-medium text-gray-700 mb-1">
                    Órgão
                  </label>
                  <select
                    id="orgao"
                    value={orgao}
                    onChange={(e) => setOrgao(e.target.value)}
                    className="form-select"
                    disabled={isLoading || !poder}
                  >
                    <option value="">Selecione o Órgão</option>
                    {opcoesOrgao.map((opt) => (
                      <option key={opt} value={opt}>
                        {opt}
                      </option>
                    ))}
                  </select>
                </div>
              </div>

              {/* Nova seção: filtros de dimensões */}
              {poder && esfera && (
                <div className="mt-6 p-4 bg-gray-50 rounded-lg border">
                  <div className="flex items-center justify-between mb-3">
                    <h3 className="text-lg font-semibold text-gray-800">
                      🎯 Auditoria Seletiva (Opcional)
                    </h3>
                    <button
                      onClick={() => setMostrarFiltrosDimensoes(!mostrarFiltrosDimensoes)}
                      className="text-blue-600 hover:text-blue-800 font-medium"
                    >
                      {mostrarFiltrosDimensoes ? '🔼 Ocultar Filtros' : '🔽 Mostrar Filtros'}
                    </button>
                  </div>

                  <p className="text-sm text-gray-600 mb-3">
                    Selecione dimensões específicas para uma auditoria mais rápida e focada.
                    Se nenhuma for selecionada, será feita auditoria completa.
                  </p>

                  {mostrarFiltrosDimensoes && (
                    <div>
                      {carregandoDimensoes ? (
                        <p className="text-gray-500">Carregando dimensões...</p>
                      ) : dimensoesDisponiveis.length > 0 ? (
                        <div>
                          <div className="flex flex-wrap gap-2 mb-3">
                            <button
                              onClick={() => setDimensoesSelecionadas([])}
                              className="px-3 py-1 text-xs bg-gray-200 text-gray-700 rounded hover:bg-gray-300"
                            >
                              🔄 Limpar Seleção
                            </button>
                            <button
                              onClick={() => setDimensoesSelecionadas([...dimensoesDisponiveis])}
                              className="px-3 py-1 text-xs bg-blue-100 text-blue-700 rounded hover:bg-blue-200"
                            >
                              ✅ Selecionar Todas
                            </button>
                          </div>

                          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2">
                            {dimensoesDisponiveis.map((dimensao) => (
                              <label
                                key={dimensao}
                                className="flex items-center space-x-2 p-2 bg-white rounded border hover:bg-blue-50 cursor-pointer"
                              >
                                <input
                                  type="checkbox"
                                  checked={dimensoesSelecionadas.includes(dimensao)}
                                  onChange={() => toggleDimensao(dimensao)}
                                  className="rounded text-blue-600"
                                />
                                <span className="text-sm text-gray-700">{dimensao}</span>
                              </label>
                            ))}
                          </div>

                          {dimensoesSelecionadas.length > 0 && (
                            <div className="mt-3 p-2 bg-blue-50 rounded border border-blue-200">
                              <p className="text-sm text-blue-700">
                                ✅ <strong>{dimensoesSelecionadas.length}</strong> dimensões selecionadas de <strong>{dimensoesDisponiveis.length}</strong> disponíveis
                              </p>
                            </div>
                          )}
                        </div>
                      ) : (
                        <p className="text-gray-500">Nenhuma dimensão disponível para este poder.</p>
                      )}
                    </div>
                  )}
                </div>
              )}
            </div>
          )}

          <button
            onClick={handleBuscar}
            className="btn-primary w-full mt-4"
            disabled={isLoading || !esfera || !poder || !orgao}
          >
            {isLoading ? 'Iniciando Auditoria...' :
              dimensoesSelecionadas.length > 0 ?
                `🎯 Iniciar Auditoria Seletiva (${dimensoesSelecionadas.length} dimensões)` :
                '🔍 Iniciar Auditoria Completa'}
          </button>
        </div>

        {/* Mapa do órgão selecionado */}
        {(esfera || poder || orgao) && orgaosParaMapa.length > 0 && (
          <div className="card mb-8">
            <div className="flex flex-col lg:flex-row items-start gap-6">
              <div className="lg:w-1/3">
                <h3 className="text-xl font-bold text-blue-800 mb-2">
                  📍 {orgao ? 'Órgão Selecionado' : 'Órgãos Filtrados'}
                </h3>
                <div className="space-y-1 text-sm text-gray-600">
                  <p><span className="font-semibold">Esfera:</span> {esfera || 'Todas'}</p>
                  <p><span className="font-semibold">Poder:</span> {poder || 'Todos'}</p>
                  {orgao && <p><span className="font-semibold">Órgão:</span> {orgao}</p>}
                  <p><span className="font-semibold">Total encontrado:</span> {orgaosParaMapa.length} órgão(s)</p>
                </div>
              </div>
              <div className="lg:w-2/3 w-full">
                <div className="h-64 rounded-lg overflow-hidden">
                  <MapaOrgaos
                    orgaos={orgaosParaMapa}
                    selectedFilters={{
                      esfera: esfera,
                      poder: poder,
                      orgao: orgao
                    }}
                    className="h-full"
                  />
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Resultados da Auditoria */}
        {(resultados || isLoading || (statusMessage && !isLoading)) && (
          <div className="card">
            <h2 className="text-2xl font-bold text-blue-800 mb-4">
              Resultado da Auditoria
            </h2>
            <div className="mb-6 p-4 bg-gray-50 rounded-lg">
              <p className="mb-3">
                <span className="font-semibold">Esfera:</span> {esfera}<br />
                <span className="font-semibold">Poder:</span> {poder}<br />
                <span className="font-semibold">Órgão:</span> {orgao}
                {/* Mostrar informações do filtro */}
                {resultados?.filtro_aplicado && (
                  <>
                    <br />
                    <span className="font-semibold">Tipo de Auditoria:</span> {
                      resultados.filtro_aplicado.auditoria_completa ?
                        '🔍 Completa' :
                        `🎯 Seletiva (${resultados.filtro_aplicado.total_criterios_filtrados} critérios)`
                    }
                    {resultados.filtro_aplicado.dimensoes_selecionadas && (
                      <>
                        <br />
                        <span className="font-semibold">Dimensões:</span> {resultados.filtro_aplicado.dimensoes_selecionadas.join(', ')}
                      </>
                    )}
                  </>
                )}
              </p>
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
                                <button
                                  onClick={() => {
                                    window.open(item.link_evidencia, '_blank', 'noopener,noreferrer');
                                  }}
                                  className="text-blue-600 hover:text-blue-800 hover:underline cursor-pointer bg-transparent border-none p-0"
                                >
                                  🔗 Ver
                                </button>
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
                <div className="flex flex-col sm:flex-row gap-4 justify-between">
                  <button
                    onClick={() => {
                      setResultados(null);
                      setProgress(0);
                      setError(null);
                      setStatusMessage('');
                      setEsfera('');
                      setPoder('');
                      setOrgao('');
                      setDimensoesSelecionadas([]);
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
        )}
      </div>
    </div>
  );
};

export default AuditoriaPage;