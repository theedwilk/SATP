import React, { useState } from 'react';
import { FaBars } from 'react-icons/fa';

// Define os tipos de visualização que o App pode ter
type CurrentView = 'mapa' | 'ranking' | 'auditoria';

interface SidebarProps {
  setCurrentView: (view: CurrentView) => void;
  currentView: CurrentView;
}

const Sidebar: React.FC<SidebarProps> = ({ setCurrentView, currentView }) => {
  // Estado para controlar se o sidebar está colapsado ou não
  const [isCollapsed, setIsCollapsed] = useState(false);

  // Função para alternar o estado de colapso
  const toggleCollapse = () => {
    setIsCollapsed(!isCollapsed);
  };

  // Função auxiliar para aplicar classes CSS com base na visualização ativa
  const navItemClass = (viewName: CurrentView) =>
    `flex items-center w-full px-4 py-3 rounded-lg transition-colors duration-200 ${
      currentView === viewName ? 'bg-blue-700 text-white' : 'text-blue-100 hover:bg-blue-600'
    } ${isCollapsed ? 'justify-center' : ''}`;

  return (
    <aside
      className={`bg-blue-800 text-white flex flex-col p-4 shadow-lg transition-all duration-300 ${
        isCollapsed ? 'w-20' : 'w-64'
      }`}
    >
      <div className="flex items-center justify-between mb-8">
        {!isCollapsed && <div className="text-2xl font-bold">SAPT</div>}
        <button onClick={toggleCollapse} className="text-white p-2 rounded-full hover:bg-blue-600">
          {/* @ts-ignore */}
          <FaBars size={20} />
        </button>
      </div>

      <nav className="flex-1 space-y-2">
        <button onClick={() => setCurrentView('mapa')} className={navItemClass('mapa')}>
          🗺️ {!isCollapsed && <span className="ml-3">Mapa</span>}
        </button>
        <button onClick={() => setCurrentView('ranking')} className={navItemClass('ranking')}>
          🏆 {!isCollapsed && <span className="ml-3">Ranking</span>}
        </button>
        <button onClick={() => setCurrentView('auditoria')} className={navItemClass('auditoria')}>
          📝 {!isCollapsed && <span className="ml-3">Avaliação</span>}
        </button>
      </nav>

      {/* Novo Footer Compacto */}
      <footer className={`mt-8 py-4 ${isCollapsed ? 'hidden' : ''}`}>
        <div className="text-center px-2">
          <a
            href="https://github.com/theedwilk/SATP"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center space-x-2 px-3 py-1.5 bg-gray-900 text-white rounded-md hover:bg-gray-700 transition-colors duration-200 text-sm"
          >
            <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
              <path fillRule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clipRule="evenodd" />
            </svg>
            <span>Ajude-nos a melhorar</span>
          </a>
          <p className="text-xs text-blue-100 mt-2">
            Desenvolvido pela equipe <span className="font-medium">DICETI TCE AM</span>
            <br />
            Contribuições são bem-vindas!
          </p>
        </div>
      </footer>

      <div className={`mt-auto text-center text-sm text-blue-200 ${isCollapsed ? 'hidden' : ''}`}>
        &copy; 2025 SAPT
      </div>
    </aside>
  );
};

export default Sidebar;