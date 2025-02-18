import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:5000", // Подставь свой сервер
});

export const searchProducts = async (query) => {
    try {
        const response = await api.get(`/products/search?query=${query}`);
        return response.data.results;
    } catch (error) {
        console.error("Ошибка API:", error);
        throw error;
    }
};
