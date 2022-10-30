count = 0
def dict_(str_):
    str_1 = "".join(str_.split())
    str_2 = str_1.lower()
    str_3 = list(str_2)
    list_ = []
     for char_ in str_3:
        if char_.isalpha():
            list_[char_3] += 1
        else:
            list_[char_3] = 1
    dict_ = {}
    for key in list_:
        dict_[key] = dict_.get(key, count) + 1
    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(dict_(str_))
