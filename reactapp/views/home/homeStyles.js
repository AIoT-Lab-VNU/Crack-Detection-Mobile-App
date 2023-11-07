import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
    container: {
        display: 'flex',
        justifyContent: "center",
        alignItems: 'center'
    },
    introduction: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        alignContent: 'center',
        marginTop: 18
    },
    title: {
        color: '#1362C5',
        fontSize: 30,
        fontWeight: 'bold',
        textTransform: 'uppercase',
        marginBottom: 20
    },
    content: {
        fontSize: 24,
        fontWeight: 'normal',
        color: "#000",
        marginBottom: 10,
        textAlign: 'center'
    },
    button: {
        paddingTop: 15,
        paddingBottom: 15,
        backgroundColor: '#1362C5',
        borderRadius: 20,
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        width: 300,
        marginTop: 30
    },
    buttonText: {
        color: '#FFFFFF',
        fontSize: 30,
        fontWeight: 'bold',
        textTransform: 'uppercase'
    }
})

export default styles;