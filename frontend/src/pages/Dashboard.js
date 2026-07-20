import { useEffect, useState } from "react";
import API from "../services/Api";

function Dashboard() {

    const [analytics, setAnalytics] = useState(null);

    useEffect(() => {

        API.get("/analytics")
            .then((response) => {
                setAnalytics(response.data);
            })
            .catch((error) => {
                console.log(error);
            });

    }, []);

    if (!analytics) {
        return (
            <h2 className="text-center mt-10 text-xl">
                Loading...
            </h2>
        );
    }

    return (

        <div className="p-8">

            <h1 className="text-3xl font-bold mb-8">
                Dashboard
            </h1>

            <div className="grid grid-cols-3 gap-6">

                <div className="bg-white rounded-lg shadow-md p-6">

                    <h2 className="text-gray-500">
                        Total Products
                    </h2>

                    <p className="text-3xl font-bold">
                        {analytics.total_products}
                    </p>

                </div>

                <div className="bg-white rounded-lg shadow-md p-6">

                    <h2 className="text-gray-500">
                        Inventory Value
                    </h2>

                    <p className="text-3xl font-bold">
                        ₹ {analytics.total_inventory_value}
                    </p>

                </div>

                <div className="bg-white rounded-lg shadow-md p-6">

                    <h2 className="text-gray-500">
                        Low Stock
                    </h2>

                    <p className="text-3xl font-bold">
                        {analytics.low_stock_products.length}
                    </p>

                </div>

            </div>

        </div>

    );

}

export default Dashboard;
