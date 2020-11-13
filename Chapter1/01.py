"""
01. 「パタトクカシーー」Permalink

「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"""

text = 'パタトクカシーー'
index = [1, 3, 5, 7]
ret = [c for idx, c in enumerate(text) if idx+1 in index]
ret = ''.join(ret)

print(ret)