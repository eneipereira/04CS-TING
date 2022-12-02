def get_occurences(word, items):
    ocurrences = []
    for index in range(len(items)):
        if word.lower() in items[index].lower():
            ocurrences.append({
                "linha": index + 1
            })
    
    return ocurrences
    
    
def exists_word(word, instance):
    dict_list_item = []

    for index in range(instance.__len__()):
        matched_item = instance.search(index)
        ocurrences_list = get_occurences(word, matched_item["linhas_do_arquivo"])
        
        if ocurrences_list:
            dict_list_item.append({
                "palavra": word,
                "arquivo": matched_item["nome_do_arquivo"],
                "ocorrencias": ocurrences_list
            })
        
    return dict_list_item
    
    


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
