stack1 = []
stack2 = []

def enqueuue(a):
    stack1.append(a)

def dequeuue():
    if(len(stack2)>0):
        return stack2.pop()
    elif len(stack2)==0 and len(stack1)>0:
        while(len(stack1) > 0):
            stack2.append(stack1.pop())
            print("before for stack2",stack2)
        return stack2.pop()
    else:
        return "Stack underFlow"

print(dequeuue())

enqueuue(10)
enqueuue(20)
print(stack1)
print(dequeuue())
print(dequeuue())
print(dequeuue())

