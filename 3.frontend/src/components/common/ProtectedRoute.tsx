import { Navigate, Outlet } from 'react-router-dom';
import { useAuthStore } from '../../store/authStore';

const ProtectedRoute = () => {
  // Get the access token from our global Zustand store
  const { accessToken } = useAuthStore((state) => state);

  // Check if the user is authenticated
  if (!accessToken) {
    // If not authenticated, redirect them to the login page
    // The 'replace' prop is important to prevent the user from
    // hitting the "back" button and getting stuck in a redirect loop.
    return <Navigate to="/login" replace />;
  }

  // If they are authenticated, render the child route content.
  // The <Outlet /> component is a placeholder provided by React Router
  // that will render the actual page component (e.g., FeedPage).
  return <Outlet />;
};

export default ProtectedRoute;