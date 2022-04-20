a = "abcabcbb"
def lengthOfLongestSubstring(a):
	count = 0
	visited = []
	for i in list(a):
		if i in visited:
			visited = visited[visited.index(i)+1:]
			visited.append(i)
			if count<len(visited):
				count = len(visited)
		else:
			visited.append(i)
			if count<len(visited):
				count = len(visited)
	return count



print(lengthOfLongestSubstring(a))
