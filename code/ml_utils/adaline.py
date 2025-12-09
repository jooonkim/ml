"""Lightweight perceptron implementation shared across Quarto notes.

Notes from Cursor

Package structure: keep shared modules under code/ml_utils/ (or subpackages) and expose public APIs via __all__/__init__.py so posts can import cleanly (from ml_utils import Foo).
Path hygiene: tests or standalone scripts should add code/ to sys.path the same way the note helper does, so they work whether run from repo root or a subdirectory.
Type hints & docstrings: match the style in perceptron.py—brief module docstring, class docstring, annotated signatures—to keep IntelliSense useful inside Quarto/VS Code.
Tests with real data: put pytest-style tests in code/tests/ (mirroring modules) and cover both happy paths and failure modes; run python -m pytest code/tests or individual files before committing.
"""

from __future__ import annotations
from mimetypes import init

import numpy as np

__all__ = ["AdalineGD"]

class AdalineGD:
    """ADAptive LInear NEuron classifier.

    Parameters
    --------------

    eta: float. 
        This is the learning rate (between 0.0 and 1.0)
    n_iter: int
        Passes over the training dataset
    random_state: int
        Random number generator seed for random weight generalization
    
    Attributes
    ---------------
    w_: 1D-Array
        Weights after fitting
    b_: Scalar
        Bias after fitting
    losses_: list
        Mean Squared Error loss function values in each epoch
    """
    def __init__(self, eta=0.01, n_iter = 50, random_state = 1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def net_input(self, X):
        """Calculate net input"""
        return np.dot(X, self.w_) + self.b_

    def activation(self, X):
        """Compute linear activation"""
        return X
    
    def predict(self, X): 
        """Return class label after unit step"""
        return np.where(self.activation(self.net_input(X)) >= 0.5, 1, 0)

    def fit(self, X, y):
        """ Fit training data.

        Parameters
        -----------
        X: array-like, shape = [m_examples, n_features]
            Training vectors
            m_examples: # of examples
            n_features: # of features
        
        y: array-like, shape = [m_examples]
            Target values
        
        Returns
        -----------
        self: object
        """
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=X.shape[1])
        self.b_ = np.float_(0.)
        self.losses_ = []

        for i in range(self.n_iter): # for each epoch
            net_input = self.net_input(X) 
            output = self.activation(net_input)
            errors = (y - output)
            """This step is important!
            We are calculating the gradient based on the whole training set,
            not just evaluating each individual training example (as in the perceptron).
            """
            self.w_ += self.eta * 2.0 * X.T.dot(errors) / X.shape[0]
            self.b_ += self.eta * 2.0 * errors.mean() 
            loss = (errors**2).mean()
            self.losses_.append(loss)
        return self



