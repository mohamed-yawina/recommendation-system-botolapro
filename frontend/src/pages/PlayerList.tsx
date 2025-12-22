import React, { useEffect, useState } from 'react';
import { playerService } from '../services/api';
import { Plus, Trash2, Search } from 'lucide-react';

const PlayerList = () => {
  const [players, setPlayers] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    loadPlayers();
  }, []);

  const loadPlayers = async () => {
    try {
      const data = await playerService.getAll();
      setPlayers(data);
    } catch (error) {
      console.error('Error loading players', error);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id: string) => {
    if (window.confirm('Êtes-vous sûr de vouloir supprimer ce joueur ?')) {
      try {
        await playerService.delete(id);
        setPlayers(players.filter(p => p.uid !== id));
      } catch (error) {
        console.error('Error deleting player', error);
      }
    }
  };

  const filteredPlayers = players.filter(p => 
    p.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    p.position.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h2 className="text-2xl font-bold font-display text-gray-800">Gestion de l'effectif</h2>
          <p className="text-gray-500">Gérez les joueurs et leurs contrats</p>
        </div>
        <button className="bg-botola-green text-white px-4 py-2 rounded-lg flex items-center gap-2 hover:bg-green-800 transition-colors">
          <Plus size={20} />
          Ajouter un joueur
        </button>
      </div>

      <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
        <div className="p-4 border-b border-gray-100">
          <div className="relative">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" size={20} />
            <input
              type="text"
              placeholder="Rechercher un joueur..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-10 pr-4 py-2 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-botola-green/50"
            />
          </div>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-sm text-left">
            <thead className="text-xs text-gray-700 uppercase bg-gray-50">
              <tr>
                <th className="px-6 py-3">Nom</th>
                <th className="px-6 py-3">Âge</th>
                <th className="px-6 py-3">Poste</th>
                <th className="px-6 py-3">Nationalité</th>
                <th className="px-6 py-3">Fin Contrat</th>
                <th className="px-6 py-3 text-right">Actions</th>
              </tr>
            </thead>
            <tbody>
              {filteredPlayers.length > 0 ? filteredPlayers.map((player) => (
                <tr key={player.uid} className="bg-white border-b hover:bg-gray-50">
                  <td className="px-6 py-4 font-medium text-gray-900">
                    {player.name}
                  </td>
                  <td className="px-6 py-4">{player.age}</td>
                  <td className="px-6 py-4">
                    <span className="bg-gray-100 text-gray-800 text-xs font-medium px-2.5 py-0.5 rounded">
                      {player.position}
                    </span>
                  </td>
                  <td className="px-6 py-4">{player.nationality}</td>
                  <td className="px-6 py-4">{player.contract_end}</td>
                  <td className="px-6 py-4 text-right">
                    <button 
                      onClick={() => handleDelete(player.uid)}
                      className="text-red-500 hover:text-red-700 p-1 hover:bg-red-50 rounded"
                    >
                      <Trash2 size={18} />
                    </button>
                  </td>
                </tr>
              )) : (
                <tr>
                  <td colSpan={6} className="px-6 py-8 text-center text-gray-500">
                    Aucun joueur trouvé.
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

export default PlayerList;
