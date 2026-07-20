import axios from "axios";

const API = axios.create({
    baseURL: "http://127.0.0.1:8000"
});

export const getAnalytics = () => API.get("/analytics");

export const getProducts = () => API.get("/products");

export const addProduct = (product) => API.post("/products", product);

export const updateProduct = (id, product) => API.put(`/products/${id}`, product);

export const deleteProduct = (id) => API.delete(`/products/${id}`);

export default API;