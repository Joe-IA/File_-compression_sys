import base64

with open("pikachu.jpeg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

decoded_string = base64.b64decode(encoded_string)

with open("reconstructed.jpeg", "wb") as fh:
    fh.write(base64.b64decode(encoded_string))