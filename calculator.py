import argparse

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def main():
    parser = argparse.ArgumentParser(description="Operations to perform.")

    parser.add_argument('--add', '-a', action='store_true')
    parser.add_argument('--sub', '-s', action='store_true')
    parser.add_argument('--mul', '-m', action='store_true')
    parser.add_argument('--div', '-d', action='store_true')

    # Execute the parse_args() method
    args = parser.parse_args()

    a = int(input("Enter A: "))
    b = int(input("Enter B: "))

    if args.add:
        print(f"Sum: {add(a,b)}")

    if args.sub:
        print(f"Difference: {sub(a,b)}")

    if args.mul:
        print(f"Product: {mul(a,b)}")

    if args.div:
        print(f"Quotient: {div(a,b)}")

if __name__ == "__main__":
    main()