import numpy as np

class SVM:

    def __init__(self, learning_rate, lambada_param,n_iters):
        self.learning_rate = learning_rate
        self.lambada_param = lambada_param
        self.n_iters = n_iters
        self.w =  None
        self.b = None

    def fit(self, X, y):
        if y <= 0:
            y_ = -1
        else:
            y_ = 1
        n_samples , n_features = X.shape
        self.w = n_features
        for i in range(self.n_iters):
            for i, x_i in enumerate(X):
                condition = y_[i] * (np.dot(x_i, self.w) - self.b)
                if condition >= 1:
                    self.w = self.w - (self.learning_rate * (2 * self.learning_rate * self.w))
                else:
                    self.w = self.w - self.learning_rate * ((2 * self.learning_rate * self.w) - (y_[i] * x_i))
                    self.b = self.b - (self.learning_rate * y_[i])   

        






        

    def predict(self, X):
        output = np.dot(X, self.w) - self.b
        return np.sign(output)