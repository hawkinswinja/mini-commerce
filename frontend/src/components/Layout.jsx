import React from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import { logout } from './Logout'; // Import the logout function

const Layout = ({ children }) => {
  const navigate = useNavigate();

  // Check if the current path is not '/login'
  const shouldShowNav = window.location.pathname !== '/login';

  // Handle Logout click
  const handleLogoutClick = (e) => {
    e.preventDefault(); // Prevent default link behavior
    logout(navigate);   // Call the logout function with navigate
  };

  return (
    <div>
      {shouldShowNav && (
        <nav className="navbar">
          <ul>
            <li>
              <NavLink to="/products" activeClassName="active">Products</NavLink>
            </li>
            <li>
              <NavLink to="/orders" activeClassName="active">Orders</NavLink>
            </li>
            <li>
              <a href="/logout" onClick={handleLogoutClick}>Logout</a>
            </li>
          </ul>
        </nav>
      )}

      {/* Render the rest of the page content */}
      {children}
    </div>
  );
};

export default Layout;
