import socket#导入模块
import ssl
"""context = ssl.create_default_context()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET代表IPV4协议，若要使用IPV6协议只需要写成AF_INET6
s.connect(('www.sina.com.cn', 443))#建立连接，前面需要输入IP地址，输入新浪网域名可以直接转换为IP地址，后面80代表端口号
#建立连接后，就可以向新浪网发送请求，这里我们请求返回首页内容
s.send(b'GET / HTTPS/1.1\r\nHost: www.sina.com.cn\r\nUser-Agent:Mozilla/5.0(Windows NT 10.0;Win64;x64)\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    c = s.recv(1024)
    if c:
        buffer.append(c)
    else:
        break
date = b''.join(buffer)
s.close()
header,html = date.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('sina.html','wb') as f:
    f.write(html)"""
import socket
import ssl

# 创建 SSL 连接
context = ssl.create_default_context()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = context.wrap_socket(s, server_hostname='www.sina.com.cn')
s.connect(('www.sina.com.cn', 443))

# 发送 HTTPS 请求
request = (
    b'GET / HTTP/1.1\r\n'
    b'Host: www.sina.com.cn\r\n'
    b'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\n'
    b'Connection: close\r\n\r\n'
)
s.send(request)

# 接收数据
buffer = []
while True:
    data = s.recv(1024)
    if not data:
        break
    buffer.append(data)
data = b''.join(buffer)
s.close()

# 分割头部和内容
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

# 处理编码
charset = 'utf-8'
if b'charset=gbk' in header.lower():
    charset = 'gbk'
elif b'charset=gb2312' in header.lower():
    charset = 'gb2312'

# 保存文件
with open('sina.html', 'w', encoding=charset) as f:
    f.write(html.decode(charset, errors='ignore'))
