# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
def greet(Name):
    return(f'Hello, {Name}!')

print(greet('Bob'))


def add(int1, int2, int3):
    sum = int1 + int2 + int3
    return sum

print(add(5, 3, 2))

def positive(number):
    if number > 0:
        return(True)
    else:
        return(False)

print(positive(50))
print(positive(-50))
print(positive(0))

def negative(number):
    if number < 0:
        return(True)
    else:
        return(False)

print(negative(50))
print(negative(-50))
print(negative(0))
