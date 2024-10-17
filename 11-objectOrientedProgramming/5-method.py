def my_decorator(func):
    def wrapper() :
        print("Sebelum fungsi dieksekusi")
        func()
        print("Setelah fungsi dieksekusi")
    return wrapper

# Dekorasi fungsi dengan decorator
@my_decorator
def say_hello() :
    print("Hello, world!")

# Memanggil fungsi yang sudah didekorasi
say_hello()

"""
Output:
Sebelum fungsi dieksekusi
Hello, world!
Setelah fungsi dieksekusi

"""