import React, { useState } from 'react';
// Importa os dados do arquivo JSON da pasta data
import orgaosRanking2024 from '../data/orgaos_amazonas_ranking_2024.json';

// Interface para tipar os objetos do ranking
interface OrgaoRanking {
  nome: string;
  valor: number;
  municipio: string;
  poder: string;
  essenciais_final: number;
  nivel_final: string;
}

// Enum para os tipos de poder (facilita manutenção futura)
const PODER_LABELS: { [key: string]: string } = {
  'E': 'Executivo',
  'L': 'Legislativo',
  'J': 'Judiciário',
  'M': 'Ministério Público',
  'D': 'Defensoria',
  'T': 'Tribunal de Contas'
};

// Enum para ordenação dos níveis (do melhor para o pior)
const NIVEL_ORDER: { [key: string]: number } = {
  'Diamante': 1,
  'Ouro': 2,
  'Elevado': 3,
  'Intermediário': 4,
  'Básico': 5,
  'Inicial': 6,
  'Inexistente': 7
};

const RankingPage: React.FC = () => {
  const [sortBy, setSortBy] = useState<'valor' | 'essenciais' | 'nivel'>('valor');
  const [filterByPoder, setFilterByPoder] = useState<string>('todos');
  const [filterByMunicipio, setFilterByMunicipio] = useState<string>('todos');

  // Converte e ordena os dados
  const dadosDoRanking: OrgaoRanking[] = orgaosRanking2024;
  
  // Função para ordenar os dados
  const sortData = (data: OrgaoRanking[]): OrgaoRanking[] => {
    return [...data].sort((a, b) => {
      switch (sortBy) {
        case 'valor':
          return b.valor - a.valor;
        case 'essenciais':
          return b.essenciais_final - a.essenciais_final;
        case 'nivel':
          return NIVEL_ORDER[a.nivel_final] - NIVEL_ORDER[b.nivel_final];
        default:
          return 0;
      }
    });
  };

  // Função para filtrar os dados
  const filterData = (data: OrgaoRanking[]): OrgaoRanking[] => {
    return data.filter(item => {
      const poderMatch = filterByPoder === 'todos' || item.poder === filterByPoder;
      const municipioMatch = filterByMunicipio === 'todos' || item.municipio === filterByMunicipio;
      return poderMatch && municipioMatch;
    });
  };

  // Aplica filtros e ordenação
  const dadosFiltrados = sortData(filterData(dadosDoRanking));

  // Obtém listas únicas para os filtros
  const poderes = Array.from(new Set(dadosDoRanking.map(item => item.poder))).sort();
  const municipios = Array.from(new Set(dadosDoRanking.map(item => item.municipio))).sort();

  // Função para obter classes CSS baseadas no nível
  const getNivelClasses = (nivel: string): string => {
    switch (nivel) {
      case 'Diamante': 
        return 'bg-gradient-to-r from-cyan-50 to-teal-100 text-teal-800 font-bold border-l-4 border-teal-500';
      case 'Ouro': 
        return 'bg-gradient-to-r from-amber-50 to-yellow-100 text-amber-800 font-bold border-l-4 border-amber-500';
      case 'Elevado': 
        return 'bg-gradient-to-r from-green-50 to-emerald-100 text-green-800 font-semibold border-l-4 border-green-500';
      case 'Intermediário': 
        return 'bg-gradient-to-r from-blue-50 to-indigo-100 text-blue-800 border-l-4 border-blue-400';
      case 'Básico': 
        return 'bg-gradient-to-r from-orange-50 to-yellow-100 text-orange-700 border-l-4 border-orange-400';
      case 'Inicial': 
        return 'bg-gradient-to-r from-red-50 to-pink-100 text-red-700 border-l-4 border-red-400';
      case 'Inexistente': 
        return 'bg-gradient-to-r from-gray-100 to-slate-200 text-gray-600 border-l-4 border-gray-400';
      default: 
        return '';
    }
  };

  // Função para obter ícone do nível
  const getNivelIcon = (nivel: string): string => {
    switch (nivel) {
      case 'Diamante': return '💎';
      case 'Ouro': return '🏆';
      case 'Elevado': return '🥇';
      case 'Intermediário': return '🥈';
      case 'Básico': return '🥉';
      case 'Inicial': return '📊';
      case 'Inexistente': return '❌';
      default: return '';
    }
  };

  // Estatísticas resumidas
  const stats = {
    total: dadosDoRanking.length,
    diamante: dadosDoRanking.filter(item => item.nivel_final === 'Diamante').length,
    ouro: dadosDoRanking.filter(item => item.nivel_final === 'Ouro').length,
    mediaValor: (dadosDoRanking.reduce((acc, item) => acc + item.valor, 0) / dadosDoRanking.length).toFixed(2)
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="container mx-auto px-4">
        {/* Cabeçalho */}
        <div className="text-center mb-8">
          <h1 className="text-5xl font-bold bg-gradient-to-r from-blue-600 to-teal-600 bg-clip-text text-transparent mb-4">
            Ranking de Transparência
          </h1>
          <p className="text-xl text-gray-600 mb-2">
            Entidades Públicas do Amazonas - 2024
          </p>
          <div className="flex justify-center space-x-6 text-sm text-gray-500">
            <span>Total: <strong>{stats.total}</strong> entidades</span>
            <span>💎 Diamante: <strong>{stats.diamante}</strong></span>
            <span>🏆 Ouro: <strong>{stats.ouro}</strong></span>
            <span>Média Geral: <strong>{stats.mediaValor}%</strong></span>
          </div>
        </div>

        {/* Filtros e Ordenação */}
        <div className="bg-white rounded-lg shadow-md p-6 mb-6">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Ordenar por:
              </label>
              <select 
                value={sortBy} 
                onChange={(e) => setSortBy(e.target.value as 'valor' | 'essenciais' | 'nivel')}
                className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                <option value="valor">Valor Geral</option>
                <option value="essenciais">Essenciais Final</option>
                <option value="nivel">Nível Final</option>
              </select>
            </div>
            
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Filtrar por Poder:
              </label>
              <select 
                value={filterByPoder} 
                onChange={(e) => setFilterByPoder(e.target.value)}
                className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                <option value="todos">Todos os Poderes</option>
                {poderes.map(poder => (
                  <option key={poder} value={poder}>
                    {PODER_LABELS[poder] || poder}
                  </option>
                ))}
              </select>
            </div>
            
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Filtrar por Município:
              </label>
              <select 
                value={filterByMunicipio} 
                onChange={(e) => setFilterByMunicipio(e.target.value)}
                className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                <option value="todos">Todos os Municípios</option>
                {municipios.map(municipio => (
                  <option key={municipio} value={municipio}>
                    {municipio}
                  </option>
                ))}
              </select>
            </div>
          </div>
          
          {/* Contador de resultados filtrados */}
          <div className="mt-4 text-center text-sm text-gray-600">
            Exibindo <strong>{dadosFiltrados.length}</strong> de <strong>{dadosDoRanking.length}</strong> entidades
          </div>
        </div>

        {/* Tabela Principal */}
        <div className="bg-white rounded-lg shadow-lg overflow-hidden">
          <div className="overflow-x-auto">
            <table className="min-w-full">
              <thead className="bg-gradient-to-r from-blue-600 to-teal-600">
                <tr>
                  <th className="py-4 px-6 text-left text-sm font-semibold text-white uppercase tracking-wider">
                    #
                  </th>
                  <th className="py-4 px-6 text-left text-sm font-semibold text-white uppercase tracking-wider">
                    Entidade
                  </th>
                  <th className="py-4 px-6 text-center text-sm font-semibold text-white uppercase tracking-wider">
                    Município
                  </th>
                  <th className="py-4 px-6 text-center text-sm font-semibold text-white uppercase tracking-wider">
                    Poder
                  </th>
                  <th className="py-4 px-6 text-center text-sm font-semibold text-white uppercase tracking-wider">
                    Valor Geral (%)
                  </th>
                  <th className="py-4 px-6 text-center text-sm font-semibold text-white uppercase tracking-wider">
                    Essenciais (%)
                  </th>
                  <th className="py-4 px-6 text-center text-sm font-semibold text-white uppercase tracking-wider">
                    Nível Final
                  </th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-200">
                {dadosFiltrados.map((item, index) => (
                  <tr 
                    key={`${item.nome}-${item.municipio}`} 
                    className={`hover:bg-gray-50 transition-all duration-200 ${getNivelClasses(item.nivel_final)}`}
                  >
                    <td className="py-4 px-6 text-sm font-medium text-gray-900">
                      {index + 1}
                    </td>
                    <td className="py-4 px-6">
                      <div className="text-sm font-semibold text-gray-900">
                        {item.nome}
                      </div>
                    </td>
                    <td className="py-4 px-6 text-center text-sm text-gray-700">
                      {item.municipio}
                    </td>
                    <td className="py-4 px-6 text-center">
                      <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
                        {PODER_LABELS[item.poder] || item.poder}
                      </span>
                    </td>
                    <td className="py-4 px-6 text-center">
                      <span className="text-lg font-bold text-gray-900">
                        {item.valor.toFixed(2)}%
                      </span>
                    </td>
                    <td className="py-4 px-6 text-center">
                      <span className="text-sm font-semibold text-gray-700">
                        {item.essenciais_final.toFixed(2)}%
                      </span>
                    </td>
                    <td className="py-4 px-6 text-center">
                      <div className="flex items-center justify-center space-x-2">
                        <span className="text-lg">{getNivelIcon(item.nivel_final)}</span>
                        <span className="text-sm font-semibold">
                          {item.nivel_final}
                        </span>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        {/* Rodapé com informações adicionais */}
        <div className="mt-8 text-center text-sm text-gray-500">
          <p>
            Dados referentes ao ano de 2024 • 
            Última atualização: {new Date().toLocaleDateString('pt-BR')} • 
            Sistema de Avaliação de Transparência Pública
          </p>
        </div>
      </div>
    </div>
  );
};

export default RankingPage;