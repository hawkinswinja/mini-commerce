import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/Layout';
import LoginPage from './pages/LoginPage';
import OrdersPage from './pages/OrdersPage';
import ProductsPage from './pages/ProductsPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/products" element={<Layout><ProductsPage /></Layout>} />
        <Route path="/orders" element={<Layout><OrdersPage /></Layout>} />
      </Routes>
    </Router>
  );
}

export default App;
