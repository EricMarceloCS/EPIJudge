from test_framework import generic_test


def can_form_palindrome(s: str) -> bool:
    ht = {}
    count = 0
    for i in range(len(s)):
        if s[i] in ht:
            val = ht.get(s[i])
            ht[s[i]] = val + 1
        else:
            ht[s[i]] = 1

    for v in ht.values():
        if v == 1:
            count = count + 1

    return count <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
