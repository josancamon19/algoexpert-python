# def longestPalindromicSubstring(string):
#     # Write your code here.
#     max_palindrome = ''
#     for i in range(len(string)):
#         for j in range(len(string)):
#             w = string[i: len(string) - j]
#             if is_palindrome(w):
#                 if len(w) > len(max_palindrome):
#                     max_palindrome = w
#
#     return max_palindrome
#
#
# def is_palindrome(string):
#     for i in range(len(string) // 2):
#         if string[i] != string[-i - 1]:
#             return False
#     return True

# def is_palindrome2(string):
#     if len(string) <= 1:
#         return True
#
#     stack = []
#     for char in string:
#         if len(stack) == 0:
#             stack.append(char)
#         else:
#             if len(stack) > 1 and stack[-2] == char:
#                 stack.pop()
#                 stack.pop()
#             elif stack[-1] == char:
#                 stack.pop()
#             else:
#                 stack.append(char)
#     return len(stack) == 0
#


def longestPalindromicSubstring(string):
    # Write your code here.
    if len(string) <= 1:
        return string
    longest = ''
    for i, char in enumerate(string):
        pass


def largest_palindrome_from_center(string, center_idx):
    if len(string) == 1:
        return string
    if center_idx == len(string) - 1:
        if string[center_idx - 1] == string[center_idx]:
            return string[center_idx - 1: center_idx + 1]
        else:
            return string[center_idx]
    elif center_idx == 0:
        if string[center_idx + 1] == string[center_idx]:
            return string[center_idx: center_idx + 1]
        else:
            return string[center_idx]
    return search_palindrome(string, center_idx - 1, center_idx + 1)


def search_palindrome(string, left_idx, right_idx):
    for i in range((left_idx + right_idx) // 2):
        left = left_idx - i
        right = right_idx + i

        print(left, right)

        if string[left] != string[right]:
            odd_palindrome = search_palindrome(string, left_idx - 1, right_idx)
            even_palindrome = string[left + 1:right]
            return max(even_palindrome, odd_palindrome, key=lambda x: len(x))
        elif right == len(string) - 1 or left <= 0:
            return string[left:right + 1]
    return ''


if __name__ == '__main__':
    # print(largest_palindrome_from_center('aabaa', 2))
    # print(largest_palindrome_from_center('aba', 1))
    # print(largest_palindrome_from_center('abba', 2))
    # print(largest_palindrome_from_center('aaa', 1))
    # print(largest_palindrome_from_center('aa', 1))
    print(largest_palindrome_from_center('aab', 0))
