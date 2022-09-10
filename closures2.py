'''
def nth_power(exponent):
    def pow_of(base):
        return pow(base,exponent)
    return pow_of

square = nth_power(2)
print(square(2))
'''
print(pow(3,3))