#for x in range(2,10):
#    print("\n");
#    for y in range(1,10):
#        print("%1dx%1d=%2d " %(x,y,x*y), end =''); 
        
#a = list (range(0,31)); # lsit of [0,1,2,3...30]
#target_lsit = a[::-1]; # list of [30,29...2,1,0]
#index = 0 ; #start value of index
#while index < len(target_lsit):
#    if target_lsit[index] ==3:
#        print( "index of 3 is %2d" %index);
#        break;
#    index +=1;
    
Class3 = [75,34,22,78,99,84,88,68,56,49,97,83,91,95,77,93,78,81,83,81,70,16];
degNum = [0,0,0,0,0];
degree = ['A','B','C','D','F'];
#
for point in Class3:
    if 90<= point <=100:
        degNum[0]+=1
    elif 80 <= point <= 89:
        degNum[1]+=1
    elif 70 <= point <= 79:
        degNum[2]+=1
    elif 60 <= point <= 69:
        degNum[3]+=1
    else: 
        degNum[4]+=1
else : 
    for i in range(5):
        print("Class %s : %2d" %(degree[i], degNum[i]));