from lab7 import MyString

if __name__ == "__main__":
    print("--- 1. Creating Instances ---")
    s_empty = MyString('')
    print("Empty string length:", len(s_empty))

    s = MyString('abcde')
    print("String from sequence:\n", s)

    s_rand = MyString(initialize_with_random=True)
    print("\nRandom string length:", len(s_rand))

    print("\n--- 2. Accessing & Modifying (Magic Methods) ---")
    print("Character at index 2:", s[2])
    s[2] = 'x'
    print("After modification (s[2] = 'x'):", "".join(s))

    print("\n--- 3. Testing Exceptions ---")
    try:
        s[1] = 'A'
    except TypeError as e:
        print("Caught exception for uppercase:", e)

    try:
        s[0] = '1'
    except TypeError as e:
        print("Caught exception for number:", e)

    print("\n--- 4. Insert & Remove ---")
    s.insert(1, 'z')
    print("After inserting 'z' at index 1:", "".join(s))
    s.insert(100, 'y')
    print("After inserting 'y' at index > length:", "".join(s))

    s.remove_character('x')
    print("After removing 'x':", "".join(s))
    try:
        s.remove_character('w')
    except ValueError as e:
        print("Caught exception for missing char:", e)

    print("\n--- 5. Replace Substring ---")
    s2 = MyString('abcabcabc')
    s2.replace('ab', 'xz', 2)
    print("After replacing 2 occurrences of 'ab' with 'xz':", "".join(s2))

    print("\n--- 6. Find & Length & Iteration ---")
    print("Index of 'bc':", s2.find('bc'))
    print("Index of 'w' (not found):", s2.find('w'))
    print("Length of string:", len(s2))
    print("Iterating over s2: ", end="")
    for char in s2:
        print(char, end=" ")
    print()

    print("\n--- 7. Slicing ---")
    sliced = s2[1:4]
    print("Slicing s2[1:4]:", "".join(sliced))

    print("\n--- 8. Concatenation & Repetition ---")
    s3 = MyString('lm')
    s4 = s3 + MyString('no')
    print("Concatenation (lm + no):", "".join(s4))
    s5 = s3 * 3
    print("Repetition (lm * 3):", "".join(s5))

    print("\n--- 9. Rotate & Reverse Substring ---")
    s_rot = MyString('abcde')
    s_rot.rotate(2)
    print("Rotate 'abcde' right by 2:", "".join(s_rot))

    s_rev = MyString('abcde')
    s_rev.reverse_substring(1, 3)
    print("Reverse substring of 'abcde' from 1 to 3:", "".join(s_rev))

    print("\n--- 10. Sliding Window & Frequency ---")
    s_win = MyString('abcabc')
    print("Sliding window (size 3, overlap 2):", s_win.sliding_window(3, 2))
    print("Character frequency:", s_win.character_frequency())