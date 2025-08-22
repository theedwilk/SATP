// Conteúdo do arquivo: src/components/Sidebar.tsx

import React from 'react';

// Define os tipos de visualização que o App pode ter
type CurrentView = 'mapa' | 'ranking' | 'auditoria';

interface SidebarProps {
  setCurrentView: (view: CurrentView) => void; // Função para mudar a visualização
  currentView: CurrentView; // A visualização atualmente ativa
}

const Sidebar: React.FC<SidebarProps> = ({ setCurrentView, currentView }) => {
  // Função auxiliar para aplicar classes CSS com base na visualização ativa
  const navItemClass = (viewName: CurrentView) =>
    `flex items-center p-3 rounded-lg transition-colors duration-200 ${
      currentView === viewName ? 'bg-blue-700 text-white' : 'text-blue-100 hover:bg-blue-600'
    }`;

  return (
    <aside className="w-64 bg-blue-800 text-white flex flex-col p-4 shadow-lg">
      <div className="text-2xl font-bold mb-8 text-center">SAPT</div>
      <nav className="flex-1 space-y-2">
        <button onClick={() => setCurrentView('mapa')} className={navItemClass('mapa')}>
          🗺️ Mapa
        </button>
        <button onClick={() => setCurrentView('ranking')} className={navItemClass('ranking')}>
          🏆 Ranking
        </button>
        <button onClick={() => setCurrentView('auditoria')} className={navItemClass('auditoria')}>
          📝 Avaliação
        </button>
      </nav>
      <div className="mt-auto text-center text-sm text-blue-200">
        &copy; 2025 SAPT
      </div>
    </aside>
  );
};

export default Sidebar;
