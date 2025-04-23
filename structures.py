Engineering = ["computer","civil","electronics","architecture"]

for i in Engineering:
    print(i)
    
#access
print(Engineering[0])

#update
Engineering[1]="mechanical"
print(Engineering)

#remove
Engineering.remove("architecture")
print(Engineering)

#append
Engineering.append("Aerospace")
print(Engineering)



    