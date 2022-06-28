class globals():
    def __init__(self):
        self.globalVars = {}

globalVariables = globals()
globalVariables.globalVars['x'] = "global"

def outer():
    globalVariables.globalVars['x'] = "local"

    def inner():
        globalVariables.globalVars['x'] = "nonlocal"
        print("inner:", globalVariables.globalVars['x'])

    def change_global():
        globalVariables.globalVars['x'] = "global: changed!"
    
    print("outer:", globalVariables.globalVars['x'])
    inner()
    print("outer:", globalVariables.globalVars['x'])
    change_global()

print(globalVariables.globalVars['x'])
outer()
print(globalVariables.globalVars['x'])



# OR

"""

x = 'global'

def outer():
    x = "local"

    def inner():
        x = "nonlocal"
        print("inner:", x)
        return x

    def change_global():
        x = "global: changed!"
        return x
    
    print("outer:", x)
    x = inner()
    print("outer:", x)
    x = change_global()
    
    return x

print(x)
x = outer()
print(x)

"""


# OR


"""

x = 'global'

def outer():
    global x
    x = "local"

    def inner():
        global x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"
    
    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()

print(x)
outer()
print(x)

"""