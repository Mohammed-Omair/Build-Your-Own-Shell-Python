import sys


def main():
    while (True):
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        user = input()
        if user == "exit 0":
            break
        print('{}: command not found'.format(user))


if __name__ == "__main__":
    main()
