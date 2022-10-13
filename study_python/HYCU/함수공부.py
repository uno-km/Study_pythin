'''
Created on 2022. 10. 13.

@author: zhfld
'''
def sum_two(v1,v2):
    print("Function of addition")
    return v1+v2;
def sum_mul(v1,v2):
    return v1+v2,v1*v2
a= sum_two(11,12)
add,mul = sum_mul(3,4)
print(a)
print("--------")
print(add)
print(mul)

