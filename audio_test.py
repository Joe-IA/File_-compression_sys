from pydub import AudioSegment
import numpy as np
import binascii

def audio_to_binary(audio_file):
    # Cargar el archivo de audio
    audio = AudioSegment.from_file(audio_file)
    
    # Aumentar la velocidad de reproducción del audio
    audio = audio.set_frame_rate(44100)  # Ajustar la frecuencia de muestreo según tus necesidades
    audio = audio.set_channels(1)        # Ajustar el número de canales según tus necesidades
    
    # Convertir el audio a binario
    return audio.raw_data

def binary_to_text(binary_data):
    return binascii.b2a_hex(binary_data).decode()

def text_to_binary(text_data):
    return binascii.a2b_hex(text_data.encode())

def binary_to_audio(binary_data, output_file):
    audio = AudioSegment(
        np.frombuffer(binary_data, dtype=np.int16).tobytes(),
        frame_rate=44100,  # Ajustar la frecuencia de muestreo según tus necesidades
        sample_width=2,    # Ajustar el ancho de muestra según tus necesidades
        channels=1         # Ajustar el número de canales según tus necesidades
    )
    audio.export(output_file, format="mp3", bitrate="192k")  # Ajustar la tasa de bits según tus necesidades

def save_binary_data_to_file(binary_data, output_file):
    with open(output_file, 'wb') as file:
        file.write(binary_data)

# Ejemplo de uso:
audio_file = "test.mp3"
output_audio_file = "output_audio.mp3"
output_file = "output_audio.bin"

# Convertir audio MP3 a binario
binary_data = audio_to_binary(audio_file)

# Convertir binario a texto
text_data = binary_to_text(binary_data)

# Convertir texto a binario
new_binary_data = text_to_binary(text_data)

save_binary_data_to_file(binary_data, output_file)
# Convertir binario a audio en formato MP3
binary_to_audio(new_binary_data, output_audio_file)
