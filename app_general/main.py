class Node:
    def create(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def insert(self, val):
        node = Node()
        node.create(val)
        if val != self.val:
            if val < self.val :
                if self.left:
                    self.left.insert(val)
                else:
                    self.left = node
                    
            elif val > self.val :
                if self.right: #ถ้ามีnodeทางขวาอยู่เเล้วก็ดันไปให้ทางขวา
                    self.right.insert(val)
                else:  #ถ้าไม่มีnodeใหม่
                    self.right = node
        else:
            return
                
    def inorder(self): #น้อยไปมาก
        if self.left:
            self.left.inorder()
        print(self.val, end = " ")
        if self.right:
            self.right.inorder()
            
    def search(self, val):
        if val == self.val:
            return True, self
        if self.left and val < self.val:
            return self.left.search(val)
        if self.right and val > self.val:
            return self.right.search(val)
            return False, None 
        
    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self
    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self
        

    def remove(self, s):
        m = s.right
        l = s.right
        while m.left:
            l = m 
            m = m.left
        if m.val != l.val:
            m.right = s.right
        l.left = None
        return m

    def delete(self, val):
        if self.val == val:
            if not self.left and not self.right:
                return True, None
            if self.left and not self.right:
                return True, self.left
            if not self.left and self.right:
                return True, self.right
            if self.left and self.right:
                m = self.remove(self)
                self.val = m.val
                self.right = m.right
            return True, self

        if self.left and val < self.val:
            r, s = self.left.delete(val)
            if r:
                if s:
                    self.left = s
                else:
                    self.left = None
            return r, self

        if self.right and val > self.val:
            r, s = self.right.delete(val)
            if r:
                if s:
                    self.right = s
                else:
                    self.right = None
            return r, self

        return False, None 
    
    def reverse_inorder(self):
        if self.right:
            self.right.reverse_inorder()
        print(self.val, end=" ")
        if self.left:
            self.left.reverse_inorder()
        
    def reverse_inorder_set(self):
        values = set()
        if self.right:
            values.update(self.right.reverse_inorder_set())
        values.add(self.val)
        if self.left:
            values.update(self.left.reverse_inorder_set())
        return values

    # O (log n)
    def get_max_and_delete(self):
        if not self.right:
            max_value = self.val
            self = self.left
            return max_value, self
        max_value, self.right = self.right.get_max_and_delete()
        return max_value, self

    # O (log n)
    def get_min_and_delete(self):
        if not self.left:
            min_value = self.val
            self = self.right
            return min_value, self
        min_value, self.left = self.left.get_min_and_delete()
        return min_value, self
        
    
            
if __name__ == "__main__":
    val = [17, 20, 2, 5, 10]
    root = Node()
    # Create
    root.create(val.pop(0))
    # Insert
    while val:
        print(val)
        root.insert( val.pop(0) )
        
    # Search and Delete
    while root:
        root.print()

        min_value, root = root.get_min_and_delete()
        print(f"Min Value: {min_value}")
