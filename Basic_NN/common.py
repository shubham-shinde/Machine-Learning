import numpy as np
from keras.datasets import mnist

def norm_max_pix_div(x):
    return x/255

wt_init_types = ['random', 'random_small', 'zeros', 'ones', 'negative_positive', 'negative']

def initialize_weights_by_type(shape, wt_init_type, mul=0.01):
    print(shape, wt_init_type)
    if wt_init_type == 'random':
        return np.random.random((shape[0], shape[1]))
    elif wt_init_type == 'random_small':
        return np.random.random((shape[0], shape[1])) * mul
    elif wt_init_type == 'zeros':
        return np.zeros((shape[0], shape[1]))
    elif wt_init_type == 'ones':
        return np.ones((shape[0], shape[1]))
    elif wt_init_type == 'negative_positive':
        return np.random.random((shape[0], shape[1])) * 2 - 1
    elif wt_init_type == 'negative':
        return np.random.random((shape[0], shape[1])) * -1
    else:
        raise ValueError('Unknown weight initialization type')

def initialize_weights(input_size, layers, mul):
    weights = []
    for i in range(len(layers)):
        nodes = layers[i]['nodes']
        W_init_type = layers[i]['W_init_type']
        b_init_type = layers[i]['b_init_type']
        obj = {}
        obj['W'] = initialize_weights_by_type((nodes, input_size if i == 0 else layers[i-1]['nodes']), W_init_type, mul)
        obj['b'] = initialize_weights_by_type((nodes, 1), b_init_type)
        weights.append(obj)
    return weights

def load_MNIST_data():
    data = mnist.load_data()
    (X_train, y_train), (X_test, y_test) = data
    train_examples = X_train.shape[0]
    test_examples = X_test.shape[0]
    return X_train.reshape(train_examples, -1).T, y_train.reshape(train_examples, -1).T, X_test.reshape(test_examples, -1).T, y_test.reshape(test_examples, -1).T

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    p = np.exp(x)
    n = np.exp(-x)
    return (p - n) / (p + n)

def relu(x):
    return np.maximum(0, x)

def backward_sigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))

def backward_tanh(x):
    return 1 - tanh(x) ** 2

def backward_relu(x):
    return np.where(x > 0, 1, 0)

def Y_to_y(y):
    Y = np.zeros((y.shape[1], 10))
    for i in range(len(Y)):
        Y[i][y.T[i]] = 1
    return Y.T

def some():
    wandb.init(project="mnist", entity="kaizen", config = config)
