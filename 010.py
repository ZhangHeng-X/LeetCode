class Solution:
    def isMatch(self, s, p) -> bool:
        L, l = len(s), len(p)
        ans = list()
        ans.append(list())
        ans[0].append(True)
        for j in range(1, L+1):
            ans[0].append(False)
        for i in range(1, l+1):
            ans.append(list())
            if p[i-1] == '*':
                ans[i].append(ans[i-2][0])
            else:
                ans[i].append(False)

        for i in range(1, l+1):
            for j in range(1, L+1):
                if p[i-1] == '*':
                    if p[i-2] =='.':
                        ans[i].append(False)
                        for k in range(j+1):
                            if ans[i-2][k]:
                                ans[i][j] = True
                                break
                    else:
                        ans[i].append(ans[i-2][j])
                        for k in range(j,0,-1):
                            if p[i-2] == s[k-1]:
                                ans[i][j] = ans[i][j] or ans[i-2][k-1]
                            else:
                                break
                elif p[i-1] == '.':
                    ans[i].append(ans[i-1][j-1])
                else:
                    if p[i-1] != s[j-1]:
                        ans[i].append(False)
                    else:
                        ans[i].append(ans[i-1][j-1])

        return ans[l][L]


s = 'aab'
p = 'c*a*b'
print(Solution().isMatch(s,p))