'''
Created on 2022. 10. 13.

@author: zhfld
'''
def sum_two(v1,v2):
    print("Function of addition")
    return v1+v2;
def sum_mul(v1,v2):
    return v1+v2,v1*v2
def sum_multiple(*values):
    sum=1
    for val in values:
        sum *= val
    return sum
def print_family(name1, name2, *rest_names, **family_names):
    print(family_names['First'],'',name1)
    print(family_names['Second'],'',name2)
    print(family_names['All_of_rest'],'',rest_names)
def prn_names(*names, family_name='KIM'):
    for name in names:
        print(family_name,'',name)
def rev_prn_names(family_name1='KIM',*names):
    for name in names:
        print(family_name1,'',name)
a= sum_two(11,12)
add,mul = sum_mul(3,4)
print(a)
print("--------")
print(sum_multiple(1,2,3,5,4,5,6,7))
print("--------")
print(print_family('김은호','천영환','김도환','황훈하',First='Cho',Second='SungIn',All_of_rest = 'CHOSUNGIN'))
print("--------")
print(prn_names('김은호','천영환','김도환'))
print(rev_prn_names('김은호','천영환','김도환'))
