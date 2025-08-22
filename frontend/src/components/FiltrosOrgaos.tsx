// Conteúdo do arquivo: src/components/FiltrosOrgaos.tsx

import React from 'react';
import { FiltrosOrgaos as FiltrosType } from '../types/orgaos'; // EstatisticasMapa removido daqui

interface FiltrosOrgaosProps {
  filters: FiltrosType;
  onFilterChange: (filterName: keyof FiltrosType, value: string | number | undefined) => void;
  opcoesEsfera: string[];
  opcoesPoder: string[];
  opcoesOrgao: string[];
  isLoading: boolean;
  onResetFilters: () => void;
}

const FiltrosOrgaos: React.FC<FiltrosOrgaosProps> = ({
  filters,
  onFilterChange,
  opcoesEsfera,
  opcoesPoder,
  opcoesOrgao,
  isLoading,
  onResetFilters,
}) => {
  return (
    <div className="bg-white p-6 rounded-lg shadow-md mb-6">
      <h2 className="text-xl font-bold text-blue-800 mb-4">
        Filtrar Órgãos
      </h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-4">
        <div>
          <label htmlFor="esfera" className="block text-sm font-medium text-gray-700 mb-1">
            Esfera
          </label>
          <select
            id="esfera"
            value={filters.esfera || ''}
            onChange={(e) => onFilterChange('esfera', e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            disabled={isLoading}
          >
            <option value="">Todas</option>
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
            value={filters.poder || ''}
            onChange={(e) => onFilterChange('poder', e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            disabled={isLoading || !filters.esfera}
          >
            <option value="">Todos</option>
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
            value={filters.orgao || ''}
            onChange={(e) => onFilterChange('orgao', e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            disabled={isLoading || !filters.poder}
          >
            <option value="">Todos</option>
            {opcoesOrgao.map((opt) => (
              <option key={opt} value={opt}>
                {opt}
              </option>
            ))}
          </select>
        </div>
        <div>
          <label htmlFor="municipio" className="block text-sm font-medium text-gray-700 mb-1">
            Município
          </label>
          <input
            type="text"
            id="municipio"
            value={filters.municipio || ''}
            onChange={(e) => onFilterChange('municipio', e.target.value)}
            placeholder="Ex: Manaus"
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            disabled={isLoading}
          />
        </div>
        <div>
          <label htmlFor="raio_km" className="block text-sm font-medium text-gray-700 mb-1">
            Raio (km)
          </label>
          <input
            type="number"
            id="raio_km"
            value={filters.raio_km || ''}
            placeholder="Ex: 100"
            onChange={(e) => {
              const value = e.target.value ? Number(e.target.value) : undefined;
              onFilterChange('raio_km', value);
            }}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            disabled={isLoading}
          />
        </div>
      </div>
      <button
        onClick={onResetFilters}
        className="mt-4 px-4 py-2 bg-gray-200 text-gray-800 rounded-md hover:bg-gray-300 transition-colors"
        disabled={isLoading}
      >
        Limpar Filtros
      </button>
    </div>
  );
};

export default FiltrosOrgaos;
