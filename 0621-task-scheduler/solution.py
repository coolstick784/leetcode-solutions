class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # At each step, we want to use the task that is most plentiful that has met the waiting period
        # If no tasks have met the waiting period, idle
        # To check which task is the most plentiful, we'll have a dictionary with 26 letters
        # Each letter is associated with the steps it must wait, as well as the number it has left
        # At each step, we'll find the letter with the maximum steps that has met the waiting period

        steps = 0
        counts = [0 for _ in range(26)]
        waiting_period = [0 for _ in range(26)]
        for ch in tasks:
            ch_n = ord(ch) - ord('A')
            counts[ch_n] += 1
        
        idx = 0
        max_letter_n = -1
        max_ct = 0
        while idx < len(tasks):
            max_letter_n = -1
            max_ct = 0
            for ch_n in range(26):
                if counts[ch_n] > max_ct and waiting_period[ch_n] == 0:
                    max_letter_n = ch_n
                    max_ct = counts[ch_n]
            if max_letter_n != -1:
                idx += 1
                waiting_period[max_letter_n] = n
                counts[max_letter_n] -= 1
                for ch_n in range(26):
                    if ch_n != max_letter_n:
                        waiting_period[ch_n] = max(0, waiting_period[ch_n]-1)
            else:
                for ch_n in range(26):
                    waiting_period[ch_n] = max(0, waiting_period[ch_n]-1)

            steps += 1


        return steps
