import pickle
from bitarray import bitarray
from pydub import AudioSegment
import base64

"""
Classes
Node and HuffmanTree build the huffman tree and generate the code table for the symbols. It uses the adaptive huffman algorithm to build the tree.

Encoding class:
    In charge of encoding and decoding the text using the huffman tree and code table.

AudioProcessor class:
    In charge of converting the audio to binary and viceversa.
    
"""

class Node:
    def __init__(self, symbol, weight=1, left=None, right=None):
        self.symbol = symbol
        self.weight = weight
        self.left = left
        self.right = right

class HuffmanTree:
    def __init__(self):
        self.root = None
        self.code_table = {}

    def build_tree(self, symbols):
        from collections import Counter

        symbol_counts = Counter(symbols)
        nodes = [Node(symbol, count) for symbol, count in symbol_counts.items()]

        while len(nodes) > 1:
            nodes.sort(key=lambda x: x.weight)
            left, right = nodes.pop(0), nodes.pop(0)
            parent = Node(None, left.weight + right.weight, left, right)
            nodes.append(parent)

        self.root = nodes[0]

    def generate_code_table(self):
        def _generate_code_table(node, current_code):
            if not node.left and not node.right:
                self.code_table[node.symbol] = current_code
                return
            if node.left:
                _generate_code_table(node.left, current_code + bitarray([0]))
            if node.right:
                _generate_code_table(node.right, current_code + bitarray([1]))

        self.code_table = {}
        _generate_code_table(self.root, bitarray())

    def encode(self, symbols):
        encoded_text = bitarray()
        for symbol in symbols:
            encoded_text.extend(self.code_table[symbol])
        return encoded_text

class Encoding:
    def __init__(self):
        self.huffman_tree = HuffmanTree()

    def adaptive_huffman_encoding(self, text):
        if not text:
            return bitarray(), {}

        self.huffman_tree.build_tree(text)
        self.huffman_tree.generate_code_table()

        encoded_text = self.huffman_tree.encode(text)
        return encoded_text, self.huffman_tree.code_table

    def decode(self, encoded_bits, code_table):
        decode_tree = {str(v): k for k, v in code_table.items()}
        decoded_message, temp_code = "", bitarray()

        for bit in encoded_bits:
            temp_code.append(bit)
            if str(temp_code) in decode_tree:
                decoded_message += decode_tree[str(temp_code)]
                temp_code = bitarray()

        return decoded_message

    @staticmethod
    def save_to_file(filename, data):
        with open(filename, 'wb') as file:
            pickle.dump(data, file)

    @staticmethod
    def load_from_file(directory, filename):
        with open(f"{directory}/{filename}", "rb") as file:
            loaded_data = pickle.load(file)
        return loaded_data

    @staticmethod
    def save_decoded_message_to_file(decoded_message, filename):
        try:
            with open(filename, 'w') as file:
                file.write(decoded_message)
            print(f"Archivo guardado con éxito en {filename}")
        except IOError as e:
            print(f"Error al guardar el archivo: {e}")

class AudioProcessor:
    @staticmethod
    def audio_to_binary(audio_file):
        audio = AudioSegment.from_file(audio_file, format="wav").set_frame_rate(44100).set_channels(1)
        return audio.raw_data

    @staticmethod
    def binary_to_text(binary_data):
        return base64.b64encode(binary_data).decode()

    @staticmethod
    def text_to_binary(text):
        return base64.b64decode(text)

    @staticmethod
    def binary_to_audio(binary_data,  path):
        AudioSegment(data=binary_data, sample_width=2, frame_rate=44100, channels=1).export(path, format="wav", bitrate="192k")

    def process_audio_to_text(self, directory, input_audio_file, compressed_data_file):
        print("Comprimiendo...")
        encoding_instance = Encoding()  # Definir encoding_instance aquí

        binary_data = self.audio_to_binary(f"{directory}/{input_audio_file}")
        text_data = self.binary_to_text(binary_data)
        encoded_text, code_table = encoding_instance.adaptive_huffman_encoding(text_data)

        # Guardar datos comprimidos y árbol Huffman en archivos binarios
        Encoding.save_to_file(f"{directory}/{compressed_data_file}", (encoded_text, code_table, encoding_instance.huffman_tree))
        
    def process_text_to_audio(self, directory, input_text_file, output_audio_file):
        print("Descomprmiendo...")
        # Cargar los datos comprimidos y el árbol Huffman desde el archivo binario
        encoded_text, code_table, huffman_tree = Encoding.load_from_file(directory, input_text_file)

        # Decodificar el texto
        decoding_instance = Encoding()
        decoded_text = decoding_instance.decode(encoded_text, code_table)

        # Convertir el texto a datos binarios
        binary_data = self.text_to_binary(decoded_text)

        # Convertir los datos binarios a audio y guardarlos en un archivo
        self.binary_to_audio(binary_data, f"{directory}/{output_audio_file}")


if __name__ == "__main__":
    encoding_instance = Encoding()
    audio_processor = AudioProcessor()

    input_audio_file, compressed_data_file, output_audio_file = "test.wav", "compressed_data.bin", "output_audio.wav"

    # Procesar de audio a texto (compresión)
    audio_processor.process_audio_to_text("/Users/atzincruz/Documents/carpeta sin título/Semestre_3_EDA/Proyecto_final/Pruebas",input_audio_file,compressed_data_file)
    
    audio_processor.process_text_to_audio("/Users/atzincruz/Documents/carpeta sin título/Semestre_3_EDA/Proyecto_final/Pruebas", compressed_data_file, output_audio_file)
