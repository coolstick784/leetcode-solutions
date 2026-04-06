class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # split by spaces, then get the count of each word. convert to lowercase
        # then, sort the counter by counts. we can do this by creating a list of tuples that have the counts and the word
        # then, loop through that list until there's not a banned word
        banned = [word.lower() for word in banned]
        paragraph = paragraph.lower().replace("!", " ").replace("?", " ").replace(",", " ").replace("'", " ").replace(";", " ").replace(".", " ")
        ctr = Counter(paragraph.split(" "))

        words = []
        for word in ctr:
            if word != '':
                words.append((ctr[word], word))
        words.sort()
        words.reverse()
        for count, word in words:
            if word not in banned:
                return word
            
