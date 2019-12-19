import math

class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # put item at end/bottom of heap 
        # bubble up if the heap eq is false
        self.storage.append(value)
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        # replace root/max element with popped last element
        # with last element as new root
        # sift it down until heap eq is true
        last = self.storage.pop()
        self.storage[0] = last
        self._sift_down(0)

    def get_max(self): #a.k.a. "peek"?
        # "returns the maximum value in the heap in constant time"
        return self.storage[0]

    def get_size(self):
        # "returns the number of elements stored in the heap."
        return len(self.storage)

    def _bubble_up(self, index):
        if index == 0:
            return
        parent = math.floor((index - 1) / 2)
        if parent <= self.get_size() - 1 and self.storage[parent] <= self.storage[index]:
            self.storage[parent], self.storage[index] = self.storage[index], self.storage[parent]
            index = parent

        # given last element index
        # as long as there's a parent item
        # as long as parent index < child index
        # swap parent index with child index
        # walk upwards - index = parent index

    def _sift_down(self, index):
        child_l = 2 * index + 1
        child_r = 2 * index + 2
        if self.storage[child_l] is not None:
            index_of_larger = child_l
            if self.storage[child_r] is not None and self.storage[child_r] > self.storage[child_l]:
                index_of_larger = child_r
            if self.storage[index] >= self.storage[index_of_larger]:
                return
            else: 
                self.storage[index], self.storage[index_of_larger] = self.storage[index_of_larger], self.storage[index]
                index = index_of_larger
                return
                
        # take root value
        # as long as children exist (just check if a left child exists)
        # find the larger of the two children
        # if root is greater than larger of two children, exit
        # but if not - swap index with larger child
        # index becomes larger child index

"""
        heap[k] <= heap[2*k+1]
        parent = (child_index - 1 - 2)
        child_l = 2 * parent_index + 1
        child_r = 2 * parent_index + 2
        self.storage.index()
        index1, index2 = index2, index 1

"""