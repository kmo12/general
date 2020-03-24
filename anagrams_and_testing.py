def anagram(s1: str, s2: str) -> bool:  # O(n)
    a = "".join(s1.split())
    b = "".join(s2.split())
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] not in b:
                return False
        return True
    else:
        return False


def anagram_testing():  # O(1)
    testing_dict = {"abc": "cba",  # True
                    "trie": "rtie",  # True
                    "qwe": "qwr",  # False
                    "test": " test1",  # False
                    "welcome home": "home weleomc"}  # True

    for a, b in testing_dict.items():
        print(f"{a} and {b}: {anagram(a, b)}")


anagram_testing()