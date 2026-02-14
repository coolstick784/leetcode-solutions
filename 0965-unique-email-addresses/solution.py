class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        local = [e.split("@")[0] for e in emails]
        domains = [e.split("@")[1] for e in emails]
        local = [e.replace(".", "") for e in local]
        local = [e.split("+")[0] for e in local]
        final = set()
        for idx, loc in enumerate(local):
            domain = domains[idx]
            final.add(loc + "@" + domain)
        return len(final)
            
        
        
