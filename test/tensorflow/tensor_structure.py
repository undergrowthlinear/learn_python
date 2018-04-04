'''
1.准备训练数据----输入/输出数据(数据即张量)
2.算法(机器学习或者深度学习算法)定义----占位符(用于替换传入的数据,例如训练时输入或者测试时的输入)替换输入/变量(与传统编程概念里面的变量不一样)定义(w/b)
3.算法训练----优化器使用损失函数,以损失函数最小(算法结果与占位符替换的输出变量进行对比)为目的,从而动态调节变量定义
4.算法应用----训练完成后进行实际测试
'''

import math

import tensorflow as tf

session = tf.Session()
# 1.准备训练数据
input = 5.
input_placeholder = tf.placeholder(dtype=tf.float32)
output = 50.
output_placeholder = tf.placeholder(dtype=tf.float32)
# 2.算法定义
w = tf.Variable(tf.constant(1.))
b = tf.Variable(tf.constant(1.))
algo = tf.add(tf.multiply(w, input_placeholder), b)
# 3.算法训练
# 最小二乘
loss = tf.square(tf.subtract(algo, output_placeholder))
train = tf.train.GradientDescentOptimizer(0.01).minimize(loss)
# 变量初始化
init = tf.global_variables_initializer()
session.run(init)
# 写tensorboard图表数据
#with tf.name_scope('loss'):
tf.summary.scalar('loss', loss)
merged = tf.summary.merge_all()
writer = tf.summary.FileWriter('tensor_log/struct_log2', session.graph)
# 开始训练
for i in range(50):
    session.run(train, feed_dict={input_placeholder: input,
                                  output_placeholder: output})
    w_val, b_val = (session.run(w), session.run(b))
    result = session.run(algo, feed_dict={input_placeholder: input})
    loss_result = session.run(loss, feed_dict={input_placeholder: input,
                                               output_placeholder: output})
    if i % 5 == 0:
        print("result=%s," % result, "loss_result=%s," % loss_result,
              "w_val=%s," % w_val, "input=%s," % str(input),
              "b_val=%s," % b_val)
        rs = session.run(merged, feed_dict={input_placeholder: input,
                                            output_placeholder: output})
        writer.add_summary(rs, i)
    if math.isclose(result, 50):
        break
# 4.算法应用
