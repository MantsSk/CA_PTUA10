class StringUtils:
    @classmethod
    def reverse(cls, s):
        return s[::-1]

print(StringUtils.reverse('Hello, world!')) # Output: '!dlrow ,olleH'
