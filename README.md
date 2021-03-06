#余弦相似度算法：
一个向量空间中两个向量夹角间的余弦值作为衡量两个个体之间差异的大小，余弦值接近1，夹角趋于0，表明两个向量越相似，余弦值接近于0，夹角趋于90度，表明两个向量越不相似。
思路：1、分词；2、列出所有词；3、分词编码；4、词频向量化；5、套用余弦函数计量两个句子的相似度。
 
1、分词：使用jieba模块对句子分词后，分别得到两个列表。
 
2、列出所有词，将两个列表放在一个set中，并将其转换成字典，key为set中的词，value为set中词出现的位置。
 
3、将两个列表进行编码，将每个字转换为出现在set中的位置。

4、对两个列表进行oneHot编码，就是计算每个分词出现的次数。

5、得出两个句子的词频向量之后，就变成了计算两个向量之间夹角的余弦值，值越大相似度越高。
![](https://img2020.cnblogs.com/blog/2150000/202009/2150000-20200924194501396-220664059.png)
![](https://img2020.cnblogs.com/blog/2150000/202009/2150000-20200924194522883-489040476.png)

##4.模块接口部分的性能改进
利用profile模块进行性能分析
```import profile
def profileTest():
      ……
if __name__ == "__main__":
   profile.run("profileTest()")
```
其中输出每列的具体解释如下：
●ncalls：表示函数调用的次数；
●tottime：表示指定函数的总的运行时间，除掉函数中调用子函数的运行时间；
●percall：（第一个 percall）等于 tottime/ncalls；
●cumtime：表示该函数及其所有子函数的调用运行的时间，即函数开始调用到返回的时间；
●percall：（第二个 percall）即函数运行一次的平均时间，等于 cumtime/ncalls；
●filename:lineno(function)：每个函数调用的具体信息；
