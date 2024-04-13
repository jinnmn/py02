#def menu?

def write_contact( contact ):
    """Функция принимает словарь и записывает его в файл
    data.txt"""
    _string = str(contact)
    print(_string)
            
    with open('data.txt', 'a') as f:
        f.write(_string+"\n")
                
def read_line( ):
    """Функция принимает контакт от пользователя
    и формирует его в словарь"""
    _fir_n = input('Имя:')
    _sec_n = input('Фамилия:')
    _fam_n = input("Отчество:")
    _phone = input("Номер телефона:")
    contact = {"Имя" : _fir_n, "Фамилия": _sec_n, "Отчество" : _fam_n ,"Номер телефона" : _phone }
    return contact

def read_data( file ):
    """Функция читает принятый файл и возвращает
    контакты списком словарей
    """
    return NULL

def print_data( data ):
    """Ф-я принимает список словарей контактов и выодит
    в консоль"""
    return NULL

def find_data( income_data, key ):
    """Ф-я принимает базу контактов и изменят её
    поисковым запросом"""
    return NULL

write_contact(read_line())
