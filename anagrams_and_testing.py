from timeit import Timer


# O(n)
def string_to_array(string: str) -> list:
    array = list()
    for letter in string:
        array.append(letter)
    return array


# O(n**2)
def anagram_1(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    a = string_to_array(s1)
    b = string_to_array(s2)
    a.sort()
    b.sort()

    # print(f"\n{a=}\n{b=}")

    if a == b:
        return True
    else:
        return False


# O(n)
def anagram_2(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    array1 = [0 for x in range(26)]
    array2 = [0 for x in range(26)]
    a_pos = 97

    for char in s1:
        pos = ord(char) - a_pos
        array1[pos] += 1

    for char in s2:
        pos = ord(char) - a_pos
        array2[pos] += 1

    if array1 == array2:
        return True
    else:
        return False


# O(1)
def anagram_testing(anagram_analizator):
    testing_dict = {"abc": "cba",  # True
                    "trie": "rtie",  # True
                    "qwe": "qwr",  # False
                    "tessting": "testting",  # False
                    string_generator(9999999, "y"): string_generator(9999999, "y"),
                    "welcomehome": "homeweleomc"}  # True

    for a, b in testing_dict.items():
        # print(f"{a} and {b}: {anagram_analizator(a, b)}")
        anagram_analizator(a, b)

        
# O(n)
def string_generator(char_num: int, char: str) -> str:
    array = [str(char) for i in range(char_num)]
    return "".join(array)


anagram1_timer = Timer("anagram_testing(anagram_1)", "from __main__ import anagram_testing, anagram_1")
anagram2_timer = Timer("anagram_testing(anagram_2)", "from __main__ import anagram_testing, anagram_2")

if __name__ == "__main__":
    print("{0:.6f}".format(anagram1_timer.timeit(number=1)))
    print("{0:.6f}".format(anagram2_timer.timeit(number=1)))
    # anagram_testing(anagram_1)
    # anagram_testing(anagram_2)
