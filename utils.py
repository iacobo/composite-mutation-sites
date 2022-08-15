"""
Helper functions for main notebook.
"""


def model(Vt, Et, theta, pi, B, i, j, L):
    """
    Returns model output.
    """

    output = (
        -(
            pow(theta, 2)
            * ((pi[i, j] - L) * (-L + pi[i, j] + 1))
            * Vt
            / 2
            * B
            * (B * pow((Et * theta - 1), 2) + pow(theta, 2) * Vt)
        )
        + (
            (pi[i, j] * theta * (pi[i, j] - L) * Vt)
            / B
            * (B * Et * (Et * theta + 1) + theta * Vt)
        )
        - (((pi[i, j] - 1) * pi[i, j] * Vt) / 2 * B * (B * pow(Et, 2) + Vt))
    )

    return output
