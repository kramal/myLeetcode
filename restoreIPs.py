class Solution:
    def isIpPartValid(self, s: str) -> bool:
        strAsInt = int(s)

        if strAsInt > 255:
            return False

        return len(s) == len(str(strAsInt))

    def restoreIpAddresses(self, s: str) -> List[str]:
        ip_len = len(s)
        result = []

        if ip_len > 12 or ip_len < 4:
            return []

        for i in range(1, min(ip_len, 4)):
            curr_ip_parts = ["", "", "", ""]

            curr_ip_parts[0] = s[:i]

            if not self.isIpPartValid(curr_ip_parts[0]):
                continue
            for j in range(i + 1, i + min(ip_len - i, 4)):
                curr_ip_parts[1] = s[i:j]
                if not self.isIpPartValid(curr_ip_parts[1]):
                    continue
                for k in range(j + 1, j + min(ip_len - j, 4)):
                    curr_ip_parts[2] = s[j:k]
                    curr_ip_parts[3] = s[k:]

                    if self.isIpPartValid(curr_ip_parts[2]) and self.isIpPartValid(curr_ip_parts[3]):
                        result.append('.'.join(curr_ip_parts))

        return result
