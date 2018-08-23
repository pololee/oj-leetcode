class Solution:
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        ip_number = self.ip_to_number(ip)
        results = []
        while n > 0:
            capacity = ip_number & (-ip_number)
            ip_space = self.space_taken(capacity, n)
            results.append(
                self.number_to_ip(ip_number) + '/' +
                str(self.prefix_length(ip_space))
            )

            ip_number += ip_space
            n -= ip_space

        return results

    def space_taken(self, capacity, requested):
        if capacity <= requested:
            return capacity

        taken = capacity
        while taken > requested:
            taken = taken // 2

        return taken

    def prefix_length(self, ip_space):
        power = 0
        while ip_space > 1:
            ip_space //= 2
            power += 1
        return 32 - power

    def ip_to_number(self, ip):
        number = 0
        chunks = ip.split('.')
        for chunk in chunks:
            number = number * 256 + int(chunk)
        return number

    def number_to_ip(self, number):
        ip = ['' for _ in range(4)]
        for i in reversed(range(4)):
            ip[i] = str(number & 255)
            number >>= 8
        # while number > 0:
        #     chunk = number % 256
        #     ip.append(str(chunk))
        #     number = number // 256
        # return '.'.join(ip[::-1])
        return '.'.join(ip)


def main():
    sol = Solution()
    ip = "192.168.1.17"
    print(sol.ipToCIDR("255.0.0.7", 10))
    # print(ip)
    # print(sol.number_to_ip(sol.ip_to_number(ip)))
if __name__ == '__main__':
    main()
