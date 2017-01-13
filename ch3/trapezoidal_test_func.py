# -*- coding: utf-8 -*-

from trapezoidal import trapezoidal

def test_trapezoidal():
    f = lambda x: 2*x**3
    a = 1
    b = 3
    n = 2
    expected = 40
    computed = trapezoidal(f, a, b, n)
    rel_error = abs(expected - computed)
    tol = 1E-15
    success = rel_error < tol
    msg = 'погрешность = %.17f больше допуска = %.17f' % (rel_error, tol)
    assert success, msg