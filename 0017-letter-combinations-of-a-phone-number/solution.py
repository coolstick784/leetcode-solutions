class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping_dict = {
            "2":["a", "b", "c"],
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j", "k", "l"], 
            "6":["m", "n", "o"],
            "7":["p", "q", "r", "s"],
            "8":["t", "u", "v"],
            "9":["w", "x", "y", "z"]
        }
        prev_step = [""]
        cur_step = []
        for d in digits:
            for pre in prev_step:
                for l in mapping_dict[d]:
                    cur_step.append(pre + l)
            prev_step = cur_step.copy()
            
            cur_step = []
        return prev_step 
        
