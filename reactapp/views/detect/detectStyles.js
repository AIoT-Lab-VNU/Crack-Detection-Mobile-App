import { StyleSheet, Dimensions } from 'react-native';

const screenWidth = Dimensions.get('screen').width;
const screenHeight = Dimensions.get('screen').height;

const styles = StyleSheet.create({
    container: {
        height: '100%'
    },
    cameraContainer: {
        // flex: 1,
        // justifyContent: 'flex-end',
        // alignItems: 'center',
        borderWidth: 1,
        borderColor: 'rgba(0, 0, 0, 0.5)', // Adjust the alpha value as needed
        borderStyle: 'solid',
        position: 'relative',
        top: 0,
        width: screenWidth,
        height: screenHeight,
        // display: 'flex',
        // flexDirection: 'row',
        // alignItems: 'flex-end'
    },
    capture: {
        flex: 0,
        backgroundColor: '#fff',
        borderRadius: 5,
        padding: 15,
        paddingHorizontal: 20,
        alignSelf: 'center',
        margin: 20,
      },
      btnContainer: {
        position: 'absolute',
        width: '100%',
        height: 80,
        bottom: 150,
        // backgroundColor: 'rgba(0,0,0,0.5)',
        display: 'flex',
        alignItems: 'center'
      },
      btnCapture: {
        width: 50,
        position: 'absolute',
        left: '50%',
        top: '50%',
        transform: [{translateY: -50}, {translateX: -50}],
        width: 80,
        height: 80,
        backgroundColor: 'rgba(0,0,0,0.5)',
        borderRadius: 80,
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        border: '10px solid #fff'
      },
      btnLib: {
        width: 50,
        position: 'absolute',
        left: 20
      }
})

export default styles;