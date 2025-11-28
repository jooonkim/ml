from pathlib import Path
import sys

import numpy as np

CODE_DIR = Path(__file__).resolve().parents[1]
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from ml_utils import Perceptron


def test_perceptron_learns_and_gate():
    # 1) Define the AND dataset
    X = np.array(
        [
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1],
        ]
    )
    y = np.array([0, 0, 0, 1])

    # 2) Create the model
    clf = Perceptron(eta=0.1, n_iter=20, random_state=1)

    # 3) Train on the dataset
    clf.fit(X, y)

    # 4) Check predictions
    preds = clf.predict(X)

    # 5) Assert predictions match the true labels
    assert np.array_equal(preds, y)


if __name__ == "__main__":
    test_perceptron_learns_and_gate()
    print("AND gate test passed")

