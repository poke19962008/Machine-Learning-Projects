import tensorflow as tf
import numpy as np
import pickle

trainingIter = 1000
verbInterval = 10
trainSubset = -1
alpha = 0.7

weights = {
    'w1': tf.Variable(np.random.rand(28*28, 300)),
    'w2': tf.Variable(np.random.rand(300, 10))
}
biases = {
    'b1': tf.Variable(np.random.rand(300)),
    'b2': tf.Variable(np.random.rand(10))
}

def model(x, weights, biases):
    hl1 = tf.matmul(x, weights['w1']) + biases['b1']
    hl1 = tf.nn.relu(hl1)

    sm = tf.nn.softmax(tf.add(tf.matmul(hl1, weights['w2']), biases['b2']))
    return sm


if __name__ == '__main__':

    print "Unpacking Datasets.."
    with open('bin/notMNIST.pkl') as f:
        alphabTest = pickle.load(f)
        print "[SUCCESS] Unpacked Datasets."

        X = alphabTest["trainingSet"]
        X = X[:len(X)].reshape(len(X), 28*28)[:trainSubset, :] # Image Dimension is 28*28

        Y = alphabTest["trainingLabel"][:trainSubset]
        Y = [ (np.arange(10) == ord(x_)-ord('A')).astype(np.float64) for x_ in Y ]
        Y = np.array(Y)
        del alphabTest

        trainingLen = len(X)

        x = tf.placeholder(tf.float64, shape=(trainingLen, 28*28))
        y = tf.placeholder(tf.float64, shape=(trainingLen, 10))

        pred = model(x, weights, biases)
        cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(pred, y))

        optimizer = tf.train.GradientDescentOptimizer(learning_rate=alpha).minimize(cost)

        isCorrect = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(isCorrect, tf.float64))

        init = tf.initialize_all_variables()

        with tf.Session() as sess:
            sess.run(init)

            for i in xrange(trainingIter):
                c, a, _ = sess.run([cost, accuracy, optimizer], feed_dict={x: X, y: Y})

                if not i % verbInterval:
                    print "Iter: ", i, "Cost: ", c, "Accuracy: ", a
