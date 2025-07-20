import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import ProtectedRoute from './components/common/ProtectedRoute'; // <-- IMPORT IT

// Placeholder for the main feed page
const FeedPage = () => (
    <div>
        <h1>Welcome to Event Horizon</h1>
        <p>This is the main feed. You are logged in.</p>
        {/* We'll add a logout button here later */}
    </div>
);

// We can also protect other pages in the future
const CalendarPage = () => <div>Calendar Page (Protected)</div>;
const ChatPage = () => <div>Chat Page (Protected)</div>;

function App() {
  return (
      // Add a dark background, primary text color, and some padding
    <div className="bg-primary text-text-primary min-h-screen p-4">
      <Router>
        {/* Simple navigation for testing */}
        <nav>
          {/* Add the accent color to links */}
          <Link to="/" className="text-accent hover:text-accent-hover">Home</Link> | 
          <Link to="/login" className="text-accent hover:text-accent-hover">Login</Link> | 
          <Link to="/register" className="text-accent hover:text-accent-hover">Register</Link>
        </nav>
        <hr className="my-4 border-secondary" />

        <Routes>
          {/* Public Routes */}
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
          
          {/* --- Protected Routes --- */}
          {/* We wrap our protected routes inside a parent Route element that uses our ProtectedRoute component */}
          <Route element={<ProtectedRoute />}>
            <Route path="/" element={<FeedPage />} />
            <Route path="/calendar" element={<CalendarPage />} />
            <Route path="/chat" element={<ChatPage />} />
            {/* Add any other protected routes here */}
          </Route>
        </Routes>
      </Router>
    </div>
  );
}

export default App;