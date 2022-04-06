from functools import reduce

lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]
neg_count=list(map(lambda x:x*(-1),
                    filter(lambda x:x<0,lst1)))
print(neg_count)
multiply = reduce(lambda a, b:a*b , neg_count)
print(multiply)

