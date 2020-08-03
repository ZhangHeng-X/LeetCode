class Solution:
	def isMatch(self, text, pattern):
		memo = {}
		def dp(i, j):
			if (i, j) not in memo:
				if i == len(pattern):
					memo[i, j] = j == len(text)
					return memo[i, j]
				first_match = j < len(text) and pattern[i] in {text[j], '.'}
				if i+1 < len(pattern) and pattern[i+1] == '*':
					memo[i, j] = dp(i+2, j) or first_match and dp(i, j+1)
				else:
					memo[i, j] = first_match and dp(i+1, j+1)

			return memo[i, j]

		return dp(0, 0)

text = 'baaa'
pattern = 'c*.a*'
print(Solution().isMatch(text, pattern))