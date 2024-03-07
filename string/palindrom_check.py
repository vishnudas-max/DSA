def is_palindrome(str):
    # reverse = str[::-1]
    # if str == reverse:
    #     return True
    # else:
    #     return False

    l= len(str)
    for i in range(l // 2):
        if str[i] != str[l-i-1]:
            return False
    return True
k = is_palindrome('racecar')
if k:
    print('Palindrome')
else:
    print('not a pilindrome')