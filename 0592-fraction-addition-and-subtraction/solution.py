import math
class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerators = []
        denominators = []

        cur = []
        m = 1
        for idx, ch in enumerate(expression):
            if ch == "/":
                cur = int("".join(cur))
                numerators.append(m * cur)

                m = 1
                cur = []
                
            elif ch == "-":
                if cur:
                    cur = int("".join(cur))
                    denominators.append(m * cur)
                m = -1
                cur = []

            elif ch == "+":
                cur = int("".join(cur))
                denominators.append(m * cur)
                cur = []
                
            else:
                cur.append(ch)
        cur = int("".join(cur))
        denominators.append(m * cur)
        lcm = 1
        for d in denominators:
            lcm = math.lcm(lcm, d)
        print(numerators, denominators)
        for idx, n in enumerate(numerators):
            numerators[idx] = n * (lcm/denominators[idx])
        s = sum(numerators)
        def reduce(n, d):
            if n == 0:
                return (0, 1)
            n, d = int(n), int(d)
            gcd = math.gcd(n, d)
            n = n // gcd
            d = d // gcd
            return (n, d)


        s, lcm = reduce(s, lcm)
        return str(int(s)) + "/" + str(int(lcm))
