import jieba
import math

f1 = open(r'C:\Users\69481\Desktop\test\orig.txt','r',encoding='utf-8')
f2 = open(r'C:\Users\69481\Desktop\test\orig_0.8_dis_10.txt','r',encoding='utf-8')  #打开文件
str1 = f1.read()
str2 = f2.read()      #将文件内容读入字符串s1,s2当中

str1_cut = [i for i in jieba.cut(str1, cut_all=True) if i!='']
str2_cut = [i for i in jieba.cut(str2, cut_all=True) if i!='']
word_cut = set(str1_cut).union(set(str2_cut))
#利用jieba模块分词，并转换成向量

word_dict = dict()   #创建字典
i = 0
for word in word_cut:
    word_dict[word] = i
    i += 1
#给文章中出现的词在字典中编号

#统计词频，形成向量
str1_code = [0] * len(word_dict)
for word in str1_cut:
    str1_code[word_dict[word]]+=1
str2_code = [0] * len(word_dict)
for word in str2_cut:
    str2_code[word_dict[word]]+=1

# 计算余弦相似度
sum = 0
a = 0
b = 0
for i in range(len(str1_code)):
    sum += str1_code[i] * str2_code[i]
    a += pow(str1_code[i], 2)
    b += pow(str2_code[i], 2)

try:
    result = round(float(sum) / (math.sqrt(a) * math.sqrt(b)), 3) # 利用math模块计算余弦相似度
except ZeroDivisionError:
    result = 0.0
print("\n余弦相似度为：%f"%result)
f3 = open(r'C:\Users\69481\Desktop\test\result.txt','w')
f3.write('文本相似度为'+str(result))        #将结果转换为字符串类型并写入result.txt文件





