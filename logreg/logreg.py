import numpy as np

class LogisticRegression:
    """
    Logistic regression with Newton's Method

    Example usage:
        > clf = LogisticRegression()
        > clf.fit(x_train, y_train)
        > clf.predict(x_val)
    """
    def __init__(self, step_size=0.01, max_iter=1000000, eps=1e-5,
                 theta_0=None, verbose=True):
        """
        Args:
            step_size: Step size for iterative solvers only.
            max_iter: Maximum number of iterations for the solver.
            eps: Threshold for determining convergence.
            theta_0: Initial guess for theta. If None, use the zero vector.
            verbose: Print loss values during training.
        """
        self.theta = theta_0
        self.step_size = step_size
        self.max_iter = max_iter
        self.eps = eps
        self.verbose = verbose

    def sigmoid(self, z):
        """
        Sigmoid Function
        
        Args:
            z: input to sigmoid function
        """
        return 1 / (1 + np.exp(-z))
    
    def fit (self, x, y):
        """
        Run Newton's Method to minimize J(theta) for logistic regression.

        Args:
            x: Training example inputs. Shape (n_examples, dim).
            y: Training example labels. Shape (n_examples,).
        """
        n, p = x.shape

        if self.theta is None:
            self.theta = np.zeros(p)

        for i in range(self.max_iter):
            h = self.sigmoid(x @ self.theta)
            grad = -1 / n * x.T @ (y - h)
            hess = 1 / n * x.T * (h * (1 - h)) @ x

            if self.verbose:
                loss = -np.mean(y * np.log(h + self.eps) + (1 - y) * np.log(1 - h + self.eps))
                print(f"Iteration {i}: Loss = {loss}")

            theta = self.theta - np.linalg.inv(hess) @ grad

            if np.linalg.norm(theta - self.theta, ord=1) < self.eps:
                self.theta = theta
                break
            else:
                self.theta = theta

    def predict(self, x):
        """Return predicted probabilities given new inputs x.

        Args:
            x: Inputs of shape (n_examples, dim).

        Returns:
            Outputs of shape (n_examples,).
        """
        return self.sigmoid(x @ self.theta)