import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import API from "../services/Api";

function Dashboard() {

    const [analytics, setAnalytics] = useState(null);

    useEffect(() => {

        loadAnalytics();

    }, []);

    const loadAnalytics = () => {

        API.get("/analytics")
            .then((response) => {

                setAnalytics(response.data);

            })
            .catch((error) => {

                console.log(error);

            });

    };

    if (!analytics) {

        return (

            <div className="flex justify-center items-center h-screen">

                <h1 className="text-3xl font-bold animate-pulse">
                    Loading Dashboard...
                </h1>

            </div>

        );

    };

    return (

    <div className="min-h-screen bg-gray-100 p-8">

        {/* Header */}

        <div className="flex justify-between items-center mb-10">

            <div>

                <h1 className="text-4xl font-bold text-gray-800">
                    StockPilot Dashboard
                </h1>

                <p className="text-gray-500 mt-2">
                    Welcome to your Inventory Management System
                </p>

            </div>

            <div>

                <Link
                    to="/products"
                    className="bg-blue-600 text-white px-5 py-3 rounded-lg shadow hover:bg-blue-700 mr-3"
                >
                    + Product
                </Link>

                <Link
                    to="/suppliers"
                    className="bg-green-600 text-white px-5 py-3 rounded-lg shadow hover:bg-green-700"
                >
                    + Supplier
                </Link>

            </div>

        </div>

        {/* Summary Cards */}

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">

            <div className="bg-gradient-to-r from-blue-500 to-blue-700 text-white rounded-xl shadow-lg p-6">

                <h2 className="text-lg">
                     Total Products
                </h2>

                <p className="text-5xl font-bold mt-4">
                    {analytics.total_products}
                </p>

            </div>

            <div className="bg-gradient-to-r from-green-500 to-green-700 text-white rounded-xl shadow-lg p-6">

                <h2 className="text-lg">
                     Inventory Value
                </h2>

                <p className="text-3xl font-bold mt-4">
                    ₹ {analytics.total_inventory_value.toLocaleString()}
                </p>

            </div>

            <div className="bg-gradient-to-r from-red-500 to-red-700 text-white rounded-xl shadow-lg p-6">

                <h2 className="text-lg">
                     Low Stock Products
                </h2>

                <p className="text-5xl font-bold mt-4">
                    {analytics.low_stock_products.length}
                </p>

            </div>

        </div>

        {/* Two Sections */}

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">

            {/* Products by Category */}

            <div className="bg-white rounded-xl shadow-lg p-6">

                <h2 className="text-2xl font-bold mb-5">
                     Products by Category
                </h2>

                <table className="w-full">

                    <thead className="bg-gray-100">

                        <tr>

                            <th className="text-left p-3">
                                Category
                            </th>

                            <th className="text-left p-3">
                                Products
                            </th>

                        </tr>

                    </thead>

                    <tbody>

                        {Object.entries(analytics.products_by_category).map(([category, count]) => (

                            <tr
                                key={category}
                                className="border-b"
                            >

                                <td className="p-3">
                                    {category}
                                </td>

                                <td className="p-3 font-semibold">
                                    {count}
                                </td>

                            </tr>

                        ))}

                    </tbody>

                </table>

            </div>

            {/* Most Valuable Products */}

            <div className="bg-white rounded-xl shadow-lg p-6">

                <h2 className="text-2xl font-bold mb-5">
                     Top Valuable Products
                </h2>

                <table className="w-full">

                    <thead className="bg-gray-100">

                        <tr>

                            <th className="text-left p-3">
                                Product
                            </th>

                            <th className="text-left p-3">
                                Value
                            </th>

                        </tr>

                    </thead>

                    <tbody>

                        {analytics.most_valuable_products.map((product, index) => (

                            <tr
                                key={index}
                                className="border-b"
                            >

                                <td className="p-3">
                                    {product.product_name}
                                </td>

                                <td className="p-3 font-semibold">
                                    ₹ {product.inventory_value.toLocaleString()}
                                </td>

                            </tr>

                        ))}

                    </tbody>

                </table>

            </div>

        </div>

        {/* Quick Actions */}

        <div className="bg-white rounded-xl shadow-lg mt-10 p-6">

            <h2 className="text-2xl font-bold mb-5">
                 Quick Actions
            </h2>

            <div className="flex flex-wrap gap-4">

                <Link
                    to="/products"
                    className="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700"
                >
                    Manage Products
                </Link>

                <Link
                    to="/suppliers"
                    className="bg-green-600 text-white px-6 py-3 rounded-lg hover:bg-green-700"
                >
                    Manage Suppliers
                </Link>

                <Link
                    to="/analytics"
                    className="bg-purple-600 text-white px-6 py-3 rounded-lg hover:bg-purple-700"
                >
                    View Analytics
                </Link>

                <Link
                    to="/inventory-logs"
                    className="bg-orange-600 text-white px-6 py-3 rounded-lg hover:bg-orange-700"
                >
                    Inventory Logs
                </Link>

            </div>

        </div>

    </div>

);

}

export default Dashboard;