from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    ht = {}
    for i in range(len(magazine_text)):
        if magazine_text[i] == " ":
            continue
        elif magazine_text[i] in ht:
            v = int(ht[magazine_text[i]])
            v += 1
            ht[magazine_text[i]] = v
        else:
            ht[magazine_text[i]] = 1

    for i in range(len(letter_text)):
        try:
            v = ht[letter_text[i]]
            v -= 1
            if v == 0:
                del ht[letter_text[i]]
            else:
                ht[letter_text[i]] = v
        except KeyError:
            return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
