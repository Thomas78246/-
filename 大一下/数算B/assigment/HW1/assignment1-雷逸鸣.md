# Assignment #1: 拉齐大家Python水平

Updated 0940 GMT+8 Feb 19, 2024

2024 spring, Complied by 雷逸鸣



**说明：**

1）数算课程的先修课是计概，由于计概学习中可能使用了不同的编程语言，而数算课程要求Python语言，因此第一周作业练习Python编程。如果有同学坚持使用C/C++，也可以，但是建议也要会Python语言。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知3月1日导入选课名单后启用。**作业写好后，保留在自己手中，待3月1日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

操作系统： Windows 11 家庭中文版
		    版本	22H2
		    安装日期	‎2023/‎8/‎9
		    操作系统版本	22621.2283
		    体验	Windows Feature Experience Pack 1000.22662.1000.0

Python编程环境：PyCharm 2023.1.2 专业版



## 1. 题目

### 20742: 泰波拿契數

http://cs101.openjudge.cn/practice/20742/



思路：



##### 代码

```python
def t(x):
    if x==0:
        return 0
    elif x==1 or x==2:
        return 1
    else:
        return t(x-1) + t(x-2) + t(x-3)


n = int(input())
k = t(n)
print(k)

```



![image-20240225211900924](C:/Users/HUAWEI/AppData/Roaming/Typora/typora-user-images/image-20240225211900924.png)





### 58A. Chat room

greedy/strings, 1000, http://codeforces.com/problemset/problem/58/A



思路：



##### 代码

```python
s = input()
t = 'hello'

i = 0
tag = False
for j in range(len(s)):
    if s[j]==t[i]:
        i += 1
    if i==5:
        tag = True
        break
if tag:
    print('YES')
else:
    print('NO')
    
```



![image-20240225212416812](C:/Users/HUAWEI/AppData/Roaming/Typora/typora-user-images/image-20240225212416812.png)





### 118A. String Task

implementation/strings, 1000, http://codeforces.com/problemset/problem/118/A



思路：



##### 代码

```python
in_s = input().lower()
#print(in_s)
out_s = ''
v_list = ['a','o','y','e','u','i']
for i in range (len(in_s)):
    if not in_s[i] in v_list:
        out_s += '.'+in_s[i]
print(out_s)

```



![image-20240227150933594](C:/Users/HUAWEI/AppData/Roaming/Typora/typora-user-images/image-20240227150933594.png)





### 22359: Goldbach Conjecture

http://cs101.openjudge.cn/practice/22359/



思路：



##### 代码

```python
n = int(input())
prime = [0]*2 + [1]*(n-1)
for i in range(n+1):
    if prime[i]:
        for j in range(i*i, n+1, i):
            prime[j] = 0
for i in range(n):
    if prime[i] and prime[n-i]:
        a = i
        b = n - i
        break
print(a, b)

```



![image-20240227151734731](C:/Users/HUAWEI/AppData/Roaming/Typora/typora-user-images/image-20240227151734731.png)



### 23563: 多项式时间复杂度

http://cs101.openjudge.cn/practice/23563/



思路：



##### 代码

```python
s = input().split('+')

def com(x):
    if x[0]=='0':
        return 0
    else:
        a, b = x.split('^')
        return int(b)

s_com = [com(item) for item in s]
ans = max(s_com)
print('n^%d' % ans)

```



![image-20240227152125427](C:/Users/HUAWEI/AppData/Roaming/Typora/typora-user-images/image-20240227152125427.png)



### 24684: 直播计票

http://cs101.openjudge.cn/practice/24684/



思路：



##### 代码

```python
select = dict()
votes = [int(i) for i in input().split()]
for i in votes:
    if i in select:
        select[i] += 1
    else:
        select[i] = 1
M = max(select.values())
champion = [key for (key, value) in select.items() if value==M]
champion.sort()
print(*champion)

```



![image-20240301111331458](C:/Users/HUAWEI/AppData/Roaming/Typora/typora-user-images/image-20240301111331458.png)



## 2. 学习总结和收获

复习了上学期的学习内容，回忆了列表、字典的用法，感觉来了。



