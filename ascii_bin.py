def bin_to_ascii(message):
    #text = ""
    try:
       # with open("C:/Users/josec/OneDrive/Escritorio/Universidad/Semestre 4/Estructuras de datos II/Proyecto final/File_compression_sys/prueba.compress.txt", "r") as file:
            #text = file.read()
        num = ''
        ascii = ''
        for i in range(len(message)):
            if len(num) == 8:
                ascii += chr(int(num, 2))
                num = ''
            num += message[i]

        if len(num) > 0:
            ascii += chr(int(num, 2))
        print(ascii)
    except Exception as e:
        print("Error: " + str(e))

def ascii_to_bin(message):
    num_bin = ''
    for i in range(len(message)):
        num_bin += format(ord(message[i]), '08b')
    print(num_bin)

bin_to_ascii("0")
ascii_to_bin('\0')