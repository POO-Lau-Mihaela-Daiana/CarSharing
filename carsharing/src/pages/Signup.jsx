import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "../styles.css";

const Signup = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [phoneNumber, setPhoneNumber] = useState("");
  const [location, setLocation] = useState("");
  const [paymentMethod, setPaymentMethod] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSignup = async (e) => {
    e.preventDefault();
    setError("");
  
    try {
      const response = await fetch("http://127.0.0.1:8000/register", {
        method: "POST", 
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, phoneNumber, location, paymentMethod, password }),
      });
  
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail);
  
      navigate("/"); // Redirect to login page
    } catch (err) {
      setError(err.message);
    }
  };
  
  return (
    <div className="container">
      <h2>Sign Up</h2>
      {error && <p className="error">{error}</p>}
      <form onSubmit={handleSignup}>
        <input type="text" placeholder="Full Name" value={name} onChange={(e) => setName(e.target.value)} required />
        <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required />
        <input type="text" placeholder="Phone Number" value={phoneNumber} onChange={(e) => setPhoneNumber(e.target.value)} required />
        <input type="text" placeholder="Location" value={location} onChange={(e) => setLocation(e.target.value)} required />
        <input type="text" placeholder="Payment Method" value={paymentMethod} onChange={(e) => setPaymentMethod(e.target.value)} required />
        <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} required />
        <button type="submit">Sign Up</button>
      </form>
      <p>Already have an account? <Link to="/">Login</Link></p>
    </div>
  );
};

export default Signup;
