#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 10:01
# @Author  : ShiXin398
# @Site    : 
# @File    : main.py
# @Software: PyCharm

import tensorflow as tf

a = tf.constant([1.2, 2.0], name="a")
b = tf.constant([3.0, 4.1], name="b")

sess = tf.Session()
result = sess.run(a + b)

print("a + b: ", result)