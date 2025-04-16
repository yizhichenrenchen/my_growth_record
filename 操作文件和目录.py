import os
print(os.name)#此处显示nt即为windows系统，显示posix即为Linux,Unix,macOS系统
#若要获取详细的系统信息，可以调用uname,但是此函数在windows系统上不提供，所以会报错

#(os.uname())
#在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看
print(os.environ)
#要获取某个环境变量的值，可以调用os.environ.get('key')
print(os.environ.get("PATH"))
#操作文件和目录
#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
#查看当前目录的绝对路径
print(os.path.abspath('.'))
#在某个目录下创建一个新目录，首先要把这个目录表示出来
print(os.path.join(r"F:\工作资料\25年图纸\4月","18"))
#然后创建新目录
#os.mkdir(r"F:\工作资料\25年图纸\4月\20")
#删除一个目录
#os.rmdir(r"F:\工作资料\25年图纸\4月\18")
#列出当前目录下的所有目录
l = [x for x in os.listdir('.') if os.path.isdir(x)]
print(l)
#列出所有的.py文件
j = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(j)
