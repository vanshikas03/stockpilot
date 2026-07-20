import { useEffect, useState } from "react";
import {
    getSuppliers,
    addSupplier,
    updateSupplier,
    deleteSupplier
} from "../services/Api";

function Suppliers() {

    const [suppliers, setSuppliers] = useState([]);

    const [editingId, setEditingId] = useState(null);

    const [formData, setFormData] = useState({
        supplier_name: "",
        contact_person: "",
        email: "",
        phone: "",
        address: ""
    });

    useEffect(() => {
        loadSuppliers();
    }, []);

    const loadSuppliers = () => {

        getSuppliers()
            .then((response) => {
                setSuppliers(response.data);
            })
            .catch((error) => {
                console.log(error);
            });

    };

    const handleChange = (e) => {

        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });

    };

    const resetForm = () => {

        setFormData({
            supplier_name: "",
            contact_person: "",
            email: "",
            phone: "",
            address: ""
        });

        setEditingId(null);

    };

    const handleSubmit = () => {

        if (editingId === null) {

            addSupplier(formData)
                .then(() => {

                    alert("Supplier added successfully!");

                    loadSuppliers();

                    resetForm();

                })
                .catch((error) => {

                    console.log(error);

                    alert("Unable to add supplier.");

                });

        } else {

            updateSupplier(editingId, formData)
                .then(() => {

                    alert("Supplier updated successfully!");

                    loadSuppliers();

                    resetForm();

                })
                .catch((error) => {

                    console.log(error);

                    alert("Unable to update supplier.");

                });

        }

    };

    const handleEdit = (supplier) => {

        setEditingId(supplier.supplier_id);

        setFormData({
            supplier_name: supplier.supplier_name,
            contact_person: supplier.contact_person,
            email: supplier.email,
            phone: supplier.phone,
            address: supplier.address
        });

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });

    };

    const handleDelete = (id) => {

        if (!window.confirm("Delete this supplier?")) {
            return;
        }

        deleteSupplier(id)
            .then(() => {

                alert("Supplier deleted successfully!");

                loadSuppliers();

                if (editingId === id) {
                    resetForm();
                }

            })
            .catch((error) => {

                console.log(error);

                alert("Unable to delete supplier.");

            });

    };

        return (

        <div className="p-8">

            <h1 className="text-3xl font-bold mb-6">
                Suppliers
            </h1>

            {/* Add Supplier Form */}

            <div className="bg-white shadow rounded-lg p-6 mb-8">

                <h2 className="text-xl font-semibold mb-4">
                    {editingId === null ? "Add Supplier" : "Edit Supplier"}
                </h2>

                <div className="grid grid-cols-2 gap-4">

                    <input
                        type="text"
                        name="supplier_name"
                        placeholder="Supplier Name"
                        value={formData.supplier_name}
                        onChange={handleChange}
                        className="border p-2 rounded"
                    />

                    <input
                        type="text"
                        name="contact_person"
                        placeholder="Contact Person"
                        value={formData.contact_person}
                        onChange={handleChange}
                        className="border p-2 rounded"
                    />

                    <input
                        type="email"
                        name="email"
                        placeholder="Email"
                        value={formData.email}
                        onChange={handleChange}
                        className="border p-2 rounded"
                    />

                    <input
                        type="text"
                        name="phone"
                        placeholder="Phone"
                        value={formData.phone}
                        onChange={handleChange}
                        className="border p-2 rounded"
                    />

                    <textarea
                        name="address"
                        placeholder="Address"
                        value={formData.address}
                        onChange={handleChange}
                        className="border p-2 rounded col-span-2"
                        rows="3"
                    />

                </div>

                <button
                    onClick={handleSubmit}
                    className="bg-green-600 text-white px-6 py-2 rounded mt-6 hover:bg-green-700"
                >
                    {editingId === null ? "Save Supplier" : "Update Supplier"}
                </button>

            </div>

            {/* Suppliers Table */}

            <div className="bg-white shadow rounded-lg overflow-hidden">

                <table className="w-full">

                    <thead className="bg-gray-200">

                        <tr>

                            <th className="p-3 text-left">ID</th>
                            <th className="p-3 text-left">Supplier Name</th>
                            <th className="p-3 text-left">Contact Person</th>
                            <th className="p-3 text-left">Email</th>
                            <th className="p-3 text-left">Phone</th>
                            <th className="p-3 text-left">Actions</th>

                        </tr>

                    </thead>

                    <tbody>

                        {suppliers.length === 0 ? (

                            <tr>

                                <td
                                    colSpan="6"
                                    className="text-center p-6 text-gray-500"
                                >
                                    No suppliers found.
                                </td>

                            </tr>

                        ) : (

                            suppliers.map((supplier) => (

                                <tr
                                    key={supplier.supplier_id}
                                    className="border-b hover:bg-gray-50"
                                >

                                    <td className="p-3">
                                        {supplier.supplier_id}
                                    </td>

                                    <td className="p-3">
                                        {supplier.supplier_name}
                                    </td>

                                    <td className="p-3">
                                        {supplier.contact_person}
                                    </td>

                                    <td className="p-3">
                                        {supplier.email}
                                    </td>

                                    <td className="p-3">
                                        {supplier.phone}
                                    </td>

                                    <td className="p-3">

                                        <button
                                            onClick={() => handleEdit(supplier)}
                                            className="bg-yellow-500 text-white px-3 py-1 rounded mr-2 hover:bg-yellow-600"
                                        >
                                            Edit
                                        </button>

                                        <button
                                            onClick={() => handleDelete(supplier.supplier_id)}
                                            className="bg-red-600 text-white px-3 py-1 rounded hover:bg-red-700"
                                        >
                                            Delete
                                        </button>

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

export default Suppliers;

