from constraintsearch import *

amigos = ["Andre", "Bernardo", "Claudio"]

domains = { "Andre" : [("Bernardo", "Claudio")],
            "Bernardo" : [("Andre", "Claudio"), ("Claudio", "Andre")],
            "Claudio" : [("Andre", "Bernardo"), ("Bernardo", "Andre")]
            }

edges = [(v1, v2) for v1 in amigos for v2 in amigos if v1 != v2]

constraints = { X: (lambda r1,c1,r2,c2: c1[0]!=c2[0] and c1[1]!=c2[1]) for X in edges}

cs = ConstraintSearch(domains, constraints)

print(cs.search())
