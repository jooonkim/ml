import numpy as np 

class Perceptron:
    """Perceptron classifier.

    Parameters

    eta: float, learning rate between 0.0 and 1.0
    n_iter: int, epochs
    random_state: int, random number generator (RNG) for random weight initialization

    Attributes

    w_: 1d-array, weights after fitting
    b_: scalar, bias unit after fitting
    errors_: list, number of misclassifications aka updates in each epoch
    """

    def __init__(self, eta=0.01, n_iter = 20, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        """Fit training data.

        Parameters 

        X: array, features
        y: array, target values

        Returns

        self: object
        """
        rgen = np.random.RandomState(self.random_state) # random number generator
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=X.shape[1]) # initializes weight vector
        # np.random.normal samples from a Gaussian (== normal distribution) with mean (loc = 0.0, no bias towards + or -) and std (scale = 0.01, weights begin near 0)
        # size == the number of columns in X
        self.b_ = np.float_(0.) # initializes bias value to 0.0
        self.errors_ = [] # logs how many samples were misclassified at each epoch

        for _ in range(self.n_iter): # repeats the training pass n_iter times
            errors = 0 # resets counter at start of each epoch
            for xi, target in zip(X, y): # zip pairs each feature vector xi from X with the corresponding target label in y
                update = self.eta * (target - self.predict(xi)) # update will be 0 if there was no error
                self.w_ += update * xi
                self.b_ += update
                errors += int(update != 0.0) # converts Boolean (update != 0.0) to 1 if True and 0 if False
            self.errors_.append(errors)
        return self
    
    def net_input(self, X):
        """Calculate net input"""
        return np.dot(X, self.w_) + self.b_ # np.dot(a, b) is the dot product of a & b
    
    def predict(self, X):
        """Return class label"""
        return np.where(self.net_input(X) >= 0.0, 1, 0) # np.where(... >= 0.0, 1, 0) returns 1 when the net input >= 0.0, 0 otherwise
