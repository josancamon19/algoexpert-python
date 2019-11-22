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


def longestPalindromicSubstring(string):
    # Write your code here.
    if len(string) <= 1:
        return string
    max_palindrome = ''
    for i in range(len(string)):
        for j in range(len(string)):
            w = string[i: len(string) - j]
            if is_palindrome2(w):
                if len(w) > len(max_palindrome):
                    max_palindrome = w

    return max_palindrome


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

def is_palindrome(string, left_idx, right_idx):
    pass


if __name__ == '__main__':
    pass
