lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

# using lambda + sum() + map() to get count
count = sum(map(lambda x: x.count("a"), lst1))
count1 = sum(map(lambda x: x.count("A"), lst1))

# printing result
print("Count a of : "+ str(count))
print("Count A of : "+ str(count1))
print(int(count)+int(count1))

lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
counting_a=list(map(lambda x:x.count("a"),lst1))
counting_A=list(map(lambda x:x.count("A"),lst1))
comb=list(map(lambda x,y:[x,y],counting_a,counting_A))
print(counting_a)
print(counting_A)
print(comb)

