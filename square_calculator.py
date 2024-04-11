def main():
    data = int(input("Input a number: "))
    print(f"Square of {data} is {square_multiplication(data)}")


def square_multiplication(n):
    square = int(n) * int(n)
    return square


if __name__ == "__main__":
    main()
