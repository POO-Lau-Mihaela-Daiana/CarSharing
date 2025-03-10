import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./pages/Login.jsx";         // Import Login page
import Signup from "./pages/Signup.jsx";       // Import Signup page

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
       
      </Routes>
    </Router>
  );
}

export default App;
