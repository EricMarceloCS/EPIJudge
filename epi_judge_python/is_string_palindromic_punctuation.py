from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    str = ''

    for i in range(len(s)):
        if s[i].isalnum():
            str += s[i].lower()

    lp = 0
    rp = len(str) - 1
    while lp < rp:
        if str[lp] != str[rp]:
            return False
        lp += 1
        rp -= 1

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
