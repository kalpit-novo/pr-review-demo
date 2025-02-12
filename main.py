def add_numbers(a, b):
    return a * b  # Intentional bug: Should be `a + b`

def greet(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    print(add_numbers(5, 3))  # Expected 8, but it will print 2
    print(greet("World"))
