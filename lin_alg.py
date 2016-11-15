# -*- coding: utf-8 -*-
"""
title              :lin_alg
description        :
date               :27.10.16
"""
import numpy as np

__author__ = 'Vitold Komorovski'


class LinAlg(object):

    def __init__(self, matrix):
        self.matrix = matrix

    def get_det(self):
        """
        Determinant
        """
        d = np.linalg.det(self.matrix)
        print(self.matrix, '\n det = ', d)

    def solve_lin(self):
        """
        Solve the system of equations
        [0][0] * x + [0][1] * y  + [0][2] * z = 9
        [1][0] * x + [1][1] * y  + [1][2] * z = 8
        [2][0] * x + [2][1] * y  + [2][2] * z = 7

        """
        v = np.array([9, 8, 7])
        res = np.linalg.solve(self.matrix, v)
        print('roots = ', res)
        return res
