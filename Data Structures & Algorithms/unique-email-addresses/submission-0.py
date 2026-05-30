class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # everything before @ = local
            # '.' can be ignored in local name, send to same address
            # everything after '+' -> '@' can be ignored in local name, 
            # send to same address as everyhitng before '+'
        # everything after @ = domain
            # '.' CANNOT be ignored in domain name, send to DIFFERENT address

    # solution, clean emails then add to dict if not already exist
        # O(1) lookup with key vs. lookup in list O(n)
    
        res = {}
        for email in emails:
            local, i = "", 0
            while email[i] != '@':
                if email[i] == '.':
                    i += 1
                    continue 
                elif email[i] == '+':
                    while email[i] != '@':
                        i += 1
                    break
                else:
                    local += email[i]
                    i += 1
            if (local + email[i:]) in res:
                continue
            else:
                res[local+email[i:]] = 1
                    
        return len(res)