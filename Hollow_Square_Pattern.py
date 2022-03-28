# hollow square pattern

def Sqaure_patttern(num):
    for i in range(num):
        if i == 0 or i == num - 1:
            print('*' * num)
        else:
        # print * in first and last position in other rows
            print('*' + ' ' * (num - 2) + '*')  

    for i in range(0, num):
    # printing * for 5 times and a new line
        print("*" * num)          

def main():
    num = int(input("Enter the number :"))
    Sqaure_patttern(num)

if __name__=="__main__":
    main()