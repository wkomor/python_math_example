#!/home/vitold/.virtualenvs/math_example/bin/python3.5
# -*- coding: utf-8 -*-
"""
title              :main
description        :
date               :10.10.16
"""
import numpy as np
from lin_alg import LinAlg
from plots import Plots

__author__ = 'Vitold Komorovski'


def set_matrix(inp):
    matrix = np.ones((3, 3), 'int32')
    matrix[0][0] *= inp
    matrix[1][1] *= inp
    return matrix


if __name__ == '__main__':
    print('Give me a number: \n')
    inp = input()
    matrix = set_matrix(inp)

    # Linear algebra
    # lin_alg = LinAlg(matrix)
    # lin_alg.get_det()
    # lin_alg.solve_lin()

    # Simple plots
    plt = Plots(matrix)
    # plt.display()
    # plt.gray_noise()
    #
    # Plot surfaces
    plt.plot_linear(matrix)
