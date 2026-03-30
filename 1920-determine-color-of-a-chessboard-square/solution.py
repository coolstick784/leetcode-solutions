class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        # If row is odd and col is even, return False
        # If row is even and col is odd, return False

        row = ord(coordinates[0]) - ord('a')
        col = int(coordinates[1])
        if row % 2 != 0 and col % 2 == 0:
            return False
        if row % 2 == 0 and col % 2 != 0:
            return False
        return True
