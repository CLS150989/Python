from timeit import repeat


def make_repeater_of(x):

    def repeater(chain):
        return x * chain
    
    return repeater

repeat5 = make_repeater_of(5)
repeat10 = make_repeater_of(100)

print(repeat5('chara'))
print(repeat10('osesno'))