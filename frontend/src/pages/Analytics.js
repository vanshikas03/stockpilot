import { useEffect, useState } from "react";
import { getAnalytics } from "../services/Api";

function Analytics() {

    const [analytics, setAnalytics] = useState(null);

    useEffect(() => {

        loadAnalytics();

    }, []);

    const loadAnalytics = () => {

        getAnalytics()
            .then((response) => {

                setAnalytics(response.data);

            })
            .catch((error) => {

                console.log(error);

            });

    };

    if (!analytics) {

        return (
            <div className="p-8">
                Loading Analytics...
            </div>
        );

    }

    return (

    <div className="p-8 bg-gray-100 min-h-screen">

        <h1 className="text-4xl font-bold mb-8">
            📊 Inventory Analytics
        </h1>

        {/* Summary Cards */}

        <div className="grid grid-cols-3 gap-6 mb-8">

            <div className="bg-blue-600 text-white rounded-lg shadow-lg p-6">

                <h2 className="text-lg">Total Products</h2>

                <p className="text-4xl font-bold mt-3">
                    {analytics.total_products}
                </p>

            </div>

            <div className="bg-green-600 text-white rounded-lg shadow-lg p-6">

                <h2 className="text-lg">Inventory Value</h2>

                <p className="text-3xl font-bold mt-3">
                    ₹ {analytics.total_inventory_value.toLocaleString()}
                </p>

            </div>

            <div className="bg-red-600 text-white rounded-lg shadow-lg p-6">

                <h2 className="text-lg">Low Stock Products</h2>

                <p className="text-4xl font-bold mt-3">
                    {analytics.low_stock_products.length}
                </p>

            </div>

        </div>

        {/* Products by Category */}

        <div className="bg-white rounded-lg shadow-lg p-6 mb-8">

            <h2 className="text-2xl font-semibold mb-4">
                Products by Category
            </h2>

            <table className="w-full">

                <thead className="bg-gray-200">

                    <tr>

                        <th className="p-3 text-left">Category</th>

                        <th className="p-3 text-left">Products</th>

                    </tr>

                </thead>

                <tbody>

                    {Object.entries(analytics.products_by_category).map(([category, count]) => (

                        <tr key={category} className="border-b">

                            <td className="p-3">{category}</td>

                            <td className="p-3">{count}</td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

        {/* Most Valuable Products */}

        <div className="bg-white rounded-lg shadow-lg p-6 mb-8">

            <h2 className="text-2xl font-semibold mb-4">
                Top Valuable Products
            </h2>

            <table className="w-full">

                <thead className="bg-gray-200">

                    <tr>

                        <th className="p-3 text-left">Product</th>

                        <th className="p-3 text-left">Inventory Value</th>

                    </tr>

                </thead>

                <tbody>

                    {analytics.most_valuable_products.map((product, index) => (

                        <tr key={index} className="border-b">

                            <td className="p-3">
                                {product.product_name}
                            </td>

                            <td className="p-3">
                                ₹ {product.inventory_value.toLocaleString()}
                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

        {/* Restock Recommendations */}

        <div className="bg-white rounded-lg shadow-lg p-6">

            <h2 className="text-2xl font-semibold mb-4">
                Restock Recommendations
            </h2>

            {analytics.restock_recommendations.length === 0 ? (

                <p className="text-green-600 font-semibold">
                    🎉 No products need restocking.
                </p>

            ) : (

                <ul className="list-disc pl-6">

                    {analytics.restock_recommendations.map((product, index) => (

                        <li key={index}>
                            {product.product_name}
                        </li>

                    ))}

                </ul>

            )}

        </div>

    </div>

    );

}

export default Analytics;