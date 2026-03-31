class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        lower_map = {}
        cleaned_vowel_map = {}

        for word in wordlist:
            lower = word.lower()
            cleaned = lower.replace("a", ".").replace("e", ".").replace("i", ".").replace("o", ".").replace("u", ".")

            if lower not in lower_map:
                lower_map[lower] = word
            if cleaned not in cleaned_vowel_map:
                cleaned_vowel_map[cleaned] = word

        wordset = set(wordlist)

        res = []
        for word in queries:
            lower = word.lower()
            cleaned = lower.replace("a", ".").replace("e", ".").replace("i", ".").replace("o", ".").replace("u", ".")

            if word in wordset:
                res.append(word)
            elif lower in lower_map:
                res.append(lower_map[lower])
            elif cleaned in cleaned_vowel_map:
                res.append(cleaned_vowel_map[cleaned])
            else:
                res.append("")
        return res
