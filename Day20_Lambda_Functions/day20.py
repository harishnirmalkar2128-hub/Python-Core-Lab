# Noraml function (3 lines)

def square_normal(n):
    return n * n

#2 Lambda Function (1 line)
#syntax: Lambda arguments : expression
square_lambda = lambda n : n * n

print("Normal result:", square_normal(5))
print("Lambda result:", square_lambda(5))

#one more example : Do numbers ko add karna 
add = lambda a, b : a + b
print('Sum is:', add(10, 20))