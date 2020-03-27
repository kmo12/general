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
    a.sort()  # O(n**2)
    b.sort()  # O(n**2)

    print(f"\n{a=}\n{b=}")

    if a == b:
        return True
    else:
        return False

    # Жалко удалять придуманное решение, работающее на sorted array
    # for index, letter in enumerate(a):
    #     if a[index] == b[index]:
    #         continue
    #     else:
    #         result = False
    # return result


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
                    "welcomehome": "homeweleomc"}  # True

    for a, b in testing_dict.items():
        print(f"{a} and {b}: {anagram_analizator(a, b)}")


if __name__ == "__main__":
    anagram_testing(anagram_2)
