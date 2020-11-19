# 宣告使用 re 模組
import re

# re.match 與 re.search的差別
print(re.match("sir", "hello, sir"))          # 從頭開始比對相符合才算
print(re.search("sir", "hello, sir"))

# 設定比對的樣板
patten = re.compile('\d{4}-\d{6}')
# 比對資料與樣板是否匹配
print(patten.match('123-456'))
print(patten.match('0936-279195'))
# <re.Match object; span=(0, 11), match='0936-123456'>
# 匹配時會回應上述的 Match 物件

# 可省略建立 re 樣板的作法
txt = "Hello sir, ur phone is 0936-279195"
print(re.match(r'\d{4}-\d{6}', txt))
print(re.search(r'\d{4}-\d{6}', txt))

# Match物件的 group() 方法可得知符合的文字
text = "Hello sir, ur mail is peterju@ncut.edu.tw"
result = re.search(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
print(result.group())
result = re.search(r'([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', text)
print(result.group(0))
print(result.group(1))
print(result.group(2))
print(result.groups())
