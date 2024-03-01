# Assignment #2: 编程练习

Updated 0953 GMT+8 Feb 24, 2024

2024 spring, Complied by 雷逸鸣



**说明：**

1）The complete process to learn DSA from scratch can be broken into 4 parts:

- Learn about Time and Space complexities
- Learn the basics of individual Data Structures
- Learn the basics of Algorithms
- Practice Problems on DSA

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

### 27653: Fraction类

http://cs101.openjudge.cn/2024sp_routine/27653/



思路：



##### 代码

```python
class Fraction:
    def __init__(self, upper, lower):
        self.upper = upper
        self.lower = lower

    def __add__(self, other):
        n_lower = self.lower * other.lower
        n_upper = self.upper * other.lower + other.upper * self.lower
        return Fraction(n_upper, n_lower)

    def simplify(self):
        x: int
        y: int
        x, y = self.upper, self.lower
        while x!=0 and y!=0:
            x, y = max(x, y), min(x, y)
            x = x % y
        gcd = x if x!=0 else y
        return Fraction(self.upper//gcd, self.lower//gcd)


data = [int(i) for i in input().split()]
f1 = Fraction(data[0], data[1])
f2 = Fraction(data[2], data[3])
fs = f1 + f2
sfs = fs.simplify()
print('%d/%d' % (sfs.upper, sfs.lower))

```



![image-20240301114213995](C:/Users/HUAWEI/AppData/Roaming/Typora/typora-user-images/image-20240301114213995.png)





### 04110: 圣诞老人的礼物-Santa Clau’s Gifts

greedy/dp, http://cs101.openjudge.cn/practice/04110



思路：



##### 代码

```python
n, w = map(int, input().split())
candy = [list(map(int, input().split())) for _ in range(n)]
candy.sort(key=lambda o:o[0]/o[1], reverse=True)
value = 0
for i in range(n):
    if w >= candy[i][1]:
        value += candy[i][0]
        w -= candy[i][1]
    elif 0 < w < candy[i][1]:
        value += w * candy[i][0] / candy[i][1]
        # w = 0
        break
    else:
        break
print('%.1f' % value)

```



![image-20240301143604233](C:/Users/HUAWEI/AppData/Roaming/Typora/typora-user-images/image-20240301143604233.png)



### 18182: 打怪兽

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/



思路：



##### 代码

```python
nCases = int(input())
for _ in range(nCases):
    n, m, b = map(int, input().split())
    move = [list(map(int, input().split())) for _ in range(n)]
    move.sort(key=lambda x:(x[0], -x[1]))
    tm, t_current, move_left = -1, -1, m
    for ti, xi in move:
        if ti!=t_current:
            t_current = ti
            move_left = m-1
            b -= xi
        elif move_left > 0:
            move_left -= 1
            b -= xi
        else:
            pass
        if b <= 0:
            tm = ti
            break
    if tm>=0:
        print(tm)
    else:
        print('alive')

```





![image-20240301160503141](C:/Users/HUAWEI/AppData/Roaming/Typora/typora-user-images/image-20240301160503141.png)





### 230B. T-primes

binary search/implementation/math/number theory, 1300, http://codeforces.com/problemset/problem/230/B



思路：



##### 代码

```python
import math
 
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
 
n = int(input())
xl = list(map(int, input().split()))
for x in xl:
    if int(math.sqrt(x))**2==x:
        if is_prime(int(math.sqrt(x))):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

```



![image-20240301160757150](C:/Users/HUAWEI/AppData/Roaming/Typora/typora-user-images/image-20240301160757150.png)



### 1364A. XXXXX

brute force/data structures/number theory/two pointers, 1200, https://codeforces.com/problemset/problem/1364/A



思路：



##### 代码

```python
def sublenth():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i]
    if sum%x!=0:
        return n
    b_tag = 0
    c_tag = 0
    b=n
    c=n
    for i in range(n):
        if a[i]%x!=0:
            b = i+1
            b_tag = 1
            break
    for i in range(n):
        if a[n-i-1]%x!=0:
            c = i+1
            c_tag = 0
            break
    if b_tag==0 and c_tag==0:
        return -1
    else:
        return n-min(b, c)
    
t = int(input())
for _ in range(t):
    print(sublenth())

```



![image-20240301160830290](C:/Users/HUAWEI/AppData/Roaming/Typora/typora-user-images/image-20240301160830290.png)





### 18176: 2050年成绩计算

http://cs101.openjudge.cn/practice/18176/



思路：



##### 代码

```python
from math import sqrt
prime = [1]*2+[0]*9999
for i in range(101):
    if prime[i] == 0:
        for j in range(2*i, 10001, i):
            prime[j] = 1
#print(prime)
m, n = map(int, input().split())
for _ in range(m):
    score = [int(i) for i in input().split()]
    tmp = 0
    num = 0
    for item in score:
        gem = int(sqrt(item))
        if item==gem**2 and prime[gem]==0 and item!=0 and item !=1:
            tmp += item
            num += 1

    if tmp==0:
        print(0)
    else:
        GPA = tmp / len(score)
        print('%.2f'%GPA)

```



 ![image-20240301160941634](C:/Users/HUAWEI/AppData/Roaming/Typora/typora-user-images/image-20240301160941634.png)





## 2. 学习总结和收获

第二次做之前做过的题时，我感觉流畅了很多，也许是自己变厉害了，抑或之前做的题在脑海中还有印象，总之之前的努力终是有回报的，这学期继续！



