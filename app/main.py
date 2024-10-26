import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    user = input()
    print('{}: command not found'.format(user))


if __name__ == "__main__":
    main()
