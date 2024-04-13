def main_funct():
    print("ДОБРО ПОЖАЛОВАТЬ В ТЕЛ СПРАВОЧНИК!")
    menu = 1
    while menu != 0:
        print("ВЫБЕРИТЕ КОМАНДУ:\n 0 -- ЗАКОНЧИТЬ РАБОТУ\n 1 -- СОЗДАТЬ НОВЫЙ КОНТАКТ\n 2 -- НАЙТИ КОНТАКТ")
        menu = int(input())
        if menu == 1:
            write_contact(read_line())
        elif menu == 2:
            return
    return "Bye"


def write_contact( contact ):
    """Функция принимает словарь и записывает его в файл
    data.txt"""
    _string = str(contact)
    print(_string)
            
    with open('data.txt', 'a', encoding="utf-8") as f:
        f.write(_string+"\n")
                
def read_line():
    """Функция принимает контакт от пользователя
    и формирует его в словарь"""
    print("Введите данные: ")
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

print(main_funct())
