#!/usr/bin/python3
"""
Defines lazy_matrix functions
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ calculates the matrix multiplication by two matrix"""
    return numpy.matmul(m_a, m_b)
