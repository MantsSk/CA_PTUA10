class MathOperations:
    @classmethod
    def factorial(cls, n):
        if n == 0:
            return 1
        elif n < 0:
            return "Factorial not available for negative numbers"
        else:
            return n * cls.factorial(n-1)

print(MathOperations.factorial(5)) # Output: 120
