import { useCallback, useEffect, useState } from 'react';
import { readJSON, STORAGE_KEYS, writeJSON } from '../lib/storage';

/** Émis après chaque modification, pour synchroniser toutes les vues montées. */
const FAVORITES_UPDATED_EVENT = 'favoritesUpdated';

function readFavorites(): number[] {
  const value = readJSON<unknown>(STORAGE_KEYS.favorites, null);
  // Le stockage peut contenir n'importe quoi (version antérieure, édition
  // manuelle) : on ne garde que les identifiants numériques.
  if (!Array.isArray(value)) return [];
  return value.filter((id): id is number => typeof id === 'number' && Number.isFinite(id));
}

export function useFavorites() {
  const [favorites, setFavorites] = useState<number[]>(readFavorites);

  useEffect(() => {
    const sync = () => setFavorites(readFavorites());

    window.addEventListener(FAVORITES_UPDATED_EVENT, sync);
    // `storage` couvre les modifications faites dans un autre onglet.
    window.addEventListener('storage', sync);

    return () => {
      window.removeEventListener(FAVORITES_UPDATED_EVENT, sync);
      window.removeEventListener('storage', sync);
    };
  }, []);

  const toggleFavorite = useCallback((matchId: number) => {
    setFavorites((prev) => {
      const next = prev.includes(matchId)
        ? prev.filter((id) => id !== matchId)
        : [...prev, matchId];

      writeJSON(STORAGE_KEYS.favorites, next);
      window.dispatchEvent(new Event(FAVORITES_UPDATED_EVENT));
      return next;
    });
  }, []);

  const isFavorite = useCallback(
    (matchId: number) => favorites.includes(matchId),
    [favorites],
  );

  return { favorites, toggleFavorite, isFavorite };
}
