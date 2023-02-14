"""
Design a max heap

if a node is at index i, then the left node will be 2(i) + 1,
right node will be 2(i) + 2.

To return the parent node, (i-1) // 2

"""

import sys 

class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0 
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    def get_parent(self, index):
        return index // 2

    def get_left_child(self, index):
        return index * 2

    def get_right_child(self, index):
        return index * 2 + 1

    def is_leaf_node(self, index):
        
        if index >= self.size // 2 and index <= self.size:
            return True 

        return False
    
    def swap(self, first, sec):

        self.Heap[first], self.Heap[sec] = self.Heap[sec], self.Heap[first]

    def maxHeapify(self, index):

        if not self.is_leaf_node(index):
            if self.Heap[index] < self.Heap[self.get_left_child(index)] or self.Heap[index] < self.Heap[self.get_right_child(index)]:

                if self.Heap[self.get_left_child(index)] > self.Heap[self.get_right_child(index)]:
                    self.swap(index, self.get_left_child(index))
                    self.maxHeapify(self.get_left_child(index))

                else:
                    self.swap(index, self.get_right_child(index))
                    self.maxHeapify(self.get_right_child(index))

            
