import pyperclip
import re
from base64 import b64encode

path = input("请输入图片路径")
if re.match('^".+"$',path):
    path = path[1:-1]
with open(path, "rb") as f:
    content = f.read()
content = str(b64encode(content))
content = content[2:-1]
content = "data:image/png;base64," + content
pyperclip.copy(content)
