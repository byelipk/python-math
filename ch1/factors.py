'''
Find factors of an integer
'''

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
        
# def is_factor(a,b):
#     if b % a == 0:
#         return True
#     else:
#         return False
#
# print(is_factor(123,12345))
