print("program to convert infix to postfix")
op=["+","-","/","*","^"]
priority={'+':1,'-':1,'*':2,'/':2,'^':3}

def create(l):
    res=[]
    i=0
    while(i<len(l)):
        if(l[i].isdigit()):
            if(i==len(l)-1):
                res.append(l[i])
                i+=1
            elif(i!=len(l)-1):
                if(l[i+1].isdigit()):
                    res.append(l[i]+l[i+1])
                    i+=2
                else:
                    res.append(l[i])
                    i+=1
        else:
            res.append(l[i])
            i+=1
    return res

def convert(inf):
    stk=[]
    postfix=[]
    for i in inf:
        if(i.isdigit() or i.isalpha()):
            postfix.append(i)
        elif(i=='(' or i=='{'  or i=='['):
            stk.append(i)
        elif(i==')' or i=='}'  or i==']'):
            if(i==')'):
                while(stk[-1]!='('):
                    postfix.append(stk.pop())
                stk.pop()

            if(i==']'):
                while(stk[-1]!='['):
                    postfix.append(stk.pop())
                stk.pop()

            if(i=='}'):
                while(stk[-1]!='{'):
                    postfix.append(stk.pop())
                stk.pop()
        else:
            while stk and stk[-1]!='(' and priority[i]<=priority[stk[-1]]:
                postfix.append(stk.pop())
            stk.append(i)
    while stk!=[]:
        postfix.append(stk.pop())
    return postfix

def display(exp):
       for i in exp:
        print(i,end=" ")

def operation(a, b,op):
    a=int(a)
    b=int(b)
    if(op == '+'):
       return b+a
    elif(op == '-'):
       return b-a
    elif(op == '*'):
       return b*a
    elif(op == '/'):
       return b/a
    elif(op == '^'):
       return pow(b,a);
    else:
       return NULL;

def postfix_eval(postfix):
   stk=[]
   for i in postfix:
       if (i.isdigit()):
           stk.append(i)
       elif(i in op):
           a=stk.pop()
           b=stk.pop()
           sol=operation(a,b,i)
           stk.append(sol)
   return sol 


#main program
val=input("please enter infix expression:")
infix=create(val)
postfix=convert(infix)
print("the infix expression is:")
display(infix)
print("\nthe potfix expression is:")
display(postfix)
print("\nevaluated value is:",postfix_eval(postfix))
infix.reverse()
prefix=convert(infix)
prefix.reverse()
print("\n the perfix expression is:")
display(prefix)
