class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 1:
            return True
        if bits[-2] == 0:
            return True
        if self.isValid(bits[:-2]):
            return False
        else:
            return True
    def isValid(self, bits):
        idx = 0
        while idx < len(bits):
            b = bits[idx]
            if b == 1:
                idx += 2
            else:
                idx += 1
        if idx > len(bits):
            return False
        else:
            return True
