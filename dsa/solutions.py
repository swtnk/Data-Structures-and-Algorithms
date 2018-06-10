from collections import defaultdict
# ################## QUESTION 1 ##################
def question1(s, t):                  #Function to find the presence of anagram of t in s as a substring:
    sdict = defaultdict(list)             #Creating dictionary for the characters in s
    tdict = defaultdict(list)             #Creating dictionary for the characters in s
    for char in s:                        #Iterating through the characters of s:
        if char in sdict:                     #Checking whether character is present in sdict:
            sdict[char] += 1                      #If present increment count value by 1
        else:                                 #If character is not there in sdict:
            sdict[char] = 1                       #Add character to sdict and initialize its value with 1
    for char in t:                        #Iterating through the characters of t:
        if char in tdict:                     #Checking whether character is present in tdict:
            tdict[char] += 1                      #If present increment count value by 1
        else:                                 #If character is not there in tdict:
            tdict[char] = 1                       #Add character to tdict and initialize its value with 1
    for key in tdict:                     #Iterating through the keys of t:
        if tdict[key] == sdict[key]:          #Checking whether value for keys in tdict and sdict are equal:
            status = "OK"                         #If values are equal set status as OK
        else:                                 #If values for keys in tdict and sdict is not equal:
            return False                          #Return False
    if status is "OK":                    #Checking whether status is OK:
        return True                           #if status is OK return true

print question1(s = "udacity", t = "ad")       #Calling function to find the presence of anagram of t in s as a substring
print question1(s = "udacity", t = "Ud")
print question1(s = "udacity", t = "tzc")
# True
# False
# False

# ################## QUESTION 2 ##################
def is_palindrome(a_sub):           #function for checking palindrome
    if not a_sub:
        return False                # return False if string is empty
    return a_sub == a_sub[::-1]     #return True if string is palindrom
    
def question2(a):                   #function to return Longest Palindromic Subsequence
    if not a:     
        return ''                   #return nothing if string is empty
    lps, front, rear = 0, 0, 0
    length = len(a)
    for i in xrange(length):
        for j in xrange(i + 1, length + 1):
            a_sub = a[i:j]
            if is_palindrome(a_sub) and len(a_sub) > lps:
                lps = len(a[i:j])
                front, rear = i, j
    return a[front:rear]           #returns longest palindromic subsequence

print question2('ABCBACADCBBCDA')  #Calling function to find the longest palindromic subsequence
print question2('')
print question2('a')
# ADCBBCDA
#
# a

# ################## QUESTION 3 ##################
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):                # A function that does union of two sets of x and y (uses union by rank)
    xroot = find(parent, x)
    yroot = find(parent, y)

    # Attach smaller rank tree under root of high rank tree
    # (Union by Rank)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    
    else :
        parent[yroot] = xroot                #If ranks are same, then make one as root
        rank[xroot] += 1                     # and increment its rank by one


def mst(graph, V, inv_dict):                        # Application of Kruskal's algorithm to construct MST 

    result = []                                     #This will store the resultant MST

    i = 0                                           # An index variable, used for sorted edges
    e = 0                                           # An index variable, used for result[]

    #Step 1:  Sort all the edges in non-decreasing order of their
    # weight.  If we are not allowed to change the given graph, we
    # can create a copy of graph
    graph =  sorted(graph,key=lambda item: item[2])

    parent = []
    rank = []

    # Create V subsets with single elements
    for node in range(V):
        parent.append(node)
        rank.append(0)

    # Number of edges to be taken is equal to V-1
    while e < V -1 :

        # Step 2: Pick the smallest edge and increment the index
        # for next iteration
        u,v,w =  graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent ,v)

        # If including this edge does't cause cycle, include it
        # in result and increment the index of result for next edge
        if x != y:
            e = e + 1
            result.append([u,v,w])
            union(parent, rank, x, y)
        # Else discard the edge

    # print the contents of result[] to display the built MST
    #"Following are the edges in the constructed MST"
    p1 = []
    final_result = defaultdict(list)
    for u,v,weight  in result:
        p1 = [(inv_dict[v],weight)]
        if inv_dict[u] not in final_result:
            final_result[inv_dict[u]] = p1
        else:
            final_result[inv_dict[u]] = final_result[inv_dict[u]].append(p1)

    return final_result

def question3(s1):
    n = len(s1)
    tmp_dict = defaultdict(list)                         #creating a default dictionary
    inv_dict = defaultdict(list)
    count = 0
    u,v,w = None, None, None
    graph = []
    for i in s1:
        tmp_dict[i] = count
        inv_dict[count] = i
        count += 1
        
    for i in s1:
        for j in s1[i]:
            u,v,w = tmp_dict[i], tmp_dict[j[0]], j[1]
            graph.append([u,v,w])

    return dict(mst(graph, count, inv_dict))

s1 = {'A': [('B', 2)],
      'B': [('A', 4), ('C', 2)],
      'C': [('A', 2), ('B', 5)]
     }
