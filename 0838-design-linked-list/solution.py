class MyLinkedList(object):

    def __init__(self):
        self.lst = []

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        try:
            return self.lst[index]
        except:
            return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.lst.insert(0, val)
        #print(self.lst)
    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.lst.append(val)
        #print(self.lst)
    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        try:
            if index <= len(self.lst):
                self.lst.insert(index, val)
        except:
            pass
        #print(self.lst)

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        try:
            del self.lst[index]
        except:
            pass
        #print(self.lst)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
