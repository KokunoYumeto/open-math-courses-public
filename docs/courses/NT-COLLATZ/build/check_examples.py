"""Finite checks accompanying, not replacing, the lesson's written proofs.

Run with Python 3. No dependencies or network access.
"""
import json


def v2(n):
    assert type(n) is int and n > 0
    a = 0
    while n % 2 == 0:
        n //= 2
        a += 1
    return a


def ordinary(n):
    return 3 * n + 1 if n % 2 else n // 2


def shortcut(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def syracuse(m):
    assert m % 2 and m > 0
    return (3 * m + 1) // 2 ** v2(3 * m + 1)


def trajectory(f, n, steps):
    out = [n]
    for _ in range(steps):
        out.append(f(out[-1]))
    return out


def main():
    assert trajectory(ordinary, 3, 7) == [3, 10, 5, 16, 8, 4, 2, 1]
    assert trajectory(shortcut, 3, 5) == [3, 5, 8, 4, 2, 1]
    assert trajectory(ordinary, 40, 8) == [40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert trajectory(shortcut, 40, 7) == [40, 20, 10, 5, 8, 4, 2, 1]
    assert trajectory(ordinary, 7, 7) == [7, 22, 11, 34, 17, 52, 26, 13]
    assert trajectory(shortcut, 7, 4) == [7, 11, 17, 26, 13]
    checked_states = 0
    returns = 12
    for n in range(1, 1025):
        a = v2(n)
        odd = trajectory(syracuse, n // 2 ** a, returns)
        qs = [v2(3 * m + 1) for m in odd[:-1]]
        sums = [0]
        for q in qs:
            sums.append(sums[-1] + q)
        times_t = [a + q for q in sums]
        times_c = [a + j + q for j, q in enumerate(sums)]
        t = trajectory(shortcut, n, times_t[-1])
        c = trajectory(ordinary, n, times_c[-1])
        assert [i for i, value in enumerate(t) if value % 2] == times_t
        assert [i for i, value in enumerate(c) if value % 2] == times_c
        assert [t[i] for i in times_t] == odd == [c[i] for i in times_c]
        for j in range(returns + 1):
            assert min(t[:times_t[j]+1]) == min(odd[:j+1]) == min(c[:times_c[j]+1])
            assert sum(value % 2 for value in t[:times_t[j]]) == j
            assert sum(value % 2 for value in c[:times_c[j]]) == j
        rt = [2 ** (a - i) * odd[0] for i in range(a)]
        rc = rt.copy()
        for j, q in enumerate(qs):
            rt += [odd[j]] + [2 ** (q-r) * odd[j+1] for r in range(1, q)]
            rc += [odd[j]] + [2 ** (q+1-r) * odd[j+1] for r in range(1, q+1)]
        assert rt + [odd[-1]] == t
        assert rc + [odd[-1]] == c
        checked_states += len(t) + len(c)
    result = {
        'passed': True,
        'starting_integers': [1, 1024],
        'odd_return_steps_per_start': returns,
        'trajectory_states_compared': checked_states,
        'claims_tested': ['displayed examples', 'visit times', 'inverse counts', 'reconstruction', 'finite aligned minima'],
        'scope': 'Finite exact-integer checks only. General results are proved in the lesson, not inferred from this test.'
    }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
