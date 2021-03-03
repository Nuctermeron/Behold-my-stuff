def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


print(isPalindrome(-1001))