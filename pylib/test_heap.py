# -*- coding: utf-8 -*-
# Python 3.6.1

import unittest, random
import heap

class HeapTest(unittest.TestCase):
    def test_size(self):
        for case in range(100):
            min_heap = heap.Heap(0)
            max_heap = heap.Heap(1)
            elem = random.randint(1, 100)
            for i in range(elem):
                min_heap.push(random.random())
                max_heap.push(random.random())
            self.assertEqual(min_heap.size(), elem)
            self.assertEqual(max_heap.size(), elem)

    def test_is_empty(self):
        min_heap = heap.Heap(0)
        max_heap = heap.Heap(1)
        self.assertTrue(min_heap.is_empty())
        self.assertTrue(max_heap.is_empty())
        min_heap.push(3)
        max_heap.push(4)
        self.assertFalse(min_heap.is_empty())
        self.assertFalse(max_heap.is_empty())
        min_heap.pop()
        max_heap.pop()
        self.assertTrue(min_heap.is_empty())
        self.assertTrue(max_heap.is_empty())
    
    def test_peek(self):
        for case in range(100):
            min_heap = heap.Heap(0)
            max_heap = heap.Heap(1)
            random_list = []
            elem = random.randint(1, 100)
            for i in range(elem):
                ran = random.random()
                random_list.append(ran)
                min_heap.push(ran)
                max_heap.push(ran)
            self.assertEqual(min_heap.peek(), min(random_list))
            self.assertEqual(max_heap.peek(), max(random_list))
            self.assertEqual(min_heap.size(), elem)
            self.assertEqual(max_heap.size(), elem)
                        
    def test_peek_exception(self):
        min_heap = heap.Heap(0)
        max_heap = heap.Heap(1)
        with self.assertRaises(IndexError):
            min_heap.peek()
        with self.assertRaises(IndexError):
            max_heap.peek()

    def test_pop(self):
        for case in range(100):
            min_heap = heap.Heap(0)
            max_heap = heap.Heap(1)
            random_list = []
            elem = random.randint(1, 100)
            for i in range(elem):
                ran = random.random()
                random_list.append(ran)
                min_heap.push(ran)
                max_heap.push(ran)
            self.assertEqual(min_heap.pop(), min(random_list))
            self.assertEqual(max_heap.pop(), max(random_list))
            self.assertEqual(min_heap.size(), elem-1)
            self.assertEqual(max_heap.size(), elem-1)

    def test_pop_exception(self):
        min_heap = heap.Heap(0)
        max_heap = heap.Heap(1)
        with self.assertRaises(IndexError):
            min_heap.pop()
        with self.assertRaises(IndexError):
            max_heap.pop()

    def test_replace(self):
        for case in range(100):
            min_heap = heap.Heap(0)
            max_heap = heap.Heap(1)
            random_list = []
            elem = random.randint(1, 100)
            for i in range(elem):
                ran = random.random()
                random_list.append(ran)
                min_heap.push(ran)
                max_heap.push(ran)
            min_heap.replace(random_list[0], 0)
            max_heap.replace(random_list[0], 1)
            self.assertEqual(min_heap.peek(), 0)
            self.assertEqual(max_heap.peek(), 1)
            self.assertEqual(min_heap.size(), elem)
            self.assertEqual(max_heap.size(), elem)
            for i in range(elem):
                self.assertNotEqual(min_heap.pop(), random_list[0])
                self.assertNotEqual(max_heap.pop(), random_list[0])
            
    def test_sorting(self):
        for case in range(100):
            min_heap = heap.Heap(0)
            max_heap = heap.Heap(1)
            for i in range(100):
                min_heap.push(random.random())
                max_heap.push(random.random())
            minheap_sorted = []
            maxheap_sorted = []
            for i in range(100):
                minheap_sorted.append(min_heap.pop())
                maxheap_sorted.append(max_heap.pop())
            for i in range(99):
                assert minheap_sorted[i] < minheap_sorted[i+1]
                assert maxheap_sorted[i] > maxheap_sorted[i+1]
                
if __name__ == "__main__":
    unittest.main()
