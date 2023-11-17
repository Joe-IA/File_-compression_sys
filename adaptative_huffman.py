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
        decoded_symbols = []
        current_node = self.root

        for bit in encoded_symbols:
            if bit == "0":
                current_node = current_node.left
            elif bit == "1":
                current_node = current_node.right
            else:
                raise ValueError("Invalid bit: " + bit)

            if not current_node.left and not current_node.right:
                decoded_symbols.append(current_node.symbol)
                current_node = self.root

        return decoded_symbols

def adaptive_huffman_encoding(symbols):
    tree = HuffmanTree()
    tree.build_tree(symbols)
    tree.generate_code_table()

    encoded_symbols = tree.encode(symbols)
    return encoded_symbols

def adaptive_huffman_decoding(encoded_symbols):
    tree = HuffmanTree()
    return tree.decode(encoded_symbols)


symbols = ['h', "o", "l", 'a', " ","c", "o", "m", "o", "e", "s", "t", "a", "s" ]
tree = HuffmanTree()
tree.build_tree(symbols)
tree.generate_code_table()

encoded_symbols = tree.encode(symbols)
print(encoded_symbols)

decoded_symbols = tree.decode(encoded_symbols)
print(decoded_symbols)
