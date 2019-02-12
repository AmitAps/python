

def main():
    i = get_positive_int("Positive integer: ")
    print(i)

def get_positive_int(prompt):
    while True:
        n = int(input(prompt))
        if n > 0:
            break
    return n


if __name__ == "__main__":
    main()


