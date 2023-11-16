import React from 'react';
import { useRef, useState } from 'react';
import { Text, View, Image, TouchableOpacity } from 'react-native';
import styles from './detectStyles.js';
import Header from '../../components/header/header.js';
import { RNCamera } from 'react-native-camera';
import { Icon } from 'react-native-elements';
import axios from 'axios';
import { useNavigation } from '@react-navigation/native';
import RNFetchBlob from 'react-native-blob-util';
import { launchImageLibrary } from 'react-native-image-picker';
import RNFS from 'react-native-fs';


export default function Detect() {
    const [selectedImage, setSelectedImage] = useState(null);
    const navigation = useNavigation();
    const cameraRef = useRef(null);
    // const [probResult, setProbResult] = useState(null);
    // const [imageResult,setImageResult] = useState(null);

    // const saveBase64ImageToFile = async (base64String, folderPath, fileName) => {
    //     try {
    //         const filePath = `${folderPath}/${fileName}`;
    //         const binaryData = atob(base64String);
    //         const arrayBuffer = new ArrayBuffer(binaryData.length);
    //         const uint8Array = new Uint8Array(arrayBuffer);
    //         for (let i = 0; i < binaryData.length; i++) {
    //             uint8Array[i] = binaryData.charCodeAt(i);
    //         }

    //         await RNFetchBlob.fs.writeFile(filePath, arrayBuffer, 'ascii');
    //     }
    //     catch (error) {
    //         console.log('Error convert base64 to image: ', error)
    //         throw error;
    //     }
    // }

    const takePicture = async () => {
        if (cameraRef.current) {
            const options = { quality: 0.5, base64: true };
            const data = await cameraRef.current.takePictureAsync(options);

            // Display the captured image
            // console.log('Captured Image:', data);
            try {
                console.log('Sending request')
                axios.post('http://10.0.2.2:5000/process-image', JSON.stringify(data), {
                    headers: {
                        'Content-Type': 'application/json',
                    }
                })
                    .then((response) => {
                        probResult = JSON.parse(response.data.result)
                        imageResult = response.data.image

                        // saveBase64ImageToFile(imageResult, '../../assets/images', 'result.png');

                        navigation.navigate('Result', { imageResult: imageResult, probResult: probResult })
                        // console.log("a: ", JSON.parse(response.data.result)[0])
                    })
                    .catch((error) => console.log('errorRN:', error))

            }
            catch (error) {
                console.log('erroRN: ', error)
            }

        }
    }

    const convertImageToBase64 = async (uri) => {
        try {
            const imgBase64 = await RNFS.readFile(uri, 'base64');
            return imgBase64
        }
        catch (error) {
            console.log('error: ', error)
            throw error;
        }
    }

    const selectImage = async () => {
        const options = {
            width: 320,
            height: 240,
            cropping: true,
            compressImageQuality: 0.7
        };

        const result = await launchImageLibrary(options)
        if (!result.didCancel) {
            setSelectedImage({ uri: result.assets[0].uri });

            const base64Image = await convertImageToBase64(result.assets[0].uri);
            try {
                console.log('Sending request')
                axios.post('http://10.0.2.2:5000/process-selected-image', JSON.stringify(base64Image), {
                    headers: {
                        'Content-Type': 'application/json',
                    }
                })
                    .then((response) => {
                        probResult = JSON.parse(response.data.result)
                        imageResult = response.data.image

                        // saveBase64ImageToFile(imageResult, '../../assets/images', 'result.png');

                        navigation.navigate('Result', { imageResult: imageResult, probResult: probResult })
                        // console.log("a: ", JSON.parse(response.data.result)[0])
                    })
                    .catch((error) => console.log('errorRN:', error))

            }
            catch (error) {
                console.log('erroRN: ', error)
            }
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
                    <TouchableOpacity style={styles.btnLib} onPress={selectImage}>
                        <Icon
                            type="ionicon"
                            name="images-outline"
                            color="#FFFFFF"
                            iconProps={{ size: 50 }}
                        />
                    </TouchableOpacity>
                    <TouchableOpacity style={styles.btnCapture} onPress={takePicture}>
                        <Text style={{ fontSize: 14, color: '#ffffff' }}>SNAP</Text>
                    </TouchableOpacity>
                </View>
            </RNCamera>
        </View>
    )
}