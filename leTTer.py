#A
'''n=int(input())
if n>4:
    for i in range(n):
        for j in range(n):
            if ((j==0 or j==n or j==n-1)and i!=0)or((i==0 or i==(n-1)//2)and 0<j<n-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()'''
                
#P
'''n=int(input("Size must be greatter than 7 \nEntar the size : "))
for i in range(n):
    for j in range(n):
        if((i==0 and j!=n-1) or
         (i==n//2 and j!=n-1)or
         (j==0)or
         (j==n-1 and i<n//2 and  i!=0)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
#B

        
