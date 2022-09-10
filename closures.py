def outerFuncton(text):
    def innerFunction():
        print(text)
    return innerFunction

########################################################
########   OuterFuncton("text")     ####################
########################################################
# This call contains already the nested inner
# function in  memory and the passed parameter get
# processed in the nested function. 
# That means we need yet to pass """the other  parameter 
# wich requieres  the inner function""" to run correctly.
#########################################################
#########################################################
#########################################################
# To do it we need to save the first  call on a variable
# and then call it with the missing parameter:

a = outerFuncton("text") #####first parameter of the first function 
a() ######second parameter wich actually runs with deafult parameter  
#####it simple prints the string "text"



###### once the first function has been stored on the variable
# even if it´s statement gets deleted the invocation  still  works. Example:

del outerFuncton ###deleting outerFunction
a()              #####printing it again