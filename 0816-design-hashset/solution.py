class MyHashSet(object):

    def __init__(self):
        self.set = []
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.set:
            self.set.append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.set:
            self.set.remove(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        for el in self.set:
            if el == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
