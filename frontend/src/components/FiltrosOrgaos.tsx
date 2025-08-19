import React from 'react';
import { FiltrosOrgaos as FiltrosType, EstatisticasMapa } from '../types/orgaos';

interface FiltrosOrgaosProps {
  filters: FiltrosType;
  onFilterChange: (key: keyof FiltrosType, value: string | number | undefined) => void;
  estatisticas?: EstatisticasMapa | null;
  className?: string;
}

const FiltrosOrgaos: React.FC<FiltrosOrgaosProps> = ({ 
  filters, 
  onFilterChange, 
  estatisticas,
  className = ''
}) => {
  return (
    <div className={`bg-white rounded-lg shadow-lg p-6 ${className}`}>
      <h3 className="text-lg font-semibold text-gray-800 mb-4">Filtros</h3>
      
      <div className="space-y-4">
        {/* Filtro por Esfera */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Esfera:
          </label>
          <select
            value={filters.esfera || ''}
            onChange={(e) => onFilterChange('esfera', e.target.value || undefined)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          >
            <option value="">Todas</option>
            <option value="Estadual">Estadual</option>
            <option value="Municipal">Municipal</option>
          </select>
        </div>

        {/* Filtro por Poder */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Poder:
          </label>
          <select
            value={filters.poder || ''}
            onChange={(e) => onFilterChange('poder', e.target.value || undefined)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          >
            <option value="">Todos</option>
            <option value="Poder Executivo">Poder Executivo</option>
            <option value="Poder Legislativo">Poder Legislativo</option>
            <option value="Poder Judiciário">Poder Judiciário</option>
            <option value="Tribunal de Contas">Tribunal de Contas</option>
            <option value="Ministério Público">Ministério Público</option>
            <option value="Defensoria">Defensoria</option>
          </select>
        </div>

        {/* Filtro por Raio */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Raio de Manaus (km):
          </label>
          <input
            type="number"
            value={filters.raio_km || ''}
            placeholder="Ex: 100"
            onChange={(e) => {
              const value = e.target.value ? Number(e.target.value) : undefined;
              onFilterChange('raio_km', value);
            }}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
        </div>
      </div>

      {/* Estatísticas */}
      {estatisticas && (
        <div className="mt-6 pt-4 border-t border-gray-200">
          <h4 className="text-sm font-medium text-gray-700 mb-2">Estatísticas</h4>
          <div className="space-y-1 text-xs text-gray-600">
            <div className="flex justify-between">
              <span>Total:</span>
              <span className="font-medium">{estatisticas.total_orgaos} órgãos</span>
            </div>
            <div className="flex justify-between">
              <span>Distância média:</span>
              <span className="font-medium">{estatisticas.distancia_media_manaus} km</span>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default FiltrosOrgaos;
