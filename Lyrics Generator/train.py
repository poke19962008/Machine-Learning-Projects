import tensorflow as tf
from tensorflow.contrib import rnn
import numpy as np

class model:
    def __init__(self):
        # Model Paramaters
        self.learningRate = 0.1
        self.trainingIters = 100
        self.seqLen = 530
        self.batchSize = 10

        # Network Parameters
        self.nHidden = 20
        self.vocabSize = 25071

    def cost(self, output, target):


    def graph(self):
        cell = tf.nn.rnn_cell.BasicLSTMCell(self.nHidden)

        x = tf.placeholder(tf.float32, [None]) # [NumSteps]
        y = tf.placeholder(tf.float32, [None]) # [NumSteps]
        seqLen = tf.placeholder(tf.int32)

        output, state = tf.nn.dynamic_rnn(cell, x, sequence_length=self.seqLen)

        # Softmax Layer
        with tf.variable_scope('softmax'):
            W = tf.get_variable("W", [self.nHidden, self.seqLen], initializer=tf.random_normal([self.nHidden, self.seqLen]))
            b = tf.get_variable("b", [self.seqLen], initializer=tf.random_normal([self.seqLen]))
        


if __name__ == '__main__':
