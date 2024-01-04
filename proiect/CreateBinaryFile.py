import sys

def create_binary_file(file_path_content):
    with open(file_path_content, 'r') as input_file:
        # Citirea continutului fisierului
        text_content = input_file.read()

    # Crearea unui nou fisier cu extensia .bin
    file_path = file_path_content[:-4] + "_binary.bin"

    with open(file_path, 'wb') as output_file:
        # Codificarea textului în bytes si scrierea in fisierul binar
        output_file.write(text_content.encode('utf-8'))


def main():
    if len(sys.argv) < 2:
        print("Usage: python CreateBinaryFile.py file_path_content")
    else:
        file_path_content = sys.argv[1]
        create_binary_file(file_path_content)


if __name__ == '__main__':
    main()
