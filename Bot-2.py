from collections import UserDict


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone = None):
        self.value = phone


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    def __init__(self, new_name):
        self.name = Name(new_name)
        self.phones = []

    def add_phone(self, new_phone):        
        self.phones.append(Phone(new_phone))

    def change_phone(self, old_phone, new_phone):        
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.add_phone(new_phone)
                self.phones.remove_phone(phone)
            else:
                print("Phone number doesn't exist")  

    def remove_phone(self, old_phone):        
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.remove(phone)
            else:
                print("Phone number does't exist")

    def __repr__(self):        
        return f'{self.phones}'



book = AddressBook()

def get_user_input():
    user_input = input('Enter command: ').lower().split(' ')
    return user_input


def get_handler(command):
    return COMMANDS[command]


def add_func(user_input):
    if user_input[1] not in book.data:
        add_record = Record(user_input[1])
        add_record.add_phone(user_input[2])
        book.add_record(add_record)
        print(f'New contact added')
    else:
        add_phone = book.data[1]
        add_phone.add_phone(user_input[2])
        print(f'New phone number has been added')


def change_func(user_input):
    if user_input[1] in book.data:
        old_phone = input('Enter phone number to change: ')
        renew_phone = book.data[user_input[1]]
        renew_phone.change_phone(old_phone, user_input[2])
        print(f'Phone number has been changed')
    else:
        print(f"Phone number doesn't exist")


def delete_func(user_input):
    if user_input[1] in book.data:
        book.data.pop(user_input[1])
        print(f'Contact has been deleted')


def remove_phone_func(user_input):
     if user_input[1] in book.data:
        removing = book.data[user_input[1]]
        removing.remove_phone(user_input[2])
        print('Phone number has been removed')


def phone_func(user_input):
    if user_input[1] in book.data:
        print(f'{user_input[1]} has {book.data[user_input[2]]} phone number')
    else:
        print('This contact does not exist.')


def hello_func(*args):
     print('How can I help you?')
    


def show_all_func(*args):
    
    print(book.data)


def quit_func():
    print(result = 'Good bay!')
    return result


COMMANDS = {
    'hello': hello_func,
    'add': add_func,
    'change': change_func,
    'phone': phone_func,
    'delete': delete_func,
    'remove': remove_phone_func,
    'show all': show_all_func,
    'good bye': quit_func,
    'close': quit_func,
    'exit': quit_func
}

def main():
    print('How can I help you?')
    while True:
        user_input = get_user_input()

        if user_input == ['']:
            continue
        elif user_input[0] == 'show':
            command = 'show all'
        else:
            command = user_input[0]

        handler = get_handler(command)
        if handler is None:
            continue

        result = handler(user_input)
        if result == 'Good bay!':
            break


if __name__ == '__main__':
    main()
