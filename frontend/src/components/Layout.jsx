import React from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import { logout } from './Logout';

const Layout = ({ children }) => {
  const navigate = useNavigate();

  // Check if the current path is not '/'
  const shouldShowNav = window.location.pathname !== '/';

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
              <NavLink
                to="/products"
                className={({ isActive }) => (isActive ? 'active' : '')} // Use `className` with a function
              >
                Products
              </NavLink>
            </li>
            <li>
              <NavLink
                to="/orders"
                className={({ isActive }) => (isActive ? 'active' : '')} // Use `className` with a function
              >
                Orders
              </NavLink>
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
