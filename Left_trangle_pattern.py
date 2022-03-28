# Left triangle star pattern

def Lft_Sqaure_patttern(num):
    for i in range(1, num+1):
        print("*" * i)

    print("'")

def Left_triangle(num):   
    # Left triangle star pattern
    for i in range(1, num+1):
        print(" " * (num - i) + "*" * i)   

    print("'")

def downward_triangle(num):
    # downward triangle star pattern
    for i in range(num):
        print('*' * (num - i))   

def hollow_triangle(num):
    # hollow triangle star pattern
    print()
    for i in range(1, num+1):
        for j in range(i):
            # print star only at start and end of the row
            if j == 0 or j == i-1:
                print('*', end='')
            # print only star if it's last row
            else:
                if i != num:
                    print(' ', end='')
                else:
                    print('*', end='')
        print()

def pyramid_triangle(num):
    # pyramid star pattern
    for i in range(num):
        for j in range(num - i - 1):
            print(' ', end='')
        for k in range(2 * i + 1):
            print('*', end='')
        print()   

    

def hollow_pyramid_triangle(num):
    # hollow pyramid star pattern
    for i in range(num):
        # printing spaces
        for j in range(num - i - 1):
            print(' ', end='')

    # printing stars
    for k in range(2 * i + 1):
        # print star at start and end of the row
        if k == 0 or k == 2 * i:
            print('*', end='')
        else:
            if i == num - 1:
                print('*', end='')
            else:
                print(' ', end='')
    print()

def Reverese_pyramid_triangle(num):
    # reverse pyramid pattern
    for i in range(num):
    # printing spaces
        for j in range(i):
            print(' ', end='')
        # printing stars
        for j in range(2*(num-i)-1):
            print('*', end='')
        print()

def diamond_star_pattern(num):
    # upward pyramid
    for i in range(num):
        for j in range(num - i - 1):
            print(' ', end='')
        for j in range(2 * i + 1):
            print('*', end='')
        print()

    # downward pyramid
    for i in range(num - 1):
        for j in range(i + 1):
            print(' ', end='')
        for j in range(2*(num - i - 1) - 1):
            print('*', end='')
        print()

def Hollow_diamond_star_pattern(num):

    # upward hollow pyramid
    for i in range(num):
        for j in range(num - i - 1):
            print(' ', end='')
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                print('*', end='')
            else:
                print(' ', end='')
        print()

    # downward pyramid
    for i in range(num - 1):
        for j in range(i + 1):
            print(' ', end='')
        for j in range(2*(num - i - 1) - 1):
            if j == 0 or j == 2*(num - i - 1) - 2:
                print('*', end='')
            else:
                print(' ', end='')
        print()

def main():
    num = int(input("Enter the number :"))
    Lft_Sqaure_patttern(num)
    Left_triangle(num)
    downward_triangle(num)
    hollow_triangle(num)
    pyramid_triangle(num)
    hollow_pyramid_triangle(num)
    Reverese_pyramid_triangle(num)
    diamond_star_pattern(num)
    Hollow_diamond_star_pattern(num)

if __name__=="__main__":
    main()