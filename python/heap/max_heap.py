class MaxHeap:
    def __init__(self, lst):
        self.list = self.build_heap(lst)
    
    def build_heap(self, a):
        if not a: return a
        size = len(a)
        i = (size // 2) - 1
        while i >= 0:
            self.shift_down(a,i,size)
            i -= 1
        return a
    
    def insert(self, val):
        self.list.append(val)
        self.shift_up(len(self.list)-1)

    def remove(self, index):
        if index >= len(self.list): return
        last_index = len(self.list)-1
        self.swap(self.list, index, last_index)
        del self.list[last_index]
        self.shift_down(self.list, index, len(self.list))


    def shift_down(self, a, index, size):
        parent = index
        while parent < size:
            child1 = 2*parent+1
            child2 = child1 + 1
            max_child = size
            if child1 < size: max_child = child1
            if max_child >= size or (child2 < size and a[child2] > a[child1]): max_child = child2
            if max_child >= size: break
            if a[parent] < a[max_child]:
                self.swap(a, parent, max_child)
            else:
                break
            parent = max_child
        return a
    

    def shift_up(self, index):
        child = index
        parent = (child-1) // 2
        while parent >= 0 and child >= 0 and self.list[child] > self.list[parent]:
            self.swap(self.list, parent, child)
            child = parent
            parent = (child-1) // 2
    
    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]
 