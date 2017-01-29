
# def rawinput():
#     yield "5"
#     yield "2 2 1 2 2"
#     yield "1 2"
#     yield "2 3"
#     yield "3 4"
#     yield "4 5"
    
# inp = [x for x in rawinput()]

# N = int(inp[0])
# T = list(map(int, inp[1].split(' ')))
# relations = [list(map(int, x.split(' '))) for x in inp[2:]]

N = int(raw_input())
T = list(map(int, raw_input().split(' ')))
relations = []
for i in range(2, N+1):
    relations.append(list(map(int, raw_input().split(' '))))

exp_times = {}
for i in range(1, N+1):
    exp_times[i] = []


available = {}
for i in range(1, N+1):
    available[i] = []
    
for r in relations:
    if (r[0] not in available[r[1]]):
        available[r[1]].append(r[0])
    if (r[1] not in available[r[0]]):
        available[r[0]].append(r[1])                             
                                          
    
    
class Node:
    
    def __init__(self, key, parent, ancestors):
        self.key = key
        self.time = T[key-1]
        self.parent = parent
        self.ancestors = ancestors
        self.children = []
        self.prior = 1
        
        for i in range(1,N+1):
            if i not in self.ancestors and i != self.key and i in available[self.key]:
                self.children.append(Node(i, self, ancestors + [self.key]))
                
    def __repr__(self):
        return "Node: " + str(self.key)
    
    
    def assign_priors(self):        
        for c in self.children:
            c.prior = self.prior/len(self.children)
            c.assign_priors()
        
        self.prior_time = self.prior * self.time
    
    def print_priors(self):
        print(self)
        print("Prior probability: " + str(self.prior))
        print("Prior expected time: " + str(self.prior_time))
        for c in self.children:
            c.print_priors()
    
    
    def sum_exp(self):
        exp = self.prior_time
        for c in self.children:
            exp += c.sum_exp()
            
        return exp
            

        
trees = [Node(i, None, []) for i in range(1, N+1)]


for tree in trees:      
    tree.assign_priors()
    
expected_times = [tree.sum_exp() for tree in trees]

print(expected_times.index(min(expected_times))+1)
