

# Guiao de representacao do conhecimento
# -- Redes semanticas
# 
# Inteligencia Artificial & Introducao a Inteligencia Artificial 
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2020
# v1.9 - 2019/10/20
#


# Classe Relation, com as seguintes classes derivadas:
#     - Association - uma associacao generica entre duas entidades
#     - Subtype     - uma relacao de subtipo entre dois tipos
#     - Member      - uma relacao de pertenca de uma instancia a um tipo
#


from collections import Counter

class Relation:
    def __init__(self,e1,rel,e2):
        self.entity1 = e1
#       self.relation = rel  # obsoleto
        self.name = rel
        self.entity2 = e2
    def __str__(self):
        return self.name + "(" + str(self.entity1) + "," + \
                str(self.entity2) + ")"
    def __repr__(self):
        return str(self)
    

# Subclasse AssocOne
class AssocOne(Relation):
    def __init__(self,e1,rel,e2):
        Relation.__init__(self,e1,rel,e2)

# Subclasse AssocNum
class AssocNum(Relation):
    def __init__(self,e1,rel,e2):
        Relation.__init__(self,e1,rel,e2)


# Subclasse Association
class Association(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,e2)

#   Exemplo:
#   a = Association('socrates','professor','filosofia')

# Subclasse Subtype
class Subtype(Relation):
    def __init__(self,sub,super):
        Relation.__init__(self,sub,"subtype",super)


#   Exemplo:
#   s = Subtype('homem','mamifero')

# Subclasse Member
class Member(Relation):
    def __init__(self,obj,type):
        Relation.__init__(self,obj,"member",type)

#   Exemplo:
#   m = Member('socrates','homem')

# Subclasse AssocOne
class AssocOne(Relation):
    def __init__(self,e1,rel,e2):
        Relation.__init__(self,e1,rel,e2)

# Subclasse AssocNum
class AssocNum(Relation):
    def __init__(self,e1,rel,e2):
        Relation.__init__(self,e1,rel,e2)

# classe Declaration
# -- associa um utilizador a uma relacao por si inserida
#    na rede semantica
#
class Declaration:
    def __init__(self,user,rel):
        self.user = user
        self.relation = rel
    def __str__(self):
        return "decl("+str(self.user)+","+str(self.relation)+")"
    def __repr__(self):
        return str(self)

#   Exemplos:
#   da = Declaration('descartes',a)
#   ds = Declaration('darwin',s)
#   dm = Declaration('descartes',m)

