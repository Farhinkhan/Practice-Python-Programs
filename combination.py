def fact(x):
    fact_x=1
    for i in range(1,x+1):
        fact_x*=i
    return(fact_x)
    
n=int(input("Enter the value of n :"))
r=int(input("Enter the value of r : "))
fn=fact(n)
fr=fact(r)
fnr=fact(n-r)
comb=fn/(fr*fnr)
print("Combination is :",comb)

