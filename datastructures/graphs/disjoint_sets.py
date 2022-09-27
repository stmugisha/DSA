## Disjoint set (alias UnionFind) data structure implementation

class DisjointSet:
    def __init__(self, size):
        """
        Initialize root array to len `size` with the values
        acting as the roots and the indices as the node values.
        Initially the root of each node(index) is itself.
        """
        self.root_array = [i for i in range(size)]


    def find(self, x):
        """Find root of node `x`.
        """
        return self.root_array[x]


    def union(self, x, y):
        """Add new connections `x`,`y` to the disjoint set.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        ## if root_x == root_y, then the nodes are already
        ## connected, else make traverse the root array and set
        ## the root (value at root[i]==root_y) of the index equal to
        ## the value of root_y to root_x
        if root_x != root_y:
            for i in range(len(self.root_array)):
                if self.root_array[i] == root_y:
                    self.root_array[i] = root_x


    def is_connected(self, x, y):
        """Check if nodes x and y are connected.
        Two nodes are connected if they have the same
        root node in the root array.
        """
        return self.find(x) == self.find(y)



if __name__=="__main__":
    d_set = DisjointSet(10)
    d_set.union(1, 2)
    d_set.union(2, 5)
    d_set.union(5, 6)
    d_set.union(6, 7)
    d_set.union(3, 8)
    d_set.union(8, 9)
    # graph: 1-2-5-6-7 3-8-9
    print(d_set.is_connected(1, 5))  # true
    print(d_set.is_connected(5, 7))  # true
    print(d_set.is_connected(4, 9))  # false
    #print(d_set.find(6))
    print(d_set.root_array)
    
    d_set.union(9, 4) # graph: 1-2-5-6-7 3-8-9-4
    print(d_set.is_connected(4, 9))  # true
    #print(d_set.find(9))