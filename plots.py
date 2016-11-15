# -*- coding: utf-8 -*-
"""
title              :graph
description        :
date               :27.10.16
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from lin_alg import LinAlg

__author__ = 'Vitold Komorovski'


class Plots(object):

    def __init__(self, matrix):
        self.matrix = matrix

    def display(self):
        tup = (self.matrix, self.matrix, self.matrix)
        m = np.column_stack(tup)
        m = np.vstack((m, m, m))
        plt.matshow(m)
        plt.show()

    def gray_noise(self):
        # Display a random matrix with a specified figure number and a grayscale
        # colormap
        plt.matshow(np.random.rand(64, 64), fignum=100, cmap=plt.cm.gray)

        plt.show()

    def plot_linear(self, matrix):
        """
        Display solution of the equations system
        :param matrix: initial matrix
        """
        ln_alg = LinAlg(matrix)
        roots = ln_alg.solve_lin()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x, y = np.linspace(-10, 10, 10), np.linspace(-10, 10, 10)
        X, Y = np.meshgrid(x, y)
        Z1 = 9 - 5 * X + Y
        Z2 = 8 - X + 5 * Y
        Z3 = 7 - X + Y

        ax.plot_surface(X, Y, Z1, alpha=0.5, rstride=100, cstride=100)
        ax.plot_surface(X, Y, Z2, alpha=0.5, rstride=100, cstride=100)
        ax.plot_surface(X, Y, Z3, alpha=0.5, facecolors='g', rstride=100,
                        cstride=100)
        ax.plot((roots[0],), (roots[1]), (roots[2],), lw=2, c='k', marker='o')

        plt.show()
