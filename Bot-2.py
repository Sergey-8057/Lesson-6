from collections import UserDict


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone = None):
        self.value = phone.split(' ')

    
class AddressBook(UserDict):
    def add_record(self):
        self.name = Name(input('Enter name: '))
        self.phone = Phone(input('Enter phone: '))
        record = Record(name=self.name.value, phone=self.phone.value).add()
        print('New contact added!')

    def remove_contact(self):
        self.name = Name(input('Enter name: '))
        record = Record(name=self.name.value, phone=self.phone.value).remove()
        print('Contact removed!')

    def change_contact(self):
        self.name = Name(input('Enter name: '))
        self.phone = Phone(input('Enter new phone: '))
        record = Record(name=self.name.value, phone=self.phone.value).change()
        print('Contact changed!')

    def find_phone(self):
        self.name = Name(input('Enter name: '))
        record = Record(name=self.name.value, phone=self.phone.value).find()
        print('Contact found!')

    def show_all(self):
        print(self.data)
    

class Record:
    def __init__(self, name, phone):
        self.name = name.title()
        self.phone = phone

    def add(self):
        book[self.name] = self.phone

    def remove(self):
        del book[self.name]

    def change(self):
        book[self.name] = self.phone

    def find(self):
        print(book[self.name])

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
