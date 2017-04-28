# -*- coding: utf-8 -*-
# Python 3.6.1

"""Python heap data structure implementation.

This module implements the heap data structure, especially binary heap with
array. It supports minheap and maxheap. Additional functionalities for heap
are added for convenience with basic functions that heap ADT requires.
   
"""
class Heap(object):
    """Heap implementation. Minheap and maxheap are supported"""
    # System functions
    def __init__(self, heaptype = 0):
        """__init__ method of the Heap class

        Args:
            heaptype (int, optional): Specifying the type of heap.
                0 means minheap and 1 means maxheap. Default is minheap.
        """
        if heaptype != 0 and heaptype != 1:
            raise ValueError("Argument only can be 0 or 1")
        self.__heaptype = heaptype
        self.__heapcmp = -1 if heaptype == 0 else 1
        self.__heap = []

    # Private methods
    def __downheap(self, item_idx):
        """Shift down the selected item to restore heap property

        Args:
            item_idx (int): Index of the selected item that
                violates heap property

        Returns:
            None
        """
        curr_idx = item_idx
        continueloop = True
        while 2*curr_idx + 1 < len(self.__heap) and continueloop:
            curr_item = self.__heap[curr_idx]
            lchild_idx = 2*curr_idx + 1
            rchild_idx = 2*curr_idx + 2
            if rchild_idx >= len(self.__heap):
                # No right child
                child_idx = lchild_idx
                child_item = self.__heap[child_idx]
            else:
                lchild_item = self.__heap[lchild_idx]
                rchild_item = self.__heap[rchild_idx]
                if (lchild_item > rchild_item) - (lchild_item < rchild_item)\
                   == self.__heapcmp:
                    child_item = lchild_item
                    child_idx = lchild_idx
                else:
                    child_item = rchild_item
                    child_idx = rchild_idx
            if (child_item > curr_item) - (child_item < curr_item)\
               == self.__heapcmp:
                self.__heap[curr_idx], self.__heap[child_idx] = \
                    self.__heap[child_idx], self.__heap[curr_idx]
                curr_idx = child_idx
            else:
                continueloop = False

    def __upheap(self, item_idx):
        """Shift up the selected item to restore heap property

        Args:
            item_idx (int): Index of the selected item that
                violates heap property

        Returns:
            None
        """
        curr_idx = item_idx
        continueloop = True
        while curr_idx > 0 and continueloop:
            curr_item = self.__heap[curr_idx]
            parent_idx = int((curr_idx - 1) / 2)
            parent_item = self.__heap[parent_idx]
            if (curr_item > parent_item) - (curr_item < parent_item)\
               == self.__heapcmp:
                self.__heap[curr_idx], self.__heap[parent_idx] = \
                    self.__heap[parent_idx], self.__heap[curr_idx]
                curr_idx = parent_idx
            else:
                continueloop = False
                
    # Public methods
    def peek(self):
        """Return the root of heap

        Args:
            None

        Returns:
            (object): Root of the heap. If heap is minheap, it should be
                minimum value, and otherwise, it should be maximum value.
        """
        if len(self.__heap) == 0:
            raise IndexError("Heap is empty")
        return self.__heap[0]

    def pop(self):
        """Remove the root of heap and return it

        Args:
            None

        Returns:
            (object): Root of the heap. If heap is minheap, it should be
                minimum value, and otherwise, it should be maximum value.
        """
        if len(self.__heap) == 0:
            raise IndexError("Heap is empty")
        top = self.__heap[0]
        self.__heap[0] = self.__heap[-1]
        self.__downheap(0)
        del self.__heap[-1]
        return top

    def push(self, item):
        """Add item to heap

        Args:
            item (object): Item to add to the heap. Item must be
                comparable.

        Returns:
            None
        """
        new_idx = len(self.__heap)
        self.__heap.append(item)
        self.__upheap(new_idx)

    def size(self):
        """Return the number of items in the heap

        Args:
            None

        Returns:
            (int): Number of items in the heap
        """
        return len(self.__heap)

    def is_empty(self):
        """Return if heap is empty or not

        Args:
            None

        Returns:
            (boolean): True if size of heap is 0, false otherwise
        """
        return len(self.__heap) == 0

    def replace(self, old_item, new_item):
        """Replace the old item in heap to given item

        Args:
            old_item (object): Item already in the heap
            new_item (object): Item that will replace old_item. It must
                be comparable with items in the heap

        Returns:
            None
        """
        try:
            idx = self.__heap.index(old_item)
        except ValueError:
            raise ValueError("No such item in the heap")
        self.__heap[idx] = new_item
        if (old_item > new_item) - (old_item < new_item) == self.__heapcmp:
            self.__downheap(idx)
        else:
            self.__upheap(idx)
