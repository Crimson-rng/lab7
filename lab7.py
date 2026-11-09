import random

class MyString:
    def __init__(self, sequence='', initialize_with_random=False):
        '''
        :param sequence:
        :param initialize_with_random:
        '''
        self.__chars = []

        if initialize_with_random:
            n = random.randint(1, 10)
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            for i in range(n):
                self.__chars.append(random.choice(alphabet))
        else:
            for char in sequence:
                self.__validate_char(char)
                self.__chars.append(char)

    @staticmethod
    def __validate_char(char):
        '''
        Static helper method to validate that a character is a lowercase alphabet letter.
        Raises TypeError if the condition is not met.
        :param char:
        :return:
        '''
        if not isinstance(char, str) or len(char) != 1:
            raise TypeError("Must be a single character")
        if not char.isalpha():
            raise TypeError("Cannot add non-letter character")
        if not char.islower():
            raise TypeError("Cannot add uppercase character")

    def __getitem__(self, index):
        '''
        :param index:
        :return:
        '''
        if isinstance(index, slice):
            sub_chars = self.__chars[index]
            return MyString("".join(sub_chars))
        return self.__chars[index]

    def __setitem__(self, index, char):
        '''
        :param index:
        :param char:
        :return:
        '''
        self.__validate_char(char)
        self.__chars[index] = char

    def replace(self, old_sub, new_sub, k):
        '''
        Replaces k occurrences of a substring with another substring in-place.
        :param old_sub:
        :param new_sub:
        :param k:
        :return:
        '''
        for char in new_sub:
            self.__validate_char(char)

        temp_str = "".join(self.__chars)
        temp_str = temp_str.replace(old_sub, new_sub, k)
        self.__chars = list(temp_str)

    def insert(self, position, char):
        '''
        :param position:
        :param char:
        :return:
        '''
        self.__validate_char(char)
        if position >= len(self.__chars):
            self.__chars.append(char)
        else:
            self.__chars.insert(position, char)

    def remove_character(self, char, start=0, end=None):
        '''
        Removes all occurrences of a character in the string between start and end indexes.
        Raises ValueError if the character is not found.
        :param char:
        :param start:
        :param end:
        :return:
        '''
        if end is None:
            end = len(self.__chars) - 1

        found = False
        i = start

        while i <= end and i < len(self.__chars):
            if self.__chars[i] == char:
                found = True
                self.__chars.pop(i)
                end -= 1
            else:
                i += 1

        if not found:
            raise ValueError(f"Character '{char}' not in string")

    def find(self, substring):
        '''
        :param substring:
        :return:
        '''
        temp_str = "".join(self.__chars)
        return temp_str.find(substring)

    def __len__(self):
        return len(self.__chars)

    def __iter__(self):
        """
        Allow direct looping over the string (e.g., for char in s:).
        """
        return iter(self.__chars)

    def __add__(self, other):
        '''
        :param other:
        :return:
        '''
        if isinstance(other, MyString):
            return MyString("".join(self.__chars) + "".join(other.__chars))
        return MyString("".join(self.__chars) + str(other))

    def __mul__(self, number):
        '''
        To allow repetition using the * operator.
        :param number:
        :return:
        '''
        return MyString("".join(self.__chars) * number)

    def rotate(self, places):
        '''
        Rotates the string to the right by a given number of places in-place.
        :param places:
        :return:
        '''
        if len(self.__chars) == 0:
            return
        places = places % len(self.__chars)
        if places > 0:
            self.__chars = self.__chars[-places:] + self.__chars[:-places]

    def reverse_substring(self, start, end):
        '''
        Reverses a substring in-place, defined by start and end indexes.
        :param start:
        :param end:
        :return:
        '''
        if start < 0 or end >= len(self.__chars) or start >= end:
            return
        sub = self.__chars[start:end + 1]
        sub.reverse()
        self.__chars[start:end + 1] = sub

    def sliding_window(self, size, overlap):
        '''
        Returns a list of substrings (windows) of a given size and overlap.
        :param size:
        :param overlap:
        :return:
        '''
        windows = []
        step = size - overlap
        if step <= 0:
            step = 1

        temp_str = "".join(self.__chars)
        i = 0
        while i <= len(temp_str) - size:
            windows.append(temp_str[i:i + size])
            i += step

        return windows

    def character_frequency(self):
        '''
        Returns a dictionary with the frequency count for each character in the string.
        :return:
        '''
        freq = {}
        for char in self.__chars:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        return freq

    def __str__(self):
        '''
        Define how the string is printed.
        Displays the sequence and then the character at each position.
        :return:
        '''
        result = "".join(self.__chars)
        for i in range(len(self.__chars)):
            result += f"\nCharacter at position {i}: {self.__chars[i]}"
        return result