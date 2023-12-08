def interpretacoes(variaveis):
    if not variaveis:
        return [[]]
    
    resto = interpretacoes(variaveis[1:])
    return [[(variaveis[0], True)] + r for r in resto] + [[(variaveis[0], False)] + r for r in resto]

def generate_conjunctions(variaveis):
        if len(variaveis) == 1:
            return [ [(variaveis[0], True)] , [(variaveis[0], False)] ]

        l = []
        for c in generate_conjunctions(variaveis[1:]):
            #print(c)
            l.append([(variaveis[0], True)] + c)
            l.append([(variaveis[0], False)] + c)

        return l


# Exemplo de uso:
resultado = interpretacoes(["a", "b"])
resultado1 = generate_conjunctions(["a", "b"])
#print(resultado)
#print(resultado1)