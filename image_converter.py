import binascii
import base64
import os
import logging
import sys

def encode_images(images_dict):
    try:
        for this_image in images_dict:
            image_name = binascii.unhexlify(this_image["identifier"].encode()).decode()
            with open(os.path.abspath('images/%s' % image_name), "rb") as image_file:
                image_data = image_file.read()
                # Encrypts image data
                image_data_encoded = base64.b64encode(image_data)
                print("--------------")
                print("Encoded %s image!" % image_name)
                this_image["data"] = image_data_encoded.decode()
    except:
        logging.exception("Unexpected error enconding immages: %s ", sys.exc_info()[0])

    return images_dict