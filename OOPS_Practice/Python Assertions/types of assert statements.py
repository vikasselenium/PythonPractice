
# assert statements are only for assert statements
# Two types
# - simple version
# - Augmented version

# simple version

# assert <conditional - expression>
# assert <conditional - expression>, message

#py -O test.py ==> now assert statement will be disabled, by default enabled
# what is difference between exception handling and assertion
# Assertions -> to fix development time errors, we use in dev and QA env
# Exception handling-> applicable for production env, to handle run time errors


def square_it(x):
    return x**x

# print(square_it(2))
# print(square_it(3))
# print(square_it(4))

assert square_it(2) ==4, "Square of 2 should be 4"
assert square_it(3) ==9, "Square of 3 should be 9"
assert square_it(4) ==16, "Square of 2 should be 17"