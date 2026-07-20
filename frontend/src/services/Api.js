import axios from "axios";

const API = axios.create({
    baseURL: "http://127.0.0.1:8000"
});

// =====================================
// Analytics API
// =====================================

export const getAnalytics = () =>
    API.get("/analytics");

// =====================================
// Products APIs
// =====================================

export const getProducts = () =>
    API.get("/products");

export const addProduct = (product) =>
    API.post("/products", product);

export const updateProduct = (id, product) =>
    API.put(`/products/${id}`, product);

export const deleteProduct = (id) =>
    API.delete(`/products/${id}`);

// =====================================
// Suppliers APIs
// =====================================

export const getSuppliers = () =>
    API.get("/suppliers");

export const addSupplier = (supplier) =>
    API.post("/suppliers", supplier);

export const updateSupplier = (id, supplier) =>
    API.put(`/suppliers/${id}`, supplier);

export const deleteSupplier = (id) =>
    API.delete(`/suppliers/${id}`);

// =====================================
// Inventory Logs API
// =====================================

export const getInventoryLogs = () =>
    API.get("/inventory-logs");

// =====================================

export default API;