'''
Multiplication table printer
'''

def table(a):
    for i in range(1,11):
        print("{0} x {1} = {2}".format(a, i, i*a))

def run():
    table(float(input("Enter a number: ")))

if __name__ == '__main__':
    try:
        run()
    except ValueError:
        print("You entered an invalid number")
