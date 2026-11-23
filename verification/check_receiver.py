"""Numerical checks for the finite receiver and comparison formulas."""
from cmath import exp
from itertools import combinations
from math import acos, cos, isclose, pi, sin, sqrt


def phasor(angle):
    return exp(1j * angle)


def dot(left, right):
    return sum(a.conjugate() * b for a, b in zip(left, right))


def discrete_analyzers():
    for blocks in range(2, 33, 2):
        eta = pi / (2 * blocks)
        for block in range(blocks):
            theta = 2 * pi * block / blocks
            u = (1 / sqrt(2), 1 / sqrt(2))
            v = tuple(phasor(theta + sign * eta) / sqrt(2) for sign in (-1, 1))
            v_plus = tuple(phasor(sign * eta / 2) / sqrt(2) for sign in (-1, 1))
            v_minus = (1j * v_plus[0], -1j * v_plus[1])
            assert abs(dot(v_plus, v_minus)) < 1e-13
            assert abs(dot(v_plus, v) / dot(v_plus, u) - phasor(theta)) < 1e-12
            assert abs(dot(v_minus, v) / dot(v_minus, u) + phasor(theta)) < 1e-12
            for early, late, overlap in ((1.0, 1.0, 1.0), (.7, .9, .95), (0, .9, .4)):
                cross = sqrt(early * late) * overlap * phasor(-eta)
                mapped_v = (cross * v[1], cross.conjugate() * v[0])
                actual = (phasor(-theta) * dot(u, mapped_v)).real
                assert isclose(actual, sqrt(early * late) * overlap, abs_tol=1e-13)


def timing_partitions():
    for blocks in range(2, 8):
        eta = pi / (2 * blocks)
        for early in (0, .05, .3, .65, 1.0):
            late = 1.0
            points = [phasor(2*j*eta) * (early if j % 2 == 0 else late)
                      for j in range(2*blocks)]
            best = 0.0
            for cuts in combinations(range(2*blocks), blocks):
                ends = cuts[1:] + (cuts[0] + 2*blocks,)
                score = sum(abs(sum(points[j % len(points)] for j in range(a, b)))
                            for a, b in zip(cuts, ends))
                best = max(best, score)
            balance = 2*sqrt(early*late)/(early+late)
            formula = sqrt(1 - balance**2*sin(eta)**2)
            assert isclose(best/(blocks*(early+late)), formula, abs_tol=1e-12)


def chord_examples():
    for label_count in range(2, 17):
        half_gap = pi / label_count
        h = cos(half_gap)
        for fraction in (.01, .2, .5, .9):
            x = h + (1-h)*fraction
            height = sqrt(1-x*x)
            target_y = .4 * height
            p = (1+target_y/height)/2
            upper, lower = x+1j*height, x-1j*height
            assert abs(p*upper + (1-p)*lower - complex(x, target_y)) < 1e-13
            primal = (p*phasor(-half_gap)*upper+(1-p)*phasor(half_gap)*lower).real
            beta = x*sin(half_gap)/height-h
            dual = sqrt(1+2*beta*h+beta*beta)-beta*x
            assert isclose(primal, dual, abs_tol=1e-12)


def span_pairs():
    for labels in range(2, 65):
        alpha = pi/labels
        norm = 1-cos(alpha)
        tau_limit = acos((1+cos(alpha))/2)/pi
        for j in range(101):
            q = j/100
            a = acos(1-q*norm)
            b = acos(1-(1-q)*norm)
            assert isclose(cos(a)+cos(b), 1+cos(alpha), abs_tol=1e-13)
            assert (a+b)/(2*pi) <= tau_limit + 1e-13 < 1/labels
    assert isclose((acos(.5)+acos(0))/(2*pi), 5/12, abs_tol=1e-13)


if __name__ == "__main__":
    discrete_analyzers()
    print("Two-port receivers and click coherence: passed for even K=2..32")
    timing_partitions()
    print("Weighted timing optimum: passed for K=2..7 and five loss ratios")
    chord_examples()
    print("Fixed-label chord primal/dual: passed for 60 cases")
    span_pairs()
    print("Overlapping span bound: passed for 63 label counts and 101 quantiles")
