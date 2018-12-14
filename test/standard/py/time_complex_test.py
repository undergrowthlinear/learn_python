"""
* AA--Algorithm Analysis--算法分析
 * Algorithm--算法--对特定问题的解决步骤的描述，是有限的指令集合
 * 算法3特征：
 * 有穷性--算法在有限步骤内结束
 * 确定性--算法的每一步的含义都是确定的
 * 可行性--算法的每一步都是可执行的
 * 程序是用某种特定的程序设计语言对算法的具体实现
 * 算法分析的2主要衡量标准：
 * 时间复杂度--算法运行所花费的时间
 * 		Frequency Count--语句频度--语句可能重复执行的最大次数
 * 		Time Complexity--
 * 				算法中所有语句的语句频度t(n)
 * 				f(n)为当n趋于无穷大时，t(n)的同阶无穷大
 * 				f(n)即为t(n)中去除首项系数和低阶项，只考虑最高阶次，因为同阶无穷大为 lim t(n)/f(n)=C,即求导
 * 				T(n)=O(f(n))
 *      常见的9种时间复杂度：
 *      	常数阶O(1)<对数阶O(log2 n)<线性阶O(n)<线性对数阶O(nlog2 n)<平方阶O(n2)<立方阶O(n3)<k次方阶O(n k)<指数阶O(2 n)<阶乘O(n!)
 * 空间复杂度--算法所花费的存储空间大小
"""
import math

def cal_tc(n=100):
    print(1)
    print(math.log(n,2))
    print(n)
    print(n*math.log(n,2))
    print(n*n)
    print(math.pow(n,3))
    print(math.pow(n,10))
    print(math.pow(2,n))
    print(math.factorial(n))

cal_tc()