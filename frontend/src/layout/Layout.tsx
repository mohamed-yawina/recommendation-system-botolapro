import React from 'react';
import { Outlet, Link, useNavigate, useLocation } from 'react-router-dom';
import { LayoutDashboard, Users, UserPlus, Network, LogOut } from 'lucide-react';
import { authService } from '../services/api';

const SidebarItem = ({ icon: Icon, label, to, active }: any) => (
  <Link
    to={to}
    className={`flex items-center space-x-3 px-4 py-3 rounded-lg transition-colors ${
      active 
        ? 'bg-botola-orange text-white' 
        : 'text-gray-300 hover:bg-botola-green/50 hover:text-white'
    }`}
  >
    <Icon size={20} />
    <span className="font-medium">{label}</span>
  </Link>
);

const Layout = () => {
  const navigate = useNavigate();
  const location = useLocation();

  const handleLogout = () => {
    authService.logout();
    navigate('/login');
  };

  return (
    <div className="flex h-screen bg-gray-50">
      {/* Sidebar */}
      <aside className="w-64 bg-botola-green text-white shadow-xl flex flex-col">
        <div className="p-6 border-b border-botola-green/50">
          <h1 className="text-2xl font-display font-bold text-white flex items-center gap-2">
            ⚽ Scouting<span className="text-botola-orange">Pro</span>
          </h1>
          <p className="text-xs text-gray-300 mt-1">Botola Pro Assistant</p>
        </div>

        <nav className="flex-1 p-4 space-y-2">
          <SidebarItem 
            icon={LayoutDashboard} 
            label="Dashboard" 
            to="/" 
            active={location.pathname === '/'} 
          />
          <SidebarItem 
            icon={Users} 
            label="Joueurs" 
            to="/players" 
            active={location.pathname === '/players'} 
          />
          <SidebarItem 
            icon={Network} 
            label="Visualisation" 
            to="/visualization" 
            active={location.pathname === '/visualization'} 
          />
        </nav>

        <div className="p-4 border-t border-botola-green/50">
          <button
            onClick={handleLogout}
            className="flex items-center space-x-3 px-4 py-3 w-full text-left text-gray-300 hover:bg-red-600/20 hover:text-red-400 rounded-lg transition-colors"
          >
            <LogOut size={20} />
            <span className="font-medium">Déconnexion</span>
          </button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto">
        <div className="p-8">
          <Outlet />
        </div>
      </main>
    </div>
  );
};

export default Layout;
