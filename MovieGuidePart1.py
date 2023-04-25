# Thomas Careny
# CIS 261 - Object-Oriented Computer Programming
# Movie Guide Part 1

movies = []

def pre_pop():
    movies.append('Good Will Hunting')
    movies.append('O Brother, Where Art Thou?')
    movies.append('Pulp Fiction')

def show_commands():
    print('The Movie List program\n')
    print('COMMAND MENU')
    print('list - List all movies')
    print('add  - Add a movie')
    print('del  - Delete a movie')
    print('exit - Exit program')

def list(l):
    for pos, item in enumerate(l,1):
        print(f'{pos}. {item}')

def add(l, li):
    l.append(li)
    print(f'{li} was added.')

def delete(l, index):
    print(f'{l[index]} was delted.')
    l.pop(index)

def main():
    show_commands()
    pre_pop()
    command = ''
    while command != 'exit':
        command = input('\nCommand:  ').lower()
        if command == 'list':
            list(movies)
        elif command == 'add':
            title = input('Name/Title:  ')
            if len(title) > 0:
                add(movies, title)
            else:
                print('No input recieved.')
        elif command == 'del':
            index = int(input('Number:  ')) - 1
            if index in range(len(movies)):
                delete(movies, index)
            else:
                print('Invalid movie number.')
        elif command == 'exit':
            print('Goodbye!')
        else:
            print('Not a valid command.  Please try agian.')


            





if __name__ == "__main__":
    main()