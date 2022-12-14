import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    ins_length = instance.__len__()

    for index in range(ins_length):
        enqueued_file = instance.search(index)
        if enqueued_file["nome_do_arquivo"] == path_file:
            return print(f"Arquivo {path_file} já existe na fila, tente outro")

    file_list = txt_importer(path_file)
    queue_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_list),
        "linhas_do_arquivo": file_list,
    }
    instance.enqueue(queue_dict)
    return print(queue_dict, file=sys.stdout)


def remove(instance):
    dequeued_item = instance.dequeue()

    if dequeued_item is None:
        return print("Não há elementos", file=sys.stdout)

    path_file = dequeued_item["nome_do_arquivo"]

    return print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        matched_item = instance.search(position)
    except IndexError:
        return print("Posição inválida", file=sys.stderr)
    else:
        return print(matched_item, file=sys.stdout)
