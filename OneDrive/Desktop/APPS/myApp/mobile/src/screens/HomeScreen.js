import React, { useState } from "react";
import { View, FlatList, Text } from "react-native";
import ProductSearch from "../components/ProductSearch";

export default function HomeScreen() {
    const [products, setProducts] = useState([]);

    const handleSearchResults = (results) => {
        setProducts(results);
    };

    return (
        <View style={{ flex: 1 }}>
            <ProductSearch onSearchResults={handleSearchResults} />
            <FlatList
                data={products}
                keyExtractor={(item) => item.link}
                renderItem={({ item }) => (
                    <View>
                        <Text>{item.title}</Text>
                        <Text>{item.price}</Text>
                        <Text>{item.link}</Text>
                    </View>
                )}
            />
        </View>
    );
}
