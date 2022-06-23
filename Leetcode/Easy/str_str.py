haystack = "sdjhlhello"
needle = "ll"
# haystack = "aaaaa"
# needle = "bba"


def strStr(haystack, needle):
	if len(needle) == 0:
		return len(needle)
	if len(haystack) < len(needle):
		return -1
	if needle in haystack:
		return haystack.index(needle)
	return -1

print(strStr(haystack, needle))
