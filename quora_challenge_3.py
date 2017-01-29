def raw_input():
    yield "6"
    yield "Animals ( Reptiles Birds ( Eagles Pigeons Crows ) )"
    yield "5"
    yield "Reptiles: Why are many reptiles green?"
    yield "Birds: How do birds fly?"
    yield "Eagles: How endangered are eagles?"
    yield "Pigeons: Where in the world are pigeons most densely populated?"    
    yield "Eagles: Where do most eagles live?"
    yield "4"
    yield "Eagles How en"
    yield "Birds Where"
    yield "Reptiles Why do"
    yield "Animals Wh"

  
inp = [x for x in raw_input()]

N = int(inp[0])
topics = inp[1].split(' ')


class Topic:
    def __init__(self, topic, parent):
        self.topic = topic
        self.parent = parent
        self.children = []
        self.questions = []
    
    def __repr__(self):
        return self.topic


parent = None
last_topic = None
topic_dict = {}

for t in topics:    
    
    if (topics.index(t) == 0):
        tree = Topic(t, None)
        # print("Creating root " + str(tree))
        parent = tree
        last_topic = tree
        topic_dict[t] = tree
        
    elif (t == '('):
        # print("Encountered opening parenthesis")
        if last_topic.parent:
            parent = last_topic
            print("Parent is now " + str(parent))
            
    elif (t == ')'):
        # print("Encountered closing parenthesis")
        if parent.parent:
            parent = parent.parent
            # print("Parent is now " + str(parent))
        
    elif (t not in ['(', ')']):
        last_topic = Topic(t, parent)
        parent.children.append(last_topic)
        # print("Appending " + str(last_topic) + " to " + str(parent))
        topic_dict[t] = last_topic
        
        
M = int(inp[2])


for i in range(3, M+3):
    key, question = inp[i].split(': ')
    topic_dict[key].questions.append(question)


K = int(inp[M+3])

queries = []
for i in range(M+5, M+K+4):
    queries.append([inp[i].split(' ')[0], ' '.join(inp[i].split(' ')[1:])])

# print(queries)