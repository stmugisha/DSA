// Disjoint set (alias UnionFind) data structure implementation
#include<iostream>
#include<vector>

//using namespace std;
class DisjointSet {

    std::vector<int> root_array;

    public:
        /* alternative intialization of root_array size
         DisjointSet(int size){
            root_array(size);
            ...
         }
        */
        DisjointSet(int size) : root_array(size) {
            // Constructor: initialize root of each node(index) to itself
            for (int i = 0; i < size; i++) {
                root_array[i] = i;
            }
        }

        int find(int x) {
            // find root of node x
            return root_array[x];
        }

        void unionSet(int x, int y) {
            // Add new node connections to the disjoint set
            int root_x = find(x);
            int root_y = find(y);

            if (root_x != root_y) {
                for (int i = 0; i < root_array.size(); i++) {
                    if (root_array[i] == root_y) {
                        root_array[i] = root_x;
                    }
                }
            }
        }

        bool is_connected(int x, int y) {
            // Check if two nodes are connected.
            // Two nodes are connected if they have the same root
            return find(x) == find(y);
        }

};


// Test 
int main() {
    DisjointSet d_set(10);
    d_set.unionSet(1, 2);
    d_set.unionSet(2, 5);
    d_set.unionSet(5, 6);
    d_set.unionSet(6, 7);
    d_set.unionSet(3, 8);
    d_set.unionSet(8, 9);
    // graph: 1-2-5-6-7 3-8-9
    std::cout << std::boolalpha; //display bool string literal instead of 0, 1
    std::cout << d_set.is_connected(1, 5) << std::endl; //true
    std::cout << d_set.is_connected(5, 7) << std::endl; //true
    std::cout << d_set.is_connected(4, 9) << std::endl; //false

    d_set.unionSet(9, 4); // graph: 1-2-5-6-7 3-8-9-4
    //std::cout << d_set.root_array << std::endl;
    std::cout << d_set.is_connected(4, 9) << std::endl; //true

    return 0;
}