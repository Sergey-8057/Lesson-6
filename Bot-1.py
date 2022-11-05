CONTACTS = {}

def corrector(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except KeyError:
            return 'Wrong name'
        except ValueError as exception:
            return exception.args[2]
        except IndexError:
            return 'Please print: name and number'
        except TypeError:
            return 'Wrong command.'
    return wrapper

def hello_func():
    print('How can I help you?')

@corrector
def add_contact(name, phone):
    name = name.title()
    CONTACTS[name] = phone

@corrector
def change_contact(name, phone):
    name = name.title()
    CONTACTS[name] = phone

@corrector
def find_contact(name):
    name = name.title()
    return name, CONTACTS[name]
    
def show_all_func():
    for key,value in CONTACTS.items():
        print(key, ':', value)

def quit_func():
    print('Good bay!')
    quit()

COMMANDS = {
    'hello': hello_func,
    'show all': show_all_func,
    'good bye': quit_func,
    'close': quit_func,
    'exit': quit_func   
    }

def main():
    while True:
        var = input('Enter command: ')
        var = var.lower()
        if var[0:3] == 'add':
            var = var.split(' ')
            add_contact(var[1], var[2])
            print('New contact addend!')
            continue
        if var[0:6] == 'change':
            var = var.split(' ')
            change_contact(var[1], var[2])
            print(f'Contact {var[1]} changed')
            continue
        if var[0:5] == 'phone':
            var = var.split(' ')
            print(find_contact(var[1]))
            continue
        if var not in COMMANDS:
            print('Wrong command')
            continue
        COMMANDS[var]()
    
if __name__ == "__main__":
    main()
