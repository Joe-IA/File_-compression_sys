import pickle
from bitarray import bitarray

class Node:
    def __init__(self, symbol, weight=1):
        self.symbol = symbol
        self.weight = weight
        self.left = None
        self.right = None

class HuffmanTree:
    def __init__(self):
        self.root = None
        self.code_table = {}

    def build_tree(self, symbols):
        symbol_counts = {}
        for symbol in symbols:
            symbol_counts[symbol] = symbol_counts.get(symbol, 0) + 1

        nodes = [Node(symbol, count) for symbol, count in symbol_counts.items()]

        while len(nodes) > 1:
            nodes.sort(key=lambda x: x.weight)
            left = nodes.pop(0)
            right = nodes.pop(0)
            parent = Node(None, left.weight + right.weight)
            parent.left = left
            parent.right = right
            nodes.append(parent)

        self.root = nodes[0]

    def generate_code_table(self):
        self.code_table = {}
        self._generate_code_table(self.root, bitarray())

    def _generate_code_table(self, node, current_code):
        if not node.left and not node.right:
            self.code_table[node.symbol] = current_code
            return

        if node.left:
            self._generate_code_table(node.left, current_code + bitarray([0]))

        if node.right:
            self._generate_code_table(node.right, current_code + bitarray([1]))

    def encode(self, symbols):
        encoded_bits = bitarray()
        for symbol in symbols:
            encoded_bits.extend(self.code_table[symbol])

        return encoded_bits

class Encoding:
    def adaptive_huffman_encoding(self, text):
        if not text:
            return bitarray(), {}

        tree = HuffmanTree()
        tree.build_tree(text)
        tree.generate_code_table()

        encoded_text = tree.encode(text)
        return encoded_text, tree.code_table

    def decode(self, encoded_bits, code_table):
        decoded_message = ""
        temp_code = bitarray()
        
        for bit in encoded_bits:
            temp_code.append(bit)
            matching_symbols = [symbol for symbol, code in code_table.items() if temp_code == code]
            
            if matching_symbols:
                decoded_message += matching_symbols[0]
                temp_code = bitarray()

        return decoded_message

def save_to_file(filename, data):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def load_from_file(filename):
    with open(filename, 'rb') as file:
        data = pickle.load(file)
    return data

if __name__ == "__main__":
    with open("output_text.txt", 'r') as file:
        text = file.read()

    encoded_text, code_table = Encoding().adaptive_huffman_encoding(text)
    save_to_file('compressed_data.bin', (encoded_text, code_table))

    loaded_data = load_from_file('compressed_data.bin')
    loaded_encoded_text, loaded_code_table = loaded_data

    decoded_message = Encoding().decode(loaded_encoded_text, loaded_code_table)
    print(decoded_message)
