"""Demo for pre-commit hooks."""
import numpy as np


def euclidean(a: np.array, b: np.array) -> np.float:
    """
    Compute the eucledian distance between `a` and `b`.

    Parameters
    ----------
    a : np.array
        collection of n numeric elements
    b : np.array
        collection of n numeric elements

    Returns
    -------
    np.float
        The distance.
    """
    return np.linalg.norm(a - b)


if __name__ == "__main__":
    a = np.array(range(2, 8))
    b = np.array(range(4, 10))
    distance = euclidean(a, b)

    print(f"Distance between {a} and {b} = {distance:,.2f}")
