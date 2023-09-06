#!/usr/bin/python3
"""
Lazy Matrix Multiplication
"""
from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrix

    Args:
        m_a: First matrix
        m_b: second matrix

    Returns:
        The result of multiply m_a by m_b

    """
    return matmul(m_a, m_b)
