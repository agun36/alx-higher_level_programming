#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    # Validate m_a and m_b as list of lists of integers or floats
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    # Validate that m_a and m_b are not empty
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # Validate that all elements of m_a and m_b are integers or floats
    for row in m_a:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_b should contain only integers or floats")

    # Validate that m_a and m_b are rectangular (rows of the same size)
    row_sizes_a = set(len(row) for row in m_a)
    row_sizes_b = set(len(row) for row in m_b)

    if len(row_sizes_a) > 1 or len(row_sizes_b) > 1:
        raise ValueError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Validate that m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            sum_product = 0
            for k in range(len(m_b)):
                sum_product += m_a[i][k] * m_b[k][j]
            row.append(sum_product)
        result.append(row)

    return result
