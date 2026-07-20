import { BrowserRouter, Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";

import Dashboard from "./pages/Dashboard";
import Products from "./pages/Products";
import Suppliers from "./pages/Suppliers";
import Analytics from "./pages/Analytics";
import InventoryLogs from "./pages/InventoryLogs";

function App() {
  return (
    <BrowserRouter>

      <Navbar />

      <Routes>

        <Route path="/" element={<Dashboard />} />

        <Route path="/products" element={<Products />} />

        <Route path="/suppliers" element={<Suppliers />} />

        <Route path="/analytics" element={<Analytics />} />

        <Route path="/logs" element={<InventoryLogs />} />

      </Routes>

    </BrowserRouter>
  );
}

export default App;