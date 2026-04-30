stack = []

# Push
stack.append('www.google.com')
stack.append('www.youtube.com')
stack.append('wwww.w3shool.com')
print("Stack: ", stack)

# Peek
topElement = stack[-1]
print("Peek: ", topElement)

# Pop
poppedElement = stack.pop()
print("Pop: ", poppedElement)

# Stack after Pop
print("Stack after Pop: ", stack)

# isEmpty
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(stack))
