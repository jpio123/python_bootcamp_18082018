from z4.mathematica.algebra import matrices as m

def test_matrices():

    m1 = [[1, 3, 5], [2, 4, 6], [10, 17, 19]]
    m2 = [[1, 1, 1],[2, 2, 2], [3, 3, 3]]

    assert m.add_matrices(m1, m2) == [[2, 4, 6], [4, 6, 8], [13, 20, 22]]
    assert m.sub_matrices(m1, m2) == [[0, 2, 4], [0, 2, 4], [7, 14, 16]]

