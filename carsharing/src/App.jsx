import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./Login";         // Import Login page
import Signup from "./Signup";       // Import Signup page

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
