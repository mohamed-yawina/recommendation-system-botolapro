import React, { useEffect, useState } from 'react';
import { playerService } from '../services/api';
import { AlertTriangle, Users, TrendingUp } from 'lucide-react';
import { Link } from 'react-router-dom';

const StatCard = ({ title, value, icon: Icon, color }: any) => (
  <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex items-center space-x-4">
    <div className={`p-3 rounded-lg ${color}`}>
      <Icon className="text-white" size={24} />
    </div>
    <div>
      <p className="text-gray-500 text-sm">{title}</p>
      <h3 className="text-2xl font-bold font-display">{value}</h3>
    </div>
  </div>
);

const Dashboard = () => {
  const [players, setPlayers] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      const data = await playerService.getAll();
      setPlayers(data);
    } catch (error) {
      console.error('Error loading data', error);
    } finally {
      setLoading(false);
    }
  };

  const expiringPlayers = players.filter(p => {
    const end = new Date(p.contract_end);
    const now = new Date();
    const diffTime = Math.abs(end.getTime() - now.getTime());
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)); 
    return diffDays < 90; // Less than 3 months approx
  });

  return (
    <div className="space-y-8">
      <div>
        <h2 className="text-2xl font-bold font-display text-gray-800">Tableau de bord</h2>
        <p className="text-gray-500">Vue d'ensemble de l'effectif</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <StatCard 
          title="Effectif Total" 
          value={players.length} 
          icon={Users} 
          color="bg-blue-500" 
        />
        <StatCard 
          title="Fins de contrat" 
          value={expiringPlayers.length} 
          icon={AlertTriangle} 
          color="bg-red-500" 
        />
        <StatCard 
          title="Recommandations" 
          value={expiringPlayers.length * 5} // Mock metric
          icon={TrendingUp} 
          color="bg-botola-orange" 
        />
      </div>

      <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
        <div className="p-6 border-b border-gray-100 flex justify-between items-center">
          <h3 className="font-bold text-gray-800 flex items-center gap-2">
            <AlertTriangle size={20} className="text-red-500" />
            Alertes Contrats
          </h3>
          <span className="text-xs font-medium px-2.5 py-0.5 rounded bg-red-100 text-red-800">
            Urgent
          </span>
        </div>
        
        <div className="overflow-x-auto">
          <table className="w-full text-sm text-left">
            <thead className="text-xs text-gray-700 uppercase bg-gray-50">
              <tr>
                <th className="px-6 py-3">Joueur</th>
                <th className="px-6 py-3">Poste</th>
                <th className="px-6 py-3">Fin Contrat</th>
                <th className="px-6 py-3">Action</th>
              </tr>
            </thead>
            <tbody>
              {expiringPlayers.length > 0 ? expiringPlayers.map((player) => (
                <tr key={player.uid} className="bg-white border-b hover:bg-gray-50">
                  <td className="px-6 py-4 font-medium text-gray-900">
                    {player.name}
                  </td>
                  <td className="px-6 py-4">{player.position}</td>
                  <td className="px-6 py-4 text-red-600 font-medium">
                    {player.contract_end}
                  </td>
                  <td className="px-6 py-4">
                    <Link 
                      to={`/recommendations/${player.uid}`}
                      className="text-botola-green hover:underline font-medium"
                    >
                      Voir recommandations
                    </Link>
                  </td>
                </tr>
              )) : (
                <tr>
                  <td colSpan={4} className="px-6 py-8 text-center text-gray-500">
                    Aucune alerte de contrat pour le moment.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
