"""
00. 文字列の逆順Permalink

文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
"""

text = 'stressed'
text = list(text)
text.reverse()
text = ''.join(text)
print(text)
