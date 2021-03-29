from image_converter import encode_images
import sys
import logging

def set_up_payload(request_body, IMESSAGE_EXTENSION_BID, REQUEST_IDENTIFIER):
    try:
        new_payload = request_body
        print(request_body)

        if "bid" in new_payload["interactiveData"]:
            new_payload["interactiveData"]["bid"] = IMESSAGE_EXTENSION_BID
        else:
            print("Did not found bid...")

        if "data" in new_payload["interactiveData"]:

            if "images" in new_payload["interactiveData"]["data"]:
                new_payload["interactiveData"]["data"]["images"] = encode_images(new_payload["interactiveData"]["data"]["images"])
            else:
                print("Did not found images...")

            if "requestIdentifier" in new_payload["interactiveData"]["data"]:
                new_payload["interactiveData"]["data"]["requestIdentifier"] = REQUEST_IDENTIFIER
            else:
                print("Did not found request identifier...")
        else:
            print("Did not found data in the request...")

    except:
        logging.exception("Unexpected error parsing payload: %s ", sys.exc_info()[0])

    return new_payload