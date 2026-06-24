# 1. Flip string (reverse)
def flipstr(s: str) -> str:
    return s[::-1]  # slicing is fastest in Python for reversal


# 2. Loudify (uppercase)
def loudify(s: str) -> str:
    result = []
    for ch in s:
        if 'a' <= ch <= 'z':
            result.append(chr(ord(ch) - 32))
        else:
            result.append(ch)
    return ''.join(result)


# 3. Softify (lowercase)
def softify(s: str) -> str:
    result = []
    for ch in s:
        if 'A' <= ch <= 'Z':
            result.append(chr(ord(ch) + 32))
        else:
            result.append(ch)
    return ''.join(result)


# 4. Vowel count
def vowcount(s: str) -> int:
    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


# 5. Consonant count
def conscount(s: str) -> int:
    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    count = 0
    for ch in s:
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count


# 6. Is palindrome
def ispali(s: str) -> bool:
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True


# 7. Word count
def wordcount(s: str) -> int:
    count = 0
    in_word = False
    for ch in s:
        if ch != ' ':
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False
    return count


# 8. Character frequency (dict)
def charfreq(s: str) -> dict:
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq


# 9. Trim spaces (leading + trailing)
def trimspace(s: str) -> str:
    start = 0
    end = len(s) - 1
    while start <= end and s[start] == ' ':
        start += 1
    while end >= start and s[end] == ' ':
        end -= 1
    return s[start:end+1]


# 10. Swap string (swap case)
def swapstr(s: str) -> str:
    result = []
    for ch in s:
        if 'a' <= ch <= 'z':
            result.append(chr(ord(ch) - 32))
        elif 'A' <= ch <= 'Z':
            result.append(chr(ord(ch) + 32))
        else:
            result.append(ch)
    return ''.join(result)


# 11. Find substring (index)
def findstr(s: str, sub: str) -> int:
    n, m = len(s), len(sub)
    if m == 0:
        return 0
    for i in range(n - m + 1):
        if s[i:i+m] == sub:
            return i
    return -1


# 12. Split string (by space)
def splitstr(s: str) -> list:
    result = []
    word = ''
    for ch in s:
        if ch == ' ':
            if word:
                result.append(word)
                word = ''
        else:
            word += ch
    if word:
        result.append(word)
    return result


# 13. Join string (list to string)
def joinstr(lst: list, sep: str = ' ') -> str:
    if not lst:
        return ''
    result = lst[0]
    for word in lst[1:]:
        result += sep + word
    return result


# 14. Capitalize first letter
def capfirst(s: str) -> str:
    if not s:
        return ''
    first = s[0]
    if 'a' <= first <= 'z':
        first = chr(ord(first) - 32)
    return first + s[1:]


def titlefy(s: str) -> str:
    result = []
    capitalize_next = True
    for ch in s:
        if capitalize_next and 'a' <= ch <= 'z':
            result.append(chr(ord(ch) - 32))
            capitalize_next = False
        else:
            result.append(ch)
            if ch == ' ':
                capitalize_next = True
            else:
                capitalize_next = False
    return ''.join(result)