print question3(s1)  #Calling function to find the Minimum Spanning Tree using Kruskal's Algorithm
s1 = {'A': [('C', 2)],
      'B': [('A', 4), ('C', 2)],
      'C': [('B', 2), ('C', 5)]
     }
print question3(s1)
s1 = {'A': [('D', 2)],
      'B': [('A', 4), ('C', 2)],
      'C': [('B', 2), ('C', 5)],
      'D': [('C', 1), ('B', 3)]
     }
print question3(s1)
# {'A': [('B', 2)], 'C': [('A', 2)]}
# {'A': [('C', 2)], 'C': [('B', 2)]}
# {'A': [('D', 2)], 'C': [('B', 2)], 'D': [('C', 1)]}

# ################## QUESTION 4 ##################
head = None #Initializing the head node to keep track of starting node globally

class Node(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def push_right(node, new_data):             # Function to insert a new node at the beginning
    new_node = Node(new_data)
    node.right = new_node
    return new_node

def push_left(node, new_data):              # Function to insert a new node at the beginning
    new_node = Node(new_data)
    node.left = new_node
    return new_node

# Function to find LCA of n1 and n2. The function assumes
# that both n1 and n2 are present in BST
def lca(head, n1, n2):
    # Base Case
    if head is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(head.data > n1 and head.data > n2):
        return lca(head.left, n1, n2)

    # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if(head.data < n1 and head.data < n2):
        return lca(head.right, n1, n2)

    return head.data


def question4(mat, root, n1, n2):
    global head
    # Making BST
    head = Node(root)
    head.left, head.right = None, None            #Initializing the left and right node of BST
    node_value = 0                                #Initializing the value
    tmp_right, tmp_left = None, None
    node_list = []
    for elem in mat[root]:
        if elem:
            if(node_value>root):
                node_list.append(push_right(head, node_value))
            else:
                node_list.append(push_left(head, node_value))
        node_value += 1

    if not tmp_node:
        pass
    else:
        tmp_node = node_list.pop(0)
    while tmp_node != None:
        node_value = 0
        for elem in mat[tmp_node.data]:                                   #traversing the elements of mat
            if elem:
                if(node_value>tmp_node.data):
                    node_list.append(push_right(tmp_node, node_value))    #Appending to right
                else:
                    node_list.append(push_left(tmp_node, node_value))     #Appending to left
            node_value += 1
        if node_list == []:
            break
        else:
            if not tmp_node:
                pass
            else:
                tmp_node = node_list.pop(0)

    return lca(head, n1, n2)

print question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)

print question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3, 1, 4)

print question4([[0, 1, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 0, 0, 0, 1]],
          3, 1, 4)
# 3
# 3
# 3

# ################## QUESTION 5 ##################
class Node_of_LinkedList(object):                     #defining node class
    def __init__(self, data):                             #Creating constructor for initializing instance variable of node class
        self.data = data                                    #assigning the data-value of the node
        self.next = None                                    #assigning the reference to next node
        
class LinkedList(object):                             #defining linked list class
    count = 0                                           #class variable to keep track of number of elements in the linked list
    def __init__(self, head = None):                    #Creating contructor for initializing instance variable of linked list class
        self.head = head                                  #Assigning the value of head to the linked list
        LinkedList.count += 1                             #incrementing the value of class variable as head element got added
        
    def append(self, node):                             #defining function to add new node to the linked list
        current = self.head                               #variable to keep track of current node(node tracker)
        if self.head:                                     #checking if the linked list has a head node
            while current.next:                             #Running loop to traverse through the linked list elements
                current = current.next                        #assigning reference of next node to node tracker
            current.next = node                             #assigning the value to the node to which the node tracker refer as None
            LinkedList.count += 1                           #incrementing the value of class variable as new element got added
        else:                                             #if the linked list does not have head node
            self.head = node                                #Assigning the value of head to the linked list
            LinkedList.count += 1                           #incrementing the value of class variable as head element got added
            
    def find(self, ll, m):                              #defing function to return value at given position from end
        pos = LinkedList.count - m                        #calculation position upto which we have to traverse
        count = 0                                         #Variable to keep track of number of traversed elements in the linked list
        current = ll                                      #assigning head node to current node tracker
        if self.head:                                     #checking if the linked list has a head node
            while current.next and count < pos:             #traverse through linked list untill required position
                current = current.next                        #assigning reference of next node to node tracker
                count += 1                                    #increment variable to keep track of number of traversed elements in the linked list
            return current.data                             #returning the value of node at desired place
        else:                                             #if the linked list doesnot have head node
            return 'Not Found'                              #returning None
def question5(ll, n):
    if n > v.count:
        return 'do not exist'
    elif n < 0:
        return 'do not exist'
    return v.find(ll, n)

n = []
for i in range(0, 100):
    n.append(Node_of_LinkedList(i))
    
v = LinkedList(n[0])
for i in range(1, len(n) - 1):
    v.append(n[i])

ll = n[0]
print question5(ll, 1)
print question5(ll, -1)
print question5(ll, 101)
# 98
# do not exist
# do not exist