def add_matrices(m1, m2):
    result = []
    for row_i in range(len(m1)):
        row = []
        for col_i in range(len(m1[row_i])):
            element = m1[row_i][col_i] + m2[row_i][col_i]
            row.append(element)
        result.append(row)
    return result


def sub_matrices(m1, m2):
    result = []
    for row_i in range(len(m1)):
        row = []
        for col_i in range(len(m1[row_i])):
            element = m1[row_i][col_i] - m2[row_i][col_i]
            row.append(element)
        result.append(row)
    return result