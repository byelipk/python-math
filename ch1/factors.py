'''
Find factors of an integer

When a nonzero integer divides another integer
leaving a remainder 0, the first integer is said
to be a factor of the second.

a = 2
b = 4

b % a = 0

Here we can say that 4 is a factor of 2 because
when 4 divides 2 the remainer is 0.
'''

def is_factor(a,b):
    if b % a == 0:
        return True
    else:
        return False


def factors(b):
    for i in range(1, b+1):
        if b % i == 0:
            print(i)

if __name__ == '__main__':

    b = float(input('Your number please: '))

    if b > 0 and b.is_integer():
        factors(int(b))
    else:
        print('Please enter a positive integer')
