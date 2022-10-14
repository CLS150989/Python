def outerFnction(text):
    def innerFunction():
        print(text)
    return innerFunction

outerFnction("text")