def somaimpar(x, y): 
    resul = 0
    for i in range(y+1, x):
        if i%2 !=0 :
         resul += i
    return resul



x= int(input())
y= int(input())
r = somaimpar(x, y)
print (r)