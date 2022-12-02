import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)

    try:
        with open(path_file, "r") as file:
            read_file = file.read()
            file_lines_list = read_file.split("\n")

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

    else:
        return file_lines_list
