def avg(*value):
    x=0
    for i in value:
        x=x+i
    return x/len(value)
y=input('value :')
y=avg(y)
print(y)
