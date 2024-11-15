# Build Your Own Shell

A custom-built shell implemented in Python, supporting built-in commands like `cd`, `pwd`, and `echo`, as well as execution of external commands. The shell dynamically resolves executable paths, handles errors gracefully, and provides an intuitive user experience for basic shell functionalities.

## Features

- **Built-in Commands**:
  - `cd <directory>`: Change the current working directory.
  - `pwd`: Display the current working directory.
  - `echo <message>`: Print the specified message to the console.
  - `type <command>`: Determine if the command is a built-in shell command or an external executable.
  - `exit`: Exit the shell.
- **External Command Execution**:
  - Executes any external commands available in the system’s `PATH`.
  - Dynamically resolves paths for executables.
- **Error Handling**:
  - Handles missing files or directories for commands like `cd`.
  - Displays appropriate error messages for unknown commands.
- **Environment Variable Parsing**:
  - Supports usage of user-defined environment variables like `~` for the home directory.
- **Path Searching**:
  - Searches through directories listed in the `PATH` environment variable to locate executables.

## Requirements

- Python 3.6+
- A Unix-like environment (Linux/Mac) or Windows with minimal adjustments.

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/Mohammed-Omair/Build-Your-Own-Shell-Python.git
cd Build-Your-Own-Shell-Python/app/
```

### Run the Shell
Start the shell by running:
```bash
python3 main.py

```
The shell will start and display a prompt (`$`). You can now enter commands.

## Usage
### Built-in Commands
#### 1. Print Working Directory (`pwd`)
```bash
$ pwd
```
Example Output:
```bash
/home/user/Build-Your-Own-Shell-Python/app
```

#### 2. Change Directory (`cd`)
```bash
$ cd <directory>

```
Example:
```bash
$ cd /tmp/

```

#### 3. Echo a Message (`echo`)
```bash
$ echo Hello, World!
```

#### 4. Check Command Type (`type`)
```bash
$ type echo
```
Example Output:
```bash
echo is a shell builtin
```

#### 5. Exit the shell (`exit`)
```bash
$ exit
```

### External Commands
Run any external command available in the system’s `PATH`. For example:
```bash
$ ls -l
$ python3 --version
```

### Error Handling
- Unknown commands will display an error:
```bash
command: not found
```

- If the target directory for `cd` does not exist:
```bash
cd: <directory>: No such file or directory
```
## How It Works

1. **Command Parsing**:
   - Splits the input into a command and its arguments.

2. **Built-in Command Handling**:
   - Matches the command against built-in commands and executes them directly.

3. **Path Resolution**:
   - For external commands, iterates through directories in `PATH` to locate the executable.

4. **Error Handling**:
   - Catches errors like invalid commands or inaccessible directories.

5. **Environment Variable Parsing**:
   - Expands user-specific shortcuts like `~` to the home directory.

## Limitations
- This shell is intended for educational purposes and basic testing.
- It lacks advanced features like piping (`|`), input/output redirection (`>`, `<`), and job control (`&`, `fg`, `bg`).
