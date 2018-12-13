# Simple fizz buzz program

def fizzBuzz(num):
    try:
        float(num)
    except ValueError:
        raise ValueError("This is not an integer.")
    if float(num) != int(float(num)):
        raise ValueError("This is not an integer.")
    num = int(num)
    if num % 3 == 0:
        if num % 5 == 0:
            return "Fizz Buzz"
        else:
            return "Fizz"
    if num % 5 ==0:
        return "Buzz"
    return num

# if __name__ == "__main__":
#     for i in range(20):
#         print(fizzBuzz(i))
#     print("What does fizzBuzz to do '1.1'?")
#     fizzBuzz(1.1)
#     print("What does fizzBuzz to do 'a'?")
#     fizzBuzz("a")
