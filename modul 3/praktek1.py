# Membuat Stack
stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')
print ("Stack : ", stack)

# pop 
if len(stack) != 0:
    print("Pop : ", stack.pop())
    print("Stack : ", stack)
else :
    print("Stack Kosong!")

# top/peek
if not bool(stack):
    print("Stack Kosong!")
else:
    print("stack : ", stack)
    print("Top/Peek : ", stack[-1])


# isEmpty
if not bool(stack):
    print("Stack Kosong ")
else :
    print("Stack tidak kosong! ", stack)


# size
print("Stack Size : ", len(stack))