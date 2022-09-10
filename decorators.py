def f1(func):
    def wrapper():
        print("Started")
        func()
        print("Ended")
    return wrapper

    
@f1  #######DECORATOR######                  
def f():
    print("hello")

###  f1(f)() ### to print the function you have to call it with the parameters of both functions, 
################# the principal and the nested one

f = f1(f)  ###this variable stores the principal function with its parameter within it

    #### once stored it has it´s first parameter in memory,
f() ### you have to add the other parameter

'''
@f1------------------>decorator: it is not really necessary to 
store the function in a variable with the parameter within like: 
f = f1() if we use decorators. @f1 will automatilly do this work pasing the parameters to each function  
'''



