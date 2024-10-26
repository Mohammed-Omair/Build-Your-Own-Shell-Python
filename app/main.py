import sys


def main():
    while (True):
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        user = input()

        # List of commands
        commands = {"exit": exit, "echo": echo}

        # splitting the whole command into the main commands and its flags
        split_command = user.split()

        if split_command[0] in commands and len(split_command) > 1:
            commands.get(split_command[0])(split_command[1:])
        elif split_command[0] in commands and len(split_command) == 1:
            commands.get(split_command[0])()
        else:
            print('{}: command not found'.format(user))

def echo(word):
    word = ' '.join(word)
    print(word)

def exit(number):
    number = ' '.join(number)
    sys.exit()

if __name__ == "__main__":
    main()
