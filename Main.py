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
        self.text = None
        self.path = None

    def set_text(self, path):
        self.path = path
        with open(self.path, "r") as file:
            self.text = file.read()
        
    def build_tree(self):
        symbol_counts = {}
        for symbol in self.text:
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
    
    def encode(self):
        encoded_symbols = ""
        for symbol in self.text:
            encoded_symbol = self.code_table[symbol]
            encoded_symbols += encoded_symbol

        return encoded_symbols

    def decode(self):
        decoded_symbols = []
        current_node = self.root

        for bit in self.text:
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
    
    def encoding(self):
        self.build_tree()
        self.generate_code_table()

        encoded_text = self.encode()
        path = self.path[:-3] + "compress.txt"
        with open(path, "w") as file:
            file.write(encoded_text)
    
    def decoding(self):
        decoded_text = self.decode()
        text = ""
        for i in decoded_text:
            text += i
        path = self.path[:-13] + "2.txt"
        with open(path, "w") as file:
            file.write(text)

    
hm = HuffmanTree()
hm.set_text("C:/Users/josec/OneDrive/Escritorio/Universidad/Semestre 4/Estructuras de datos II/Proyecto final/File_compression_sys/prueba.txt")
code = hm.encoding()
hm.set_text("C:/Users/josec/OneDrive/Escritorio/Universidad/Semestre 4/Estructuras de datos II/Proyecto final/File_compression_sys/prueba.compress.txt")
hm.decoding()