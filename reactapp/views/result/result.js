import React from 'react';
import { Text, View, Image, TouchableOpacity } from 'react-native';
import styles from './resultStyles.js';
import Header from '../../components/header/header.js';
import { Icon } from 'react-native-elements';

export default function Result() {
    const renderedResults = [];
    for (let count = 0; count < probResult.length; count++) {
        renderedResults.push(
            <View style={styles.resultSentence} key={count}>
                <Text>Crack predicted accuracy: <Text style={{ fontWeight: 'bold' }}>{probResult[count][1]}%</Text></Text>
                <Text>The area of crack is: <Text style={{ fontWeight: 'bold' }}>{probResult[count][0]}</Text></Text>
            </View>
        )
    }
    return (
        <View style={styles.container}>
            <Header isChild={true} />
            {/* <Text style={styles.test}>{imageResult}</Text> */}
            <View style={styles.imageContainer}>
                <Image
                    source={{ uri: `data:image/png;base64,${imageResult}` }}
                    style={styles.image}
                />
                {/* <Text>a</Text> */}
            </View>
            <View style={styles.resultBackground}>
                <Text style={styles.resultHeader}>Result:</Text>
                <View>{renderedResults}</View>
            </View>
        </View>
    )
}