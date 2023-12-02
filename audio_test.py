from pydub import AudioSegment
import base64

def audio_to_binary(audio_file):
    # Cargar el archivo de audio WAV
    audio = AudioSegment.from_file(audio_file, format="wav")
    audio = audio.set_frame_rate(44100)  # Ajustar la frecuencia de muestreo según tus necesidades
    audio = audio.set_channels(1) 
    # Convertir el audio a binario
    return audio.raw_data

def binary_to_text(binary_data):
    # Convertir los datos binarios a texto Base64
    return base64.b64encode(binary_data).decode()

def text_to_binary(text):
    # Convertir el texto Base64 a datos binarios
    return base64.b64decode(text)

def binary_to_audio(binary_data, output_audio_file):
    # Crear un nuevo objeto AudioSegment a partir de los datos binarios
    audio = AudioSegment(data=binary_data, sample_width=2, frame_rate=44100, channels=1)
    # Exportar el audio al archivo de salida
    audio.export(output_audio_file, format="wav",  bitrate="192k")
# Ejemplo de uso:
audio_file = "test.wav"
text_file = "output_text.txt"
output_audio_file = "output_audio.wav"

# Convertir audio WAV a binario
binary_data = audio_to_binary(audio_file)

# Convertir binario a texto ASCII
text_data = binary_to_text(binary_data)

# Guardar el texto en un archivo
with open(text_file, 'w') as file:
    file.write(text_data)

# Cargar texto de archivo
with open(text_file, 'r') as file:
    loaded_text_data = file.read()

# Convertir texto a binario
new_binary_data = text_to_binary(loaded_text_data)

# Convertir binario a audio WAV
binary_to_audio(new_binary_data, output_audio_file)
