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
            if symbol not in symbol_counts:
                symbol_counts[symbol] = 0
            symbol_counts[symbol] += 1

        nodes = []
        for symbol, count in symbol_counts.items():
            node = Node(symbol, count)
            nodes.append(node)

        while len(nodes) > 1:
            left = nodes.pop(0)
            right = nodes.pop(0)
            parent = Node(None, left.weight + right.weight)
            parent.left = left
            parent.right = right
            nodes.append(parent)

        self.root = nodes[0]

    def generate_code_table(self):
        self.code_table = {}
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
        encoded_symbols = ""
        for symbol in symbols:
            encoded_symbol = self.code_table[symbol]
            encoded_symbols += encoded_symbol

        return encoded_symbols

    def decode(self, encoded_symbols):
        decoded_text = ""
        current_node = self.root

        for bit in encoded_symbols:
            if bit == "0":
                current_node = current_node.left
            elif bit == "1":
                current_node = current_node.right
            else:
                raise ValueError("Invalid bit: " + bit)

            if not current_node.left and not current_node.right:
                decoded_text += current_node.symbol
                current_node = self.root

        return decoded_text

def adaptive_huffman_encoding(text):
    tree = HuffmanTree()
    tree.build_tree(text)
    tree.generate_code_table()

    encoded_text = tree.encode(text)
    return encoded_text

def adaptive_huffman_decoding(tree, encoded_text):
    return tree.decode(encoded_text)

# Usage
text = "Hola como estas"
tree = HuffmanTree()
tree.build_tree(text)
tree.generate_code_table()

encoded_text = adaptive_huffman_encoding(text)
print(encoded_text)

decoded_text = adaptive_huffman_decoding(tree, encoded_text)
print(decoded_text)
