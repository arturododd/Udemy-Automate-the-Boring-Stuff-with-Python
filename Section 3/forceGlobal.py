def spam():
    global eggs # Using global we instruct Python to use the global variable
    eggs = 'Hello'
    print(eggs)

eggs = 42
spam()
print(eggs)
