mydata = []
for i in range(10):
    Nums = int(input("Enter Numbers: "))  
    mydata.append(Nums)
evens = list(filter( lambda x : x % 2 == 0 , mydata ))
adding = list(map( lambda x : x + 15 , evens ))
print(f"Your Data: {adding}")