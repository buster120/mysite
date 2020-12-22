import matplotlib.pyplot as plt
# x = []
# y = []
# b = -5.0
# for i in range(100):
#     a = 1.0/(1+b*b)
#     x.append(b)
#     y.append(a)
#     b += 10.0/100
# plt.plot(x, y, 'g', label='y = 1/(1+x**2)')
# plt.title("function")
# plt.xlabel('x')
# plt.ylabel('y = 1/(1+x**2)')
# plt.legend()#加上图例，右上角的曲线的图例
# plt.show()
'''
绘制L图像，拉格朗日插值函数
'''


def Lagrange(n):
    """
    绘制拉格朗日的函数
    :param n: 输入的需要拟合的点的个数，在[-5,5]区间上，将其等距进行分割。确定的函数图像为：y = 1/(1+x^2)
    :return: null
    注：此时书写的for i in range(100)逻辑循环有问题
    """
    x_i = -5
    x = []
    y = []
    t = -5.0

    t_all = []
    l_t_all = []
    for i in range(n+1):
        y_i = 1.0/(1+x_i*x_i)
        x.append(x_i)
        x_i += 10.0 / float(n)
        y.append(y_i)
    for i in range(100+1):
        l_t = 0
        for x_k, y_k in zip(x,y):
            a = 1.0
            for x_i in x:
                if x_i != x_k:#
                    a *= ((t-x_i)/(x_k-x_i))
            l_t += (a*y_k) # 此时只求得一个相应的拉格朗日插值点
            print(l_t)
        t_all.append(t)
        t += 10.0/100
        l_t_all.append(l_t)
    """
    在此绘制原先的函数进行函数图像的对比
    """
s = []
p = []
o = -5.0
for i in range(100+1):
    w = 1.0/(1+o*o)
    s.append(o)
    p.append(w)
    o += 10.0/100
plt.plot(t_all, l_t_all, 'r', label='Lagrange n = '+str(n+1))
plt.plot(s, p, 'b', label='y = 1/(1+x**2)')
plt.title("function")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()  # 加上图例，右上角的曲线的图例
plt.show()



Lagrange(10)