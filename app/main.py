import sys  # Library for interacting with the system
import os  # Library for file system and environment variable handling
import subprocess  # Library for executing external commands

# Get the system's PATH environment variable and split it into a list of directories
path = os.environ.get('PATH')
path = path.split(":")

def pathExists(cmd):
    """
    Checks if the given command exists in any directory listed in the PATH.
    
    Args:
        cmd (str): The command to search for.

    Returns:
        str: The full path of the command if it exists, otherwise None.
    """
    for filePath in path:
        if os.path.exists(filePath + "/" + cmd):
            return filePath + "/" + cmd

def notFound(cmd):
    """
    Prints an error message indicating that the given command was not found.

    Args:
        cmd (str): The command that was not found.
    """
    print('{}: command not found'.format(cmd))

def echo(word):
    """
    Prints the given arguments as a single space-separated string.

    Args:
        word (list): The list of words to echo.
    """
    word = ' '.join(word)
    print(word)

def exit(number=None):
    """
    Exits the shell with an optional exit code.

    Args:
        number (list or None): The exit code to use. Defaults to None, which exits with code 0.
    """
    if number:
        number = ' '.join(number)
        sys.exit(int(number))  # Exit with the provided number as the code
    else:
        sys.exit()  # Exit with the default code (0)

def pwd():
    """
    Prints the current working directory.
    """
    print(os.getcwd())

def cd(dir):
    """
    Changes the current working directory.

    Args:
        dir (list): The directory to change to.
    """
    dir = ' '.join(dir)  # Convert the list of arguments to a single string
    home = os.environ.get('HOME')  # Get the user's home directory
    if dir == "~":  # If "~", change to the home directory
        os.chdir(home)
    elif os.path.exists(dir):  # If the directory exists, change to it
        os.chdir(dir)
    else:  # Otherwise, print an error message
        print("cd: {}: No such file or directory".format(dir))

def type(cmd):
    """
    Checks whether a command is a shell built-in or an external executable.

    Args:
        cmd (list): The command to check.
    """
    cmd = ' '.join(cmd)  # Convert the list of arguments to a single string
    if cmd in commands:  # If the command is in the built-in commands
       print('{} is a shell builtin'.format(cmd))
    elif exists := pathExists(cmd):  # If the command is an external executable
        print('{} is {}'.format(cmd, exists))
    else:  # If the command is neither built-in nor an external executable
        print('{}: not found'.format(cmd))

# Dictionary of built-in commands
commands = {"exit": exit, "echo": echo, "type": type, "pwd": pwd, "cd": cd}

def main():
    """
    Main function to run the custom shell. Continuously waits for user input, parses the command,
    and executes it as either a built-in or an external command.
    """
    while True:
        # Display the shell prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        user = input().strip()  # Strip leading/trailing whitespace

        # Skip processing if the input is empty
        if not user:
            continue

        # Split the input into the command and its arguments
        split_command = user.split()

        # Execute built-in commands with arguments
        if split_command[0] in commands and len(split_command) > 1:
            commands.get(split_command[0])(split_command[1:])
        # Execute built-in commands without arguments
        elif split_command[0] in commands and len(split_command) == 1:
            commands.get(split_command[0])()
        # Execute external commands with arguments
        elif (exists := pathExists(split_command[0])) and len(split_command) > 1:
            args = ' '.join(split_command[1:])  # Combine arguments into a single string
            subprocess.run([exists, args])  # Run the external command
        # Execute external commands without arguments
        elif (exists := pathExists(split_command[0])) and len(split_command) == 1:
            subprocess.run(exists)  # Run the external command
        else:
            # If the command is not found, print an error message
            notFound(split_command[0])

if __name__ == "__main__":
    main()  # Entry point for the shell
