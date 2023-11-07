import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
    container: {
        position: 'relative',
        backgroundColor: "#1362C5",
        width: '100%'
    },
    header:{
        position: 'relative',
        width: "100%",
        height: 100,
        display: 'flex',
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'center'
    },
    headerTitle: {
        color: "#FFFFFF",
        fontSize: 28,
        fontWeight: 'bold'
    },
    logo: {
        width: 80,
        height: 80
    },
    backButton: {
        position: 'absolute',
        height: '100%',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        marginLeft: 10
    }
})

export default styles;