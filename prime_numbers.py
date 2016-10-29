import math
def all_prime_numbers_below_n(num):

    for num in range(1,num):
        if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
           print num

all_prime_numbers_below_n(10)
