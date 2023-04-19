import re
class Solution:
    def solve(self, ipaddress):
        #Following patter to vlaidate all octactest are within minimum 1 and max 3 digits
        pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
        if not re.match(pattern,ipaddress):
            return False
        octests = ipaddress.split(".")
        for octet in octests:
            if not 0 <= int(octet) <=255:
                return False
        return True

networking = Solution()
print(networking.solve('11.11.11.11'))
print(networking.solve('11.11.11.'))
print(networking.solve('11.11.11.346'))
