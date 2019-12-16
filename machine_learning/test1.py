#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# numpy 基础科学计算库
import numpy

i = numpy.array([[1,2,3],[4,5,6]])
print("i:\n{}".format(i))

# scipy 科学计算工具集
from scipy import sparse

matrix = numpy.eye(3)
# 生成3阶对角阵
sparse_matrix = sparse.csr_matrix(matrix)
# 把numpy数组转化为CSR格式的scipy稀疏矩阵

print("对角矩阵：\n{}".format(matrix))
# 打印对角矩阵
print("\nsparse matrix:\n{}".format(sparse_matrix))
# 打印稀疏矩阵

# pandas 数据分析工具

import pandas
data = {"Name":["seanOY","sillyM"],
        "City":["A City","Z City"],
        "Age":["22","22"]}
data_frame = pandas.DataFrame(data)
#display(data_frame) 只能在jupyter中执行

