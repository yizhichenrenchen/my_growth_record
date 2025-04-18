from os import write

#1.打开文件并读取，然后关闭
f = open(r'C:\Users\34952\编程实验.txt','r',encoding='utf-8')
print(f.read(1))
"""此处可以在read()里面加入限制，表示每次读取多少个字符，此方法可以
避免爆内存，以为read方法最多可以读取10G，或者rea
dline()表示读取一行，readlines()可以一次性读取所有内容并返回list。
以上方法可按需选择，如果文件很小，可以直接read方法，若是文件大小不能确定，可以反
复使用read（size），如果是配置文件，调用readlines()最方便"""
f.close()
#2.由于文件打开时可能会出错，出错时close不会运行，为了保证不管出错没有都运行close，可以使用try...finally...来实现
try:
    f = open(r'C:\Users\34952\编程实验.txt', 'r', encoding='utf-8')
    print(f.read())
finally:
    if f:
        f.close()
#但是上述方法太过繁琐，可以使用with来代替
with open(r'C:\Users\34952\编程实验.txt','r',encoding='utf-8') as f:
    print(f.read())
#3.二进制文件，比如图片，视频等
"""m = open(r"E:\SteamLibrary\steamapps\workshop\content\431960\3324086615\啊~BJ golaniyule0 是果冻！- 4.mp4",'rb')
print(m.read())
m.close()"""
#此方法无法直接打开视频，想要打开视频可使用以下几种方法
#1.默认播放器打开
import webbrowser
import os
video_path = r"E:\SteamLibrary\steamapps\workshop\content\431960\3333313628\斗鱼 小小玉酱 (3)电报群@fulidashu888 (2).mp4"
webbrowser.open(video_path)
#2.获取视频元信息

from moviepy.editor import VideoFileClip

video_path = r"D:\视频\example.mp4"

try:
    with VideoFileClip(video_path) as video:
        print(f"时长: {video.duration} 秒")
        print(f"分辨率: {video.size}")  # (宽度, 高度)
        print(f"帧率: {video.fps}")
except Exception as e:
    print(f"错误: {e}")
#写文件
with open(r"C:\Users\34952\编程实验.txt",'a',encoding= 'utf-8') as f:#'a'可以在后面追加字符，而不是直接覆盖原文件
    f.write('\nhello,world')#\n可以换行写入
#'a+'模式（追加+读取）
with open(r"C:\Users\34952\编程实验.txt",'a+',encoding= 'utf-8') as f:
    f.write("I love you")
    f.seek(0)#可以将指针移回开头
    print(f.read())#读取文件内容



