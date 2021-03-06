# -*- coding:utf-8 -*-
"""
@Time: 2020/09/29 19:39
@Author: Shanshan Wang
@Version: Python 3.7
@Function:
"""
import torch
import random
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
import numpy as np


import torch

batch_size = 5
nb_digits = 10
# Dummy input that HAS to be 2D for the scatter (you can use view(-1,1) if needed)
y = torch.LongTensor(batch_size,1).random_() % nb_digits
# One hot encoding buffer that you create out of the loop and just keep reusing
y_onehot = torch.FloatTensor(batch_size, nb_digits)

# In your for loop
y_onehot.zero_()
y_onehot.scatter_(1, y, 1)

print(y)
print(y_onehot)



