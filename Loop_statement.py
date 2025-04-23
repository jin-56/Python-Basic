#iteration
#print(list(range(1,5)))
#loop for string 
a= "Mahrajan"
for i in a:
    print(i,end=":)")
    
#loop for list
subjects =["Probability","Software","Graphics","organization"]
for i in subjects:
    print (i,end=" ")  
    
    
#nested loop
for i in  a:
    for j in subjects:
        print (i,j,end=" ::")
                
#while loop
count=0
while count<=5:
    if count==3:
        print("THREE") #breal and continue
    else:    
        print(count)
    count=count+1
    break

