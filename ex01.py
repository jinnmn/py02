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
                print("Критерий поиска?:\n 5 - назад\n 0 - Имя\n 1 - Фамилия\n 2 - Отчество\n 3 - Телефон)\n 4 - Все")
                key = int(input())
                if key == 4:
                    print("Имя Фамилия Отчество Телефон")
                    print(read_data('data.txt'))
                elif key in [1, 2, 3, 0]:
                    print("Имя Фамилия Отчество Телефон")
                    print(find_data(read_data('data.txt'), key))
    return "Bye"


def write_contact( contact ):
    """Функция принимает словарь и записывает его в файл
    data.txt"""
    _string = ' '.join(contact)
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
    contact = [_fir_n, _sec_n, _fam_n ,_phone ]
    return contact

def read_data( file ):
    """Функция читает принятый файл и возвращает
    контакты списком словарей
    """
    with open(file , 'r', encoding="utf-8") as f:
        _file_str = f.read()
        return _file_str


def find_data( income_data , key):
    """Ф-я принимает базу контактов и изменят её
    поисковым запросом"""
    
print(main_funct())
