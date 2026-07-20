import { useEffect, useState } from "react";
import {
    getProducts,
    addProduct,
    updateProduct,
    deleteProduct
} from "../services/Api";

function Products() {

    const [products, setProducts] = useState([]);

    const [editingId, setEditingId] = useState(null);

    const [formData, setFormData] = useState({
        supplier_id: "",
        product_name: "",
        category: "",
        quantity: "",
        purchase_price: "",
        selling_price: "",
        reorder_level: ""
    });

    useEffect(() => {
        loadProducts();
    }, []);

    const loadProducts = () => {

        getProducts()
            .then((response) => {
                setProducts(response.data);
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
            supplier_id: "",
            product_name: "",
            category: "",
            quantity: "",
            purchase_price: "",
            selling_price: "",
            reorder_level: ""
        });

        setEditingId(null);

    };

    const handleSubmit = () => {

        if (editingId === null) {

            addProduct(formData)
                .then(() => {

                    alert("Product added successfully!");

                    loadProducts();

                    resetForm();

                })
                .catch((error) => {

                    console.log(error);

                    alert("Unable to add product.");

                });

        } else {

            updateProduct(editingId, formData)
                .then(() => {

                    alert("Product updated successfully!");

                    loadProducts();

                    resetForm();

                })
                .catch((error) => {

                    console.log(error);

                    alert("Unable to update product.");

                });

        }

    };

    const handleEdit = (product) => {

        setEditingId(product.product_id);

        setFormData({
            supplier_id: product.supplier_id,
            product_name: product.product_name,
            category: product.category,
            quantity: product.quantity,
            purchase_price: product.purchase_price,
            selling_price: product.selling_price,
            reorder_level: product.reorder_level
        });

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });

    };

    const handleDelete = (id) => {

        if (!window.confirm("Delete this product?")) {
            return;
        }

        deleteProduct(id)
            .then(() => {

                alert("Product deleted successfully!");

                loadProducts();

                if (editingId === id) {
                    resetForm();
                }

            })
            .catch((error) => {

                console.log(error);

                alert("Unable to delete product.");

            });

    };

    return (

        <div className="p-8">

            <h1 className="text-3xl font-bold mb-6">
                Products
            </h1>

            {/* Add Product Form */}

            <div className="bg-white shadow rounded-lg p-6 mb-8">

                <h2 className="text-xl font-semibold mb-4">
                    Add Product
                </h2>

                <div className="grid grid-cols-2 gap-4">

                    <input
                        type="number"
                        name="supplier_id"
                        placeholder="Supplier ID"
                        value={formData.supplier_id}
                        onChange={handleChange}
                        className="border p-2 rounded"
                    />

                    <input
                        type="text"
                        name="product_name"
                        placeholder="Product Name"
                        value={formData.product_name}
                        onChange={handleChange}
                        className="border p-2 rounded"
                    />

                    <input
                        type="text"
                        name="category"
                        placeholder="Category"
                        value={formData.category}
                        onChange={handleChange}
                        className="border p-2 rounded"
                    />

                    <input
                        type="number"
                        name="quantity"
                        placeholder="Quantity"
                        value={formData.quantity}
                        onChange={handleChange}
                        className="border p-2 rounded"
                    />

                    <input
                        type="number"
                        name="purchase_price"
                        placeholder="Purchase Price"
                        value={formData.purchase_price}
                        onChange={handleChange}
                        className="border p-2 rounded"
                    />

                    <input
                        type="number"
                        name="selling_price"
                        placeholder="Selling Price"
                        value={formData.selling_price}
                        onChange={handleChange}
                        className="border p-2 rounded"
                    />

                    <input
                        type="number"
                        name="reorder_level"
                        placeholder="Reorder Level"
                        value={formData.reorder_level}
                        onChange={handleChange}
                        className="border p-2 rounded"
                    />

                </div>

                <button
                    onClick={handleSubmit}
                    className="bg-green-600 text-white px-6 py-2 rounded mt-6 hover:bg-green-700"
                >
                    Save Product
                </button>

            </div>

            {/* Products Table */}

            <div className="bg-white shadow rounded-lg overflow-hidden">

                <table className="w-full">

                    <thead className="bg-gray-200">

                        <tr>

                            <th className="p-3 text-left">ID</th>
                            <th className="p-3 text-left">Product</th>
                            <th className="p-3 text-left">Category</th>
                            <th className="p-3 text-left">Quantity</th>
                            <th className="p-3 text-left">Selling Price</th>
                            <th className="p-3 text-left">Actions</th>

                        </tr>

                    </thead>

                    <tbody>

                        {products.length === 0 ? (

                            <tr>

                                <td
                                    colSpan="6"
                                    className="text-center p-6 text-gray-500"
                                >
                                    No products found.
                                </td>

                            </tr>

                        ) : (

                            products.map((product) => (

                                <tr
                                    key={product.product_id}
                                    className="border-b hover:bg-gray-50"
                                >

                                    <td className="p-3">
                                        {product.product_id}
                                    </td>

                                    <td className="p-3">
                                        {product.product_name}
                                    </td>

                                    <td className="p-3">
                                        {product.category}
                                    </td>

                                    <td className="p-3">
                                        {product.quantity}
                                    </td>

                                    <td className="p-3">
                                        ₹ {Number(product.selling_price).toLocaleString()}
                                    </td>

                                    <td className="p-3">

                                        <button
                                            onClick={() => handleEdit(product)}
                                            className="bg-yellow-500 text-white px-3 py-1 rounded mr-2 hover:bg-yellow-600"
                                        >
                                            {editingId === null ? "Edit" : "Save Product"}
                                        </button>

                                        <button
                                            onClick={() => handleDelete(product.product_id)}
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

export default Products;