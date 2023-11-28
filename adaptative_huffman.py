import json
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
            left = nodes.pop(0)
            right = nodes.pop(0)
            parent = Node(None, left.weight + right.weight)
            parent.left, parent.right = left, right
            nodes.append(parent)

        self.root = nodes[0]

    def generate_code_table(self):
        self._generate_code_table(self.root, "")

    def _generate_code_table(self, node, prefix):
        if not node.left and not node.right:
            self.code_table[node.symbol] = prefix
            return

        if node.left:
            self._generate_code_table(node.left, prefix + "0")

        if node.right:
            self._generate_code_table(node.right, prefix + "1")

    def encode(self, symbols):
        return ''.join(self.code_table[symbol] for symbol in symbols)

def adaptive_huffman_encoding(text):
    tree = HuffmanTree()
    tree.build_tree(text)
    tree.generate_code_table()
    return tree.encode(text)

def decode(encoded_message, code_table):
    decoded_message = ""
    while encoded_message:
        for character, code in code_table.items():
            if encoded_message.startswith(code):
                decoded_message += character
                encoded_message = encoded_message[len(code):]
                break  # Agregamos un break para evitar comparaciones innecesarias
    return decoded_message

# Usage
text = "Hola como estas"
tree = HuffmanTree()
tree.build_tree(text)
tree.generate_code_table()

tree2 = json.dumps(tree.code_table)

encoded_text = adaptive_huffman_encoding(text)

aux = json.dumps(tree.code_table) + '|' + encoded_text
position = aux.find('|')
json_string, encoded_message = aux[:position], aux[position+1:]
code_table = json.loads(json_string)

binary = aux.encode("utf-8")
print(binary)

# Ahora puedes usar 'code_table' y 'encoded_message' para decodificar el mensaje
decoded_message = decode(encoded_message, code_table)
print(decoded_message)
