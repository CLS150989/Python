def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        x= func( *args,  **kwargs)
        print("Finished")
        return x
    return wrapper



@f1
def add(x,y):
    return x + y

print(add(4,5)) 