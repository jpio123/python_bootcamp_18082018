from z4.mathematica.geometry import figures

def test_geometry_sq():
    assert figures.square_area(2) == 4
    assert figures.square_area(3) == 9

def test_geometry_tr():
    assert figures.triangle_area(3, 4, 5) == 6