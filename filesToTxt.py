<<<<<<< HEAD
import numpy as np
import PIL.Image as Image
import base64


class ImagesToTxt:
    @staticmethod
    def image_to_text(route):
        imagen = Image.open(route)
        matriz = np.array(imagen)
        width, height, channels = matriz.shape
        binarios = matriz.tobytes()
        return width, height, channels, binarios

    @staticmethod
    def text_to_image(width, height, channels, binarios, route):
        matriz = np.frombuffer(binarios, dtype=np.uint8)
        matriz = matriz.reshape((width, height, channels))
        imagen = Image.fromarray(matriz)
        imagen.save(route)




if __name__ == "__main__":
  w, h, c, b = ImagesToTxt.image_to_text("imagen1.bmp")
  print(f"type w: {type(w)}, type h: {type(h)}, type c: {type(c)}, type b: {type(b)}")
  ImagesToTxt.text_to_image(w, h, c, b, "imagen2.bmp")