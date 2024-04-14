def main_funct():
    print("ДОБРО ПОЖАЛОВАТЬ В ТЕЛ СПРАВОЧНИК!")
    menu = 1
    while menu != 0:
        print("ВЫБЕРИТЕ КОМАНДУ:\n 0 -- ЗАКОНЧИТЬ РАБОТУ\n 1 -- СОЗДАТЬ НОВЫЙ КОНТАКТ\n 2 -- НАЙТИ КОНТАКТ")
        menu = int(input())
        if menu == 1:
            write_contact(read_line())
        elif menu == 2:
            key = 0
            while key != 5: 
                print("Критерий поиска?:\n 5 - назад\n 0 - Имя\n 1 - Фамилия\n 2 - Отчество\n 3 - Телефон\n 4 - Все")
                key = int(input())
                if key == 4:
                    print("Имя\tФамилия\tОтчест\tТелефон")
                    print(read_data('data.txt'))
                elif key in [1, 2, 3, 0]:
                    #print(list_data(read_data('data.txt')))
                    data = list_data(read_data('data.txt'))
                    _keys = {0 : "Имя", 1:'Фамилия',2:'Отчество',3:"Номер телефона:"}
                    print(_keys[key])
                    data_c = cut_data(data, key)
                    _str = (input('введите поисковый запрос:'))
                    find_flag = [True  if _str in x else False for x in data_c]
                    print("Имя\tФамилия\tОтчест\tТелефон")
                    for i in range(len(data)):
                        if find_flag[i]:
                            print('\t'.join(data[i]))
                                                           
    return "Bye"
def merge_contact():
    return

def write_contact( contact ):
    """Функция принимает словарь и записывает его в файл
    data.txt"""
    _string = '\t'.join(contact)    
    with open('data.txt', 'a', encoding="utf-8") as f:
        f.write(_string+"\n")
                
def read_line():
    """Функция принимает контакт от пользователя
    и формирует его в список"""
    print("Введите данные: ")
    _fir_n = input('Имя:')
    _sec_n = input('Фамилия:')
    _fam_n = input("Отчество:")
    _phone = input("Номер телефона:")
    contact = [_fir_n, _sec_n, _fam_n ,_phone ]
    return contact

def cut_data( in_data , k):
    """Ф-я принимает базу контактов и изменят её
    поисковым запросом"""
    out_data = []
    for i in in_data:
        out_data.append(i[k])
        print(i[k])
    return out_data

def read_data( file ):
    """Функция читает принятый файл и возвращает
    контакты списком словарей
    """
    with open(file , 'r', encoding="utf-8") as f:
        _file_str = f.read()
        return _file_str


def list_data( income_data ):
    """Ф-я принимает базу контактов и изменят её
    поисковым запросом"""
    _data = list(income_data.split())
    _data[0] = _data[0][1:]         # отрезаем служебный символ в начале файла(толи из-за utf-8 толи ещё почему)
    count = 0
    new_data = []
    _string = []
    for i in _data:
        _string.append(i)
        count+=1
        if count == 4:
           count = 0
           new_data.append(_string)
           _string = []
    # list new_data
        
    return new_data
        
    
print(main_funct())
