from PIL import Image
import base64
import io

def decode_image(image_dir):
    # try:
    #     print(image)
    #     buffered = io.ByteIO()
    #     image.save(buffered, format="png")
    #     img_base64 = Buffer.from()
    #     print(img_base64)
    #     return img_base64
    # except Exception as ex:
    #     print("Exception: ", ex)
    #     return ''
    with open(image_dir, 'rb') as image_file:
        base64_bytes = base64.b64encode(image_file.read())
        # print(base64_bytes)
        return base64_bytes

