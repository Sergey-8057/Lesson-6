from collections import UserDict
from datetime import datetime

class Field:
    pass

class Name(Field):
    def __init__(self, name):
        self.__value = None
        self.value = name

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if len(value) > 2:
            self.__value = value
        else:
            print('Name too short, min 3 letters')
            book.add_record()

class Phone(Field):
    def __init__(self, phone = None):
        self.__value = None
        self.value = phone

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value.isdigit():
            self.__value = new_value
        else:
            print('Phone number is digits')
           

class Birthday(Field):
    def __init__(self, birthday = None):
        self.value = birthday

    
class AddressBook(UserDict):
    def add_record(self):
        self.name = Name(input('Enter name: '))
        self.phone = Phone(input('Enter phone: '))
        self.birthday = Birthday(input('Enter birthday "year-month-day": '))
        record = Record(name=self.name.value, phone=self.phone.value, birthday=self.birthday.value)
        record.add()
        print('New contact added!')

    def remove_contact(self):
        self.name = Name(input('Enter name: '))
        record = Record(name=self.name.value, phone=self.phone.value, birthday=self.birthday.value)
        record.remove()
        print('Contact removed!')

    def change_contact(self):
        self.name = Name(input('Enter name: '))
        self.phone = Phone(input('Enter new phone: '))
        record = Record(name=self.name.value, phone=self.phone.value, birthday=self.birthday.value)
        record.change()
        print('Contact changed!')

    def find_phone(self):
        self.name = Name(input('Enter name: '))
        record = Record(name=self.name.value, phone=self.phone.value, birthday=self.birthday.value)
        record.find()
        print('Contact found!')

    def show_all(self):
        self.count = input('Enter count: ')
        interable = Iterable(list_data=self.data, count=self.count,)
        print(interable)
        
    def birthday_day(self):
        self.name = Name(input('Enter name: '))
        record = Record(name=self.name.value, phone=self.phone.value, birthday=self.birthday.value)
        record.days_to_birthday()


class Iterable:
    def __init__(self, list_data, count = int):
        self.page_size = count
        self.offset = 0
        self.list_data = list_data

    def __next__(self):
        end_value = self.offset + self.page_size
        page = self.list_data[self.offset:end_value]
        self.offset = end_value
        if self.offset > self.iterable:
            raise StopIteration

    def __iter__(self):
        return page    

class Record:
    def __init__(self, name, phone, birthday):
        self.name = name.title()
        self.phone = phone.split(' ')
        self.birthday = birthday

    def add(self):
        book[self.name] = self.phone
        if self.birthday != '':
            data_birthday = datetime.strptime(self.birthday, '%Y-%m-%d')
            data_birthday = datetime.date(data_birthday)
            self.phone.append(data_birthday)
        
    def remove(self):
        del book[self.name]

    def change(self):
        book[self.name] = self.phone

    def find(self):
        print(book[self.name])

    def days_to_birthday(self):
        data = book[self.name]
        if data[-1] != '':
            current_date = datetime.now()
            x = datetime.now()
            y = str(x.year)
            m = str(data[-1].month)
            d = str(data[-1].day)
            new_data = str(y + m + d)
            new_data = datetime.strptime(new_data, '%Y%m%d')
            delta = new_data - current_date
            print(f'Birthday in {delta}!')
            return
        print('Birthday not entered!')
        
    

def hello_func():
    print('How can I help you?')

def quit_func():
    print('Good bay!')
    quit()


book = AddressBook()

def main():
    commands = {
        'hello': hello_func,
        'add': book.add_record,
        'remove': book.remove_contact,
        'change': book.change_contact,
        'phone': book.find_phone,
        'show all': book.show_all,
        'birthday': book.birthday_day,
        'good bye': quit_func,
        'close': quit_func,
        'exit': quit_func 
        }

    while True:
        var = input('Enter commad: ')
        var = var.lower()
        if var not in commands:
            print('Wrong command')
            continue
        commands[var]()

if __name__ == '__main__':
    main()
