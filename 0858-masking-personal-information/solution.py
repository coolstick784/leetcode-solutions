class Solution:
    def maskPII(self, s: str) -> str:
        # it's an email if it has an @ and a ., otherwise it's a phone number

        if "@" in s and "." in s:
            is_email = True
        else:
            is_email = False
        
        # split the @, convert the middle to *
        if is_email:
            name = s.split("@")[0]
            masked_name = name[0] + "*****" + name[-1]
            return masked_name.lower() + "@" + s.split("@")[1].lower()
        else:
            #remove sep chars, add the + if country code, add sep chars back
            s = s.replace("(", "").replace(")", "").replace("-", "").replace("+", "").replace(" ", "")
            if len(s) > 10:
                country_code = s[:-10]

            else:
                num = s
                country_code = None
            res = ""
            if country_code:
                res = "+"
                for _ in country_code:
                    res += "*"
                res += "-"
            res += "***-***-" + s[-4:]
            return res
            
        

