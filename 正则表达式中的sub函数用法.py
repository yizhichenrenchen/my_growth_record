import re
#1.简单替换
s1 = 'I Love cats.Cats are cute!'
s2 = re.sub(r'cats','dogs',s1,flags=re.IGNORECASE)#不区分大小写替换
print(s2)
#2.批量替换模式化文本
phone = '132-2043-0087'
phone2 = re.sub(r'(\d{3})-(\d{4})-(\d{4})',r'\1-****-\3',phone)#此时替换号码中间四位为****
print(phone2)
#3.清理无效字符
s3 = 'uhguheghieh%^*,haifhi'
s4 = re.sub(r'[^0-9a-zA-Z]','',s3)
print(s4)
#4.动态内容生成
date = '2023-10-01'
date1 = re.sub(r'(\d{4})-(\d{2})-(\d{2})',r'\1/\2/\3',date)
print(date1)
