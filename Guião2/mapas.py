from constraintsearch import *

region = ['A', 'B', 'C', 'D', 'E']
colors = ['red', 'blue', 'green', 'yellow', 'white']

domains = {r:colors for r in region}
print(domains)

edge_graph =  {
                "A" : ["B", "C", "E"],
                "B" : ["A", "C", "E"],
                "C" : ["B", "C", "E"],
                "D" : ["A", "C", "E"],
                "E" : ["A", "B", "C", "D", "E"]
                }

constraints = { (X,Y): (lambda r1,c1,r2,c2: c1!=c2) for X in edge_graph for Y in edge_graph[X] if X!=Y}  

cs = ConstraintSearch(domains, constraints)

print(cs.search())