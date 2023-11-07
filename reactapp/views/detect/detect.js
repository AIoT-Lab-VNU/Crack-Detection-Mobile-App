import React from 'react';
import { Text, View, Image, TouchableOpacity } from 'react-native';
import styles from './detectStyles.js';
import Header from '../../components/header/header.js';
import { RNCamera } from 'react-native-camera';

export default function Detect() {
    
    const takePicture = async () => {
        if (this.camera) {
          const options = { quality: 0.5, base64: true };
          const data = await this.camera.takePictureAsync(options);
          console.log(data.uri);
        }
      };

    return (
        <View style={styles.container}>
            <Header isChild={true} />
            <RNCamera
                ref={ref => {
                    this.camera = ref;
                }}
                style={styles.cameraContainer}
                type={RNCamera.Constants.Type.back}
                flashMode={RNCamera.Constants.FlashMode.on}
                androidCameraPermissionOptions={{
                    title: 'Permission to use camera',
                    message: 'We need your permission to use your camera',
                    buttonPositive: 'Ok',
                    buttonNegative: 'Cancel',
                }}
            />
            <View style={{ flex: 0, flexDirection: 'row', justifyContent: 'center' }}>
                <TouchableOpacity onPress={() => takePicture(this)} style={styles.capture}>
                    <Text style={{ fontSize: 14 }}> SNAP </Text>
                </TouchableOpacity>
            </View>
        </View>
    )
}