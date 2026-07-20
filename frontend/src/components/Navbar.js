import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="bg-slate-800 text-white px-8 py-4 flex justify-between items-center shadow-md">

      <h1 className="text-2xl font-bold">
        StockPilot
      </h1>

      <div className="flex gap-8">

        <Link to="/" className="hover:text-blue-300">
          Dashboard
        </Link>

        <Link to="/products" className="hover:text-blue-300">
          Products
        </Link>

        <Link to="/suppliers" className="hover:text-blue-300">
          Suppliers
        </Link>

        <Link to="/analytics" className="hover:text-blue-300">
          Analytics
        </Link>

        <Link to="/logs" className="hover:text-blue-300">
          Inventory Logs
        </Link>

      </div>

    </nav>
  );
}

export default Navbar;