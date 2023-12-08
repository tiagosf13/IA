lst = [1,2,3,4,5,6,7,8,9,10]

print("---------------------Exercicio 1a)---------------------")


def f(x): 
    if x==[]: 
        return 0 
    if x[0]>0: 
        return x[0] + f(x[1:]) 
    return f(x[1:])

print(f(lst))


print("---------------------Exercicio 1b)---------------------")

def g(x): 
    if x==[]: 
        return [[]] 
    y = g(x[1:]) 
    return y + [ [x[0]]+z for z in y ]

print(g(lst))