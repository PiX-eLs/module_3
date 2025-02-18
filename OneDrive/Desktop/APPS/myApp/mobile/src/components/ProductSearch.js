import React, { useState } from "react";
import { View, TextInput, Button, Text, FlatList } from "react-native";
import axios from "axios";
import { searchProducts } from "../services/api";

export default function ProductSearch({ onSearchResults }) {
    const [query, setQuery] = useState("");
    const [loading, setLoading] = useState(false);

    const searchProducts = async () => {
        setLoading(true);
        try {
            const response = await axios.get(
                `http://localhost:5000/products/search?query=${query}`,
            );
            onSearchResults(response.data.results); // передаем результат родительскому компоненту
        } catch (error) {
            console.error("Ошибка при поиске товаров:", error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <View style={{ padding: 20 }}>
            <TextInput
                style={{
                    height: 40,
                    borderColor: "gray",
                    borderWidth: 1,
                    marginBottom: 10,
                }}
                placeholder="Поиск товаров..."
                value={query}
                onChangeText={setQuery}
            />
            <Button title="Найти" onPress={searchProducts} />
            {loading && <Text>Загрузка...</Text>}
        </View>
    );
}

// Внутри компонента
const searchProductsHandler = async () => {
    setLoading(true);
    try {
        const results = await searchProducts(query);
        onSearchResults(results);
    } catch (error) {
        console.error("Ошибка при поиске товаров:", error);
    } finally {
        setLoading(false);
    }
};
