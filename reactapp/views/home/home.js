import React from 'react';
import { Text, View, Image, TouchableOpacity } from 'react-native';
import styles from './homeStyles.js';
import Header from '../../components/header/header.js';
import { useNavigation } from '@react-navigation/native';

export default function Home() {
    const navigation = useNavigation();
    return (
        <View style={styles.container}>
            {/* Header */}
            <Header />
            {/* Introduction to Lab  */}
            <View style={styles.introduction}>
                <Text style={styles.title}>Crack Inspector 360</Text>
                <Text style={styles.content}>Quickly evaluate the location and extent of cracks, an algorithm built on the YOLOv8 platform to detect and evaluate different levels of cracks in images. Developed by students of CE and IT departments of international universities.</Text>
                <Text style={styles.title}>About Us</Text>
                <Text style={styles.content}>AIoT Lab VN, established in 2022, is a pioneering hub at the forefront of Artificial Intelligence and Internet of Things in Vietnam.</Text>
            </View>
            {/* Button redirect to detect view */}
            <TouchableOpacity 
            onPress={() => navigation.navigate('Detect')}
            style={styles.button}>
                <Text style={styles.buttonText}>Get Started</Text>
            </TouchableOpacity>
        </View>
    )
}