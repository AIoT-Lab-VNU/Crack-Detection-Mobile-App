import React from 'react';
import { useRef } from 'react';
import { Text, View, Image, TouchableOpacity } from 'react-native';
import styles from './detectStyles.js';
import Header from '../../components/header/header.js';
import { RNCamera } from 'react-native-camera';
import { Icon } from 'react-native-elements';


export default function Detect() {
    const cameraRef = useRef(null);
    const takePicture = async () => {
        if(cameraRef.current){
            const options = { quality: 0.5, base64: true };
            const data = await cameraRef.current.takePictureAsync(options);

            // Display the captured image
            console.log('Captured Image:', data.base64);
        }
    }

    return (
        <View style={styles.container}>
            <Header isChild={true} />
            <RNCamera
                style={styles.cameraContainer}
                ref={cameraRef}
            >
                <View style={styles.btnContainer}>
                    <TouchableOpacity style={styles.btnLib}>
                        <Icon
                            type="ionicon"
                            name="images-outline"
                            color="#FFFFFF"
                            iconProps={{ size: 50 }}
                        />
                    </TouchableOpacity>
                    <TouchableOpacity style={styles.btnCapture} onPress={takePicture}>
                        <Text style={{ fontSize: 14 }}>SNAP</Text>
                    </TouchableOpacity>
                </View>
            </RNCamera>
        </View>
    )
}