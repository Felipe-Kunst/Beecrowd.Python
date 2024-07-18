x = 0
count= 0
Media= 0

for i in range (0,6,1):
    x= float(input())
    if x >= 0 :
        count +=1
        Media +=x
        
Media/=count 
print(f'{count} valores positivos')
print(f'{Media:.1f}')