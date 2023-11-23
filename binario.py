#with open("prueba.txt", "w") as f:
 #   for i in range(100):
  #      f.write(chr(0))

with open("prueba.txt", "r") as f:
    text = f.read()

print(len(text))