"""Lightweight perceptron implementation shared across Quarto notes."""

from __future__ import annotations

import numpy as np

__all__ = ["Perceptron"]


class Perceptron:
    """Classic perceptron classifier with NumPy tensors."""

    def __init__(self, eta: float = 0.01, n_iter: int = 20, random_state: int = 1):
        """
        Parameters
        ----------
        eta:
            Learning rate between 0 and 1.
        n_iter:
            Number of training epochs.
        random_state:
            Seed for deterministic weight initialization.
        """

        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X: np.ndarray, y: np.ndarray) -> "Perceptron":
        """Fit training data and record misclassification counts per epoch."""

        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=X.shape[1])
        self.b_ = np.float64(0.0)
        self.errors_: list[int] = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_ += update * xi
                self.b_ += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X: np.ndarray) -> np.ndarray:
        """Compute the linear combination of inputs and weights."""

        return np.dot(X, self.w_) + self.b_

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Return the class label prediction for a given input."""

        return np.where(self.net_input(X) >= 0.0, 1, 0)

