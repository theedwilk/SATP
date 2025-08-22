// Conteúdo do arquivo: src/components/AuditoriaPage.tsx

import React, { useState, useEffect } from 'react';
import ApiService, { AuditoriaResponse, OrgaosData } from '../services/api'; // OrgaosData importado daqui
// MapaOrgaos NÃO é mais usado aqui, pois o mapa foi movido para HomePage

// A interface OrgaosData foi movida para src/services/api.ts

const AuditoriaPage: React.FC = () => {
  // Estados principais para os filtros
  const [esfera, setEsfera] = useState('');
  const [poder, setPoder] = useState('');
  const [orgao, setOrgao] = useState('');

  // Dados e loading
  const [orgaosData, setOrgaosData] = useState<OrgaosData>({}); // Dados para os dropdowns
  const [orgaosLoading, setOrgaosLoading] = useState(true); // Loading dos dados dos dropdowns
  const [isLoading, setIsLoading] = useState(false); // Loading da auditoria
  const [resultados, setResultados] = useState<AuditoriaResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [progress, setProgress] = useState(0);
  const [statusMessage, setStatusMessage] = useState('');

  // Carregar dados dos órgãos para os dropdowns na inicialização
  useEffect(() => {
    const carregarOrgaos = async () => {
      try {
        setOrgaosLoading(true);
        const data = await ApiService.obterOrgaos();
        setOrgaosData(data);
        setError(null);
      } catch (err: any) {
        setError(err.message);
        console.error('Erro ao carregar órgãos:', err);
      } finally {
        setOrgaosLoading(false);
      }
    };
    carregarOrgaos();
  }, []);

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

  const handleBuscar = async () => {
    if (!esfera || !poder || !orgao) {
      setError('Por favor, selecione Esfera, Poder e Órgão.');
      return;
    }

    setIsLoading(true);
    setResultados(null);
    setError(null);
    setProgress(0);
    setStatusMessage('Iniciando auditoria...');

    try {
      const orgaoSelecionado = orgaosData[esfera][poder][orgao];
      const siteUrl = orgaoSelecionado.site;
      const transparenciaUrl = orgaoSelecionado.transparencia;

      if (!siteUrl && !transparenciaUrl) {
        throw new Error('URL do site ou transparência não disponível para o órgão selecionado.');
      }

      // Simulação de progresso e chamada da API
      const totalSteps = 100;
      for (let i = 0; i <= totalSteps; i += 10) {
        await new Promise(resolve => setTimeout(resolve, 100)); // Pequeno delay
        setProgress(i);
        if (i < 30) {
          setStatusMessage('Coletando informações iniciais...');
        } else if (i < 60) {
          setStatusMessage('Analisando dados de transparência...');
        } else if (i < 90) {
          setStatusMessage('Verificando conformidade com critérios...');
        } else {
          setStatusMessage('Finalizando auditoria...');
        }
        if (!isLoading) break; // Permite cancelar a simulação
      }

      if (isLoading) { // Se não foi cancelado
        const response = await ApiService.realizarAuditoria(siteUrl, transparenciaUrl);
        setResultados(response);
        setStatusMessage('Auditoria concluída com sucesso!');
      }

    } catch (err: any) {
      setError(`Erro durante a auditoria: ${err.message}`);
      setStatusMessage(`Erro: ${err.message}`);
      console.error('Erro na auditoria:', err);
    } finally {
      setIsLoading(false);
      setProgress(100); // Garante que o progresso chegue a 100% no final
    }
  };

  return (
    <div className="flex flex-col h-full bg-gray-100">
      <header className="bg-white shadow-md p-6">
        <h1 className="text-3xl font-bold text-blue-800 text-center">
          Avaliação de Transparência e Conformidade
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
          ) : error && !orgaosData ? ( // Mostra erro apenas se não carregou os dados iniciais
            <p className="text-red-600">Erro ao carregar opções: {error}</p>
          ) : (
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
          )}
          <button
            onClick={handleBuscar}
            className="btn-primary w-full"
            disabled={isLoading || !esfera || !poder || !orgao}
          >
            {isLoading ? 'Iniciando Auditoria...' : 'Iniciar Auditoria'}
          </button>
        </div>

        {/* Resultados da Auditoria (mantido como estava) */}
        {resultados && (
          <div className="card">
            <h2 className="text-2xl font-bold text-blue-800 mb-4">
              Resultado da Auditoria
            </h2>
            <div className="mb-6 p-4 bg-gray-50 rounded-lg">
              <p className="mb-3">
                <span className="font-semibold">Esfera:</span> {esfera}<br />
                <span className="font-semibold">Poder:</span> {poder}<br />
                <span className="font-semibold">Órgão:</span> {orgao}
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
              <div className="flex flex-col sm:flex-row gap-4 justify-between">
                <button
                  onClick={() => {
                    setResultados(null);
                    setProgress(0);
                    setError(null);
                    // Opcionalmente, resetar filtros aqui
                    setEsfera('');
                    setPoder('');
                    setOrgao('');
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
          </div>
        )}
      </div>
      {/* Assuming you have a Footer component */}
      {/* <Footer /> */}
    </div>
  );
};

export default AuditoriaPage;
