def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def main():
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))

    print(f"Sum: {add(a,b)}")
    print(f"Difference: {sub(a,b)}")
    print(f"Product: {mul(a,b)}")
    print(f"Quotient: {div(a,b)}")

if __name__ == "__main__":
    main()