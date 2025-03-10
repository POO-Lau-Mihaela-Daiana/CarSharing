import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

const Dashboard = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      navigate("/"); // Redirect to login if no token is found
    }
  }, [navigate]);

  return (
    <div className="container">
      <h1>CarSharing Dashboard</h1>
      <p>Welcome! You have successfully logged in.</p>
      <button onClick={() => {
        localStorage.removeItem("token");
        navigate("/");
      }}>
        Logout
      </button>
    </div>
  );
};

export default Dashboard;
