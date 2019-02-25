first_side = int(input('Enter an integer as a side of tringle: '))
second_side = int(input('Enter an integer as a side of tringle: '))
third_side = int(input('Enter an integer as  a side of tringle: '))

def is_triangle(a, b, c):
    if ((a > (b + c)) or  (b > (a +c)) or (c > (a +b))):
        print("No")         
    else:
        print("yes")
        

is_triangle(first_side, second_side, third_side)
