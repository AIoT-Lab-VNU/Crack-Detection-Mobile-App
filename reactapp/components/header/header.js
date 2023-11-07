import React from 'react';
import { Text, View, Image, TouchableOpacity } from 'react-native';
import { useNavigation } from '@react-navigation/native'
import styles from './headerStyles.js';
// import HeartIcon from 'react-native-heroicons/solid';
import { Icon } from 'react-native-elements';

export default function Header({ isChild }) {
    const navigation = useNavigation();
    return (
        <View style={styles.container}>
            {
                isChild &&
                <TouchableOpacity 
                onPress={() => navigation.goBack()}
                style={styles.backButton}>
                    <Icon
                        type="ionicon"
                        name="arrow-back-circle-outline"
                        color="#FFFFFF"
                        iconProps={{ size: 50 }}
                    />
                </TouchableOpacity>
            }
            <View style={styles.header}>
                <Image
                    style={styles.logo}
                    source={require("../../assets/images/icon.png")}
                />
                <Text style={styles.headerTitle}>AIOT Lab VN</Text>
            </View>
        </View>
    )
}