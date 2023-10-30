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

                
    def print(self,p=""):
        print(p,self.val)
        if self.left:
            q=p+"-"
            self.left.print(q)
        if self.right:
            q=p+"*"
            self.right.print(q)
                
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
        
    def min_max(self):
        if self.left:
            if  self.left.val >= self.left.min().val:
                print(self.val, end = " ")
        if self.right:
            if  self.left.val <= self.right.max().val:
                print(self.val, end = " ")
        
    def remove(self, s,):
        m = s.right
        l = s.right
        while m.left:
            l = m 
            m = m.left 
        if m.val != l.val:
            m.right = s.right 
        l.left = None 
        m.left = s.left
        del s 
        return m 

    def delete(self, val):
        if self.val == val:
            return True, self
        if self.left and val < self.val:
            r,s = self.left.delete(val)
            if r:
                if s.left is None and s.right is None:
                    self.left = None 
                    del s
                elif s.left and s.right:
                    m = self.remove(s)
                    self.left = m 
                elif s.left or s.right:
                    self.left = s.left if s.left else s.right
                    del s 
        if self.right:
            r,s = self.right.delete(val)
            if r:
                if s.left is None and s.right is None:
                    self.right = None 
                    del s 
                elif s.left and s.right:
                    m = self.remove(s)
                    self.right = m 
                elif s.left or s.right:
                    self.right = s.left if s.left else s.right
                    del s  
                    return False, None 
        
    
            
if __name__ == "__main__":
    val = [54,39,87,63,12,8,47,99,100,46]
    root = Node()
    root.create(val.pop(0))
    while val:
        root.insert( val.pop(0) )
    root.print()
    print("Inorder=>" )
    root.inorder()
    r, n = root.search(100)
    if r:
        print("Found ",n.val)
    else:
        print("Not found...")
        
    print("min/max")
    mn = root.min()
    mx = root.max()
    print("Min=>",mn.val," Max=>", mx.val)
    print(root.min_max())