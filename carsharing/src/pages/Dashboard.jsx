import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios"; // Axios to make API requests

const Dashboard = () => {
  const [user, setUser] = useState(null); // Store user info (e.g., name, email)
  const [availableCars, setAvailableCars] = useState([]); // Store available cars
  const [currentRentals, setCurrentRentals] = useState([]); // Store current rentals

  useEffect(() => {
    // Fetch the client info (you can adjust the API endpoint)
    const fetchUserData = async () => {
      const response = await axios.get("http://localhost:8000/user/me", {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`, // Assume JWT is stored in localStorage
        },
      });
      setUser(response.data);
    };

    // Fetch the available cars (replace with your own API)
    const fetchAvailableCars = async () => {
      const response = await axios.get("http://localhost:8000/cars/available");
      setAvailableCars(response.data);
    };

    // Fetch current rentals (you can adjust the API)
    const fetchCurrentRentals = async () => {
      const response = await axios.get("http://localhost:8000/user/rentals", {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      });
      setCurrentRentals(response.data);
    };

    fetchUserData();
    fetchAvailableCars();
    fetchCurrentRentals();
  }, []);

  return (
    <div className="dashboard-container">
      {user ? (
        <div>
          <h2>Welcome, {user.name}!</h2>
          <p>Email: {user.email}</p>
          <p>Phone Number: {user.phoneNumber}</p>
          
          <div className="available-cars">
            <h3>Available Cars</h3>
            <ul>
              {availableCars.map((car) => (
                <li key={car.carID}>
                  <p>{car.model}</p>
                  <p>{car.location}</p>
                  <p>Status: {car.status}</p>
                  {car.status === "available" && (
                    <button
                      onClick={() => {
                        // Here you would send a request to rent the car
                        alert(`You are renting ${car.model}`);
                      }}
                    >
                      Rent this car
                    </button>
                  )}
                </li>
              ))}
            </ul>
          </div>

          <div className="current-rentals">
            <h3>Your Current Rentals</h3>
            <ul>
              {currentRentals.length === 0 ? (
                <p>You have no active rentals.</p>
              ) : (
                currentRentals.map((rental) => (
                  <li key={rental.rentalID}>
                    <p>Car: {rental.car.model}</p>
                    <p>Start Date: {rental.rental_start}</p>
                    <p>Status: {rental.rental_end ? "Returned" : "Active"}</p>
                  </li>
                ))
              )}
            </ul>
          </div>

          <Link to="/profile">
            <button>Go to Profile</button>
          </Link>
          <Link to="/logout">
            <button>Logout</button>
          </Link>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default Dashboard;
