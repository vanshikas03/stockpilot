import { useEffect, useState } from "react";
import { getInventoryLogs } from "../services/Api";

function InventoryLogs() {

    const [logs, setLogs] = useState([]);

    useEffect(() => {

        loadLogs();

    }, []);

    const loadLogs = () => {

    getInventoryLogs()
        .then((response) => {

            console.log("Inventory Logs:", response.data);

            setLogs(response.data);

        })
        .catch((error) => {

            console.log("API Error:", error);

        });

};

        return (

        <div className="p-8 bg-gray-100 min-h-screen">

            <h1 className="text-4xl font-bold mb-8">
                📋 Inventory Logs
            </h1>

            <div className="bg-white shadow-lg rounded-lg overflow-hidden">

                <table className="w-full">

                    <thead className="bg-gray-200">

                        <tr>

                            <th className="p-3 text-left">Log ID</th>

                            <th className="p-3 text-left">Product ID</th>

                            <th className="p-3 text-left">Action</th>

                            <th className="p-3 text-left">Qty Changed</th>

                            <th className="p-3 text-left">Previous Qty</th>

                            <th className="p-3 text-left">New Qty</th>

                            <th className="p-3 text-left">Remarks</th>

                            <th className="p-3 text-left">Timestamp</th>

                        </tr>

                    </thead>

                    <tbody>

                        {logs.length === 0 ? (

                            <tr>

                                <td
                                    colSpan="8"
                                    className="text-center p-6 text-gray-500"
                                >
                                    No inventory logs found.
                                </td>

                            </tr>

                        ) : (

                            logs.map((log) => (

                                <tr
                                    key={log.log_id}
                                    className="border-b hover:bg-gray-50"
                                >

                                    <td className="p-3">
                                        {log.log_id}
                                    </td>

                                    <td className="p-3">
                                        {log.product_id}
                                    </td>

                                    <td className="p-3">

                                        <span
                                            className={`px-3 py-1 rounded-full text-white text-sm font-semibold
                                                ${
                                                    log.action === "CREATE"
                                                        ? "bg-green-600"
                                                        : log.action === "UPDATE"
                                                        ? "bg-blue-600"
                                                        : "bg-red-600"
                                                }`}
                                        >
                                            {log.action}
                                        </span>

                                    </td>

                                    <td className="p-3">
                                        {log.quantity_changed}
                                    </td>

                                    <td className="p-3">
                                        {log.previous_quantity}
                                    </td>

                                    <td className="p-3">
                                        {log.new_quantity}
                                    </td>

                                    <td className="p-3">
                                        {log.remarks}
                                    </td>

                                    <td className="p-3">
                                        {log.timestamp}
                                    </td>

                                </tr>

                            ))

                        )}

                    </tbody>

                </table>

            </div>

        </div>

    );

}

export default InventoryLogs;