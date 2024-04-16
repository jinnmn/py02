def main_funct():
    print("ДОБРО ПОЖАЛОВАТЬ В ТЕЛ СПРАВОЧНИК!")
    menu = 1
    while menu != 0:
        print("ВЫБЕРИТЕ КОМАНДУ:\n 0 -- ЗАКОНЧИТЬ РАБОТУ\n 1 -- СОЗДАТЬ НОВЫЙ КОНТАКТ\n 2 -- НАЙТИ КОНТАКТ\n 3 -- ПРИНЯТЬ ФАЙЛ")
        menu = int(input())
        if menu == 1:
            write_contact(read_line())
        elif menu == 2:
            key = 0
            while key != 5: 
                print("Критерий поиска?:\n 5 - Nазад\n 0 - Имя\n 1 - Фамилия\n 2 - Отчество\n 3 - Телефон\n 4 - Все")
                key = int(input())
                if key == 4:
                    print("Имя\tФамилия\tОтчест\tТелефон")
                    print(read_data('data.txt'))
                elif key in [1, 2, 3, 0,]:
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
                if key != 5: input('...')
        elif menu == 3:
             merge_menu()
    return "Bye"

 
def merge_menu():
    menu = 1
    file_name = input('Введите файл:/')
    try:
        with open(file_name, 'r', encoding="utf-8") as f:
            _file_str = f.read()
        _data = list_data(read_data(file_name))
        print('Файл:\n',_file_str)
        merge( _data  )
        
    except:
        print('Ошибка')



def merge(new_data):
    print(f'Обнаружено {len(new_data)} контактов')
    _ind = input('Введите индексы контактов для добавления через пробел или all\n')
    with open('data.txt', 'a', encoding="utf-8") as f:
        if _ind == "all":
            _ind = [10**6]
        else:
            _ind = list(map(int, _ind.split()))            
        for i in range(len(new_data)):
            if i in _ind or _ind[0]== 10**6:
                write_contact(new_data[i])    
                
       
def write_contact( contact ):
    """Функция принимает контакт и записывает его в файл
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
    контакты списком 
    """
    with open(file , 'r', encoding="utf-8") as f:
        _file_str = f.read()
        return _file_str


def list_data( income_data ):
    """Ф-я принимает базу контактов """
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
