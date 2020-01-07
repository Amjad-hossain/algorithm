# LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them.
# A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
# For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.
# Examples:
# LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
# LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.


def lcs(x, y, m, n):
    if m == 0 or n == 0:
        return 0
    if x[m - 1] == y[n - 1]:
        return lcs(x, y, m - 1, n - 1) + 1
    return max(lcs(x, y, m, n - 1), lcs(x, y, m - 1, n))


x = 'AGGTAB'
y = 'GXTXAYB'
print(lcs(x, y, len(x), len(y)))

x = 'ABCDGH'
y = 'AEDFHR'
print(lcs(x, y, len(x), len(y)))

x = 'ABCDG'
y = 'AEDFHR'
print(lcs(x, y, len(x), len(y)))
