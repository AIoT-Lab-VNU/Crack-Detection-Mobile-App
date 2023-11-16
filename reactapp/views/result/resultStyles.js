import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
    container: {

    },
    test: {
        position: 'relative',
        top: 100
    },
    image: {
        width: "100%",
        height: '100%',
        position: 'absolute',
        objectFit: 'contain',
        // transform: [{rotate: '90deg'}]
    },
    imageContainer: {
        width: "100%",
        height: 300,
        position: 'relative',
        backgroundColor: '#333',
        // transform: [{rotate: '90deg'}]
    },
    resultBackground: {
        backgroundColor: '#D9D9D9',
        padding: 20
    },
    resultHeader: {
        fontSize: 23,
        fontWeight: 'bold',
        marginBottom: 10
    },
    resultSentence: {
        position: 'relative',
        width: '100%',
        marginBottom: 15
    }
})

export default styles;