def file_to_text(route):
    with open(route, "rb") as f:
        read_text = f.read()
    text = read_text.decode("latin-1")
    print(text)


if __name__ == "__main__":
    file_to_text("imagen1.bmp")