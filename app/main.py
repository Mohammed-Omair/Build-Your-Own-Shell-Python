import sys
import os

path = os.environ.get('PATH')
path = path.split(":")
def notFound(cmd):
    print('{}: command not found'.format(cmd))

def echo(word):
    word = ' '.join(word)
    print(word)

def exit(number):
    number = ' '.join(number)
    sys.exit()

def type(cmd):
    cmd = ' '.join(cmd)
    if cmd in commands:
       print('{} is a shell builtin'.format(cmd))
    else:
        found = False
        for filePath in path:
            if os.path.exists(filePath + cmd):
                print('{} is {}'.format(cmd, filePath + cmd))
                found = True
                break
        if not found:
            print('{}: not found'.format(cmd))

commands = {"exit": exit, "echo": echo, "type": type}
def main():
    while (True):
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        user = input()

        # List of commands
        

        # splitting the whole command into the main commands and its flags
        split_command = user.split()

        if split_command[0] in commands and len(split_command) > 1:
            commands.get(split_command[0])(split_command[1:])
        elif split_command[0] in commands and len(split_command) == 1:
            commands.get(split_command[0])()
        else:
            #print('{}: command not found'.format(user))
            notFound(split_command[0])



if __name__ == "__main__":
    main()
