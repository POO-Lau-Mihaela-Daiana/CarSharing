import { Link } from "react-router-dom";
import "../styles.css"; // Import CSS

const Signup = () => {
  return (
    <div className="container">
      <h2>Sign Up</h2>
      <form>
        <input type="email" placeholder="Email" required />
        <input type="password" placeholder="Password" required />
        <button type="submit">Sign Up</button>
      </form>
      <p>Already have an account? <Link to="/">Login</Link></p>
    </div>
  );
};

export default Signup;
