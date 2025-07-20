import { create } from 'zustand';
import { persist } from 'zustand/middleware';

// Define the shape of our user object for the frontend
interface User {
  id: number;
  username: string;
  email: string;
}

// Define the shape of the entire auth store's state
interface AuthState {
  accessToken: string | null;
  refreshToken: string | null;
  user: User | null;
  setTokens: (tokens: { accessToken: string; refreshToken: string }) => void;
  setUser: (user: User) => void;
  logout: () => void;
}

// Create the Zustand store
export const useAuthStore = create<AuthState>()(
  // The 'persist' middleware automatically saves the store's state
  // to localStorage, so it survives page refreshes.
  persist(
    (set) => ({
      accessToken: null,
      refreshToken: null,
      user: null,
      setTokens: ({ accessToken, refreshToken }) =>
        set({ accessToken, refreshToken }),
      setUser: (user) => set({ user }),
      logout: () => set({ accessToken: null, refreshToken: null, user: null }),
    }),
    {
      name: 'auth-storage', // The key to use in localStorage
    }
  )
);