# classe SemanticNetwork
# -- composta por um conjunto de declaracoes
#    armazenado na forma de uma lista
#
class SemanticNetwork:
    def __init__(self,ldecl=None):
        self.declarations = [] if ldecl==None else ldecl
    def __str__(self):
        return str(self.declarations)
    def insert(self,decl):
        self.declarations.append(decl)
    def query_local(self,user=None,e1=None,rel=None,e2=None):
        self.query_result = \
            [ self.declarations for d in self.declarations
                if  (user == None or d.user==user)
                and (e1 == None or d.relation.entity1 == e1)
                and (rel == None or d.relation.name == rel)
                and (e2 == None or d.relation.entity2 == e2) 
            ]
        return self.query_result
    def query(self, entity, ass_name=None):
        declarations = [declaration for declaration in self.declarations
                        if not isinstance(declaration.relation, Association)
                        and declaration.relation.entity1 == entity
                        ]
        associations = [association for association in self.query_local(e1=entity, rel=ass_name)
                        if isinstance(association.relation, Association)]
        for declaration in declarations:
            associations += self.query(declaration.relation.entity2, ass_name)
        return associations
    def query2(self, entity, ass_name=None):

        local = [query for query in self.query_local(e1=entity, rel=ass_name)
                    if isinstance(query.relation, Member) or isinstance(query.relation, Subtype)
                ]

        herdadas = self.query(entity=entity, ass_name=ass_name)

        return local+herdadas
    def query_cancel(self, entity, ass_name):
        ldeclarations = self.query_local(e1=entity)
        lparents = [ d.relation.entity2 for d in ldeclarations if not isinstance(d.relation, Association) ]

        lassoc = [ d for d in ldeclarations if isinstance(d.relation, Association) and d.relation.name == ass_name ]
        
        if lassoc == []:
            for p in lparents:
                lassoc += self.query_cancel(p, ass_name)

        return lassoc
    def query_down(self, entity, association_name, child=False):
        ldeclartions = self.query_local(e2=entity)
        lchildren = [ d.relation.entity1 for d in ldeclartions if not isinstance(d.relation, Association) ]

        lassoc = []
        if child:
            lassoc = [ d for d in self.query_local(e1=entity) if isinstance(d.relation, Association) 
                                                                and d.relation.name == association_name ]
    
        for c in lchildren:
            lassoc += self.query_down(c, association_name, child=True)

        return lassoc
    
    def query_induce(self, entity, association_name):
        lassoc = self.query_down(entity, association_name)

        counter_dict = {}

        for assoc in lassoc:
            if assoc.relation.entity2 not in counter_dict:
                counter_dict[assoc.relation.entity2] = 1
            else:
                counter_dict[assoc.relation.entity2] += 1
        
        return max(counter_dict, key=counter_dict.get)


    def show_query_result(self):
        for d in self.query_result:
            print(str(d))

    def list_associations(self):
        return list(set([ d.relation.name for d in self.declarations
                    if isinstance(d.relation,Association) ]))

    def list_objects(self):
        return list(set([ d.relation.entity1 for d in self.declarations
                        if isinstance(d.relation,Member) ]))

    def list_users(self):
        return list(set([ d.user for d in self.declarations]))
    
    def list_types(self):
        
        # Three different places where types can be found:
        # 1. In the entity2 of a Member relation
        # 2. In the entity1 of a Subtype relation
        # 3. In the entity2 of a Subtype relation

        return list(set([ d.relation.entity2 for d in self.declarations
                        if isinstance(d.relation,Member) ] + \
                        [ d.relation.entity1 for d in self.declarations
                        if isinstance(d.relation,Subtype) ] + \
                        [ d.relation.entity2 for d in self.declarations
                        if isinstance(d.relation,Subtype) ]))

    def list_local_associations(self,obj):
        return list(set([ d.relation.name for d in self.declarations
                        if isinstance(d.relation,Association) and d.relation.entity1 == obj ]))
    
    def list_relations_by_user(self,user):
        return list(set([ d.relation.name for d in self.declarations
                        if d.user == user ]))
    
    def associations_by_user(self,user):
        return len(list(set([ d.relation.name for d in self.declarations
                        if d.user == user and isinstance(d.relation,Association) ])))
    
    def list_local_associations(self,obj):
        return list(set([ d.relation.name for d in self.declarations
                        if isinstance(d.relation,Association) and d.relation.entity1 == obj ]))
    
    def list_local_associations_by_entity(self,obj):
        return list(set([ (d.relation.name,d.user) for d in self.declarations
                        if isinstance(d.relation,Association) and d.relation.entity1 == obj ]))

    def predecessor(self, entity1, entity2):
        
        # Recursively search for entity2 in the entity2 of Subtype relations
        # until entity1 is found or there are no more Subtype relations to search

        if entity1 == entity2:
            return True
        else:
            for declaration in self.declarations:
                # If the relation of the declaration is a Member and the entity1 of the declaration is entity1
                if (declaration.relation.entity1 == entity2) and \
                    (
                        isinstance(declaration.relation,Member) or \
                        isinstance(declaration.relation,Subtype)  and \
                        declaration.relation.entity1 == entity2
                    ):
                    return True
        return False
    
    def predecessor_path(self, entity1, entity2):
        
        # Recursively search for entity2 in the entity2 of Subtype relations
        # until entity1 is found or there are no more Subtype relations to search

        pds = [d.relation.entity2 for d in self.declarations 
                if (
                        isinstance(d.relation, Member) or \
                        isinstance(d.relation, Subtype) and \
                        d.relation.entity1 == entity2
                    )
                ]
        if entity1 in pds:
            return [entity1, entity2]
        
        for declaration in pds:
            path = self.predecessor_path(entity1, declaration)
            if path is not None:
                return path + [entity2]
        

    def query_local_assoc(self, entity, association_name):

        # Devolve uma lista de pares (val, freq) com os valores locais mais frequentes e respectivas frequências.
        # Na seleção dos valores mais frequentes, os valores ̃sao acrescentados à lista por ordem decrescente da sua frequência,
        # até a soma das frequências atingir um valor não inferior a 0.75


        lassoc = self.query_local(e1=entity, rel=association_name)
        if lassoc == []:
            return None
        else:
            freq= {}

            for assoc in lassoc:
                if assoc.relation.entity2 not in freq:
                    freq[assoc.relation.entity2] = 1
                else:
                    freq[assoc.relation.entity2] += 1

            # Sort the dictionary by value
            freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

            # Get the sum of all frequencies
            total_freq = sum(freq.values())

            lst = []

            for key in freq:
                if total_freq >= 0.75:
                    lst.append((key, freq[key]))
                    total_freq -= freq[key]
                else:
                    break
        
        print(lst)
        freq = lst[0][1]/sum([x[1] for x in lst])
        return (lst[0][0], freq)
