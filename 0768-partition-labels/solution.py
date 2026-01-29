class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Read in the letters one by one
        # There are at most 26 groups -- thus, we can initialize 26 groups
        # Each group is associated with a group of letters, a start index, and an end index
        # For each letter we go through, we loop through each group. 
        # If the letter is found, all groups past that group # are destroyed and that group's letters are concatenated with all the destroyed group numbers
        # The end index of that group is now the latest index
        groups = {}
        max_group = 0
        for i in range(1, 27):
            groups[i] = [set(), 0, 0]
        for idx, ch in enumerate(s):
            n = 1
            while n < 27:

                if ch in groups[n][0]:
                    print(ch)
                    print(idx)
                    groups[n][2] = idx
                    for i in range(n+1, 27):
                        
                        groups[n][0] = groups[n][0].union(groups[i][0])
                        groups[i][1] = 0
                        groups[i][2] = 0
                        groups[n][2] = max(groups[n][2], groups[i][2])
                        groups[i][0] = set()

                    n = 27
                elif groups[n][0] == set():
                    groups[n][0].add(ch)
                    groups[n][1] = idx
                    groups[n][2] = idx
                    n = 28

                n += 1
        all_s = []
        print(groups)
        for i in range(1, 27):
            if groups[i][0] != set():
                all_s.append(groups[i][2]-groups[i][1] +1)
        return all_s


                
            




