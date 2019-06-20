#!/usr/bin/env python3

import string


def simplify(text, whitespace=string.whitespace, delete=""):
    r"""Return the text with multiple spaces reduced to single spaces

    :param text: the text to be reduced
    :param whitespace: the whitespace to be checked
    :param delete: the char inside text would be delete
    :return: return the simplified text

    >>> simplify("  there    are a pencil\n   and   a book\t  too")
    'there are a pencil and a book too'
    """
    result=[]
    word=""
    for char in text:
        if char in delete:
            continue
        elif char in whitespace:
            if word:
                result.append(word)
                word=""
        else:
            word += char
    if word:
        result.append(word)
    return " ".join(result)

def shorten(text, length=25, indicator="..."):
    if len(text)>length:
        text = text[:length-len(indicator)] + indicator
    return text

def is_balanced(text, brackets="()[]{}<>"):
    counts = {}
    left_to_right={}
    for left, right in zip(brackets[::2], brackets[1::2]):
        assert left != right, "the bracket characters must differ"
        counts[left]=0
        left_to_right[right]=left
    for c in text:
        if c in counts:
            counts[left]+=1
        elif c in left_to_right:
            left = left_to_right[c]
            if counts[left]==0:
                return False
            counts[left] -= 1
    return not any(counts.values())

if __name__ == "__main__":
    import doctest
    doctest.testmod()
