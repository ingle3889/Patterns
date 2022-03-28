# Square pattern program

def Sqaure_patttern(num):
    for i in range(0, num):
        # Create a list of columns
        for j in range(0, num):
            print("*", end="")
        print()

    print("")
    for i in range(0, num):
    # printing * for 5 times and a new line
        print("*" * num)     

def main():
    num = int(input("Enter the number :"))
    Sqaure_patttern(num)

if __name__=="__main__":
    main()