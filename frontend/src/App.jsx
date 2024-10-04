import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import PrivateRoute from './components/PrivateRoute';
import LoginPage from './pages/LoginPage';
import OrdersPage from './pages/OrdersPage';
import ProductsPage from './pages/ProductsPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/products"  element={<PrivateRoute element={<Layout><ProductsPage /></Layout>} />} />
        <Route path="/orders"  element={<PrivateRoute element={<Layout><OrdersPage /></Layout>} />} />
      </Routes>
    </Router>
  );
}

export default App;
