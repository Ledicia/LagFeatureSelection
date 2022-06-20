import tensorflow as tf
tfk = tf.keras
tfkl = tfk.layers


class CancelOut(tfkl.Layer):
    '''
    CancelOut layer, keras implementation -> element wise multiplication of NN inputs and parameters
    The idea is that those weights are multiplied by the inputs, therefore, the inputs will only contribute to 
    the target prediction if its weight is 0 or the activation function of its weigth is 0
    Besides, regularization loss can be added to regularize training
    '''
    def __init__(self, activation='sigmoid', cancelout_loss=False, lambda1=0.002, lambda2=0.001):
        super(CancelOut, self).__init__()
        self.lambda_1 = lambda1
        self.lambda_2 = lambda2
        self.cancelout_loss = cancelout_loss
        
        if activation == 'relu': self.activation = tf.nn.relu
        if activation == 'linear': self.activation = tfk.activations.linear
        if activation == 'sigmoid': self.activation = tf.math.sigmoid
        if activation == 'softmax': self.activation = tf.nn.softmax
        if activation == 'custom_relu': self.activation = custom_relu

    def build(self, input_shape):
        self.w = self.add_weight(
            shape=(input_shape[-1],),
            initializer=tf.keras.initializers.Constant(1),
            trainable=True,
        )
    def call(self, inputs):
        if self.cancelout_loss:
            self.add_loss( self.lambda_1 * tf.norm(self.w, ord=1) + self.lambda_2 * tf.norm(self.w, ord=2))
        return tf.math.multiply(inputs, self.activation(self.w))
    
    
    def get_config(self):
        return {"activation": self.activation}    
    
# @tf.function 
def custom_relu(x):
# 	return tf.math.minimum(1.0,tf.math.maximum(0.0, x))
    return tf.sigmoid(tf.nn.relu(x))-0.5
    
    
## FOR TIMESERIES ## 
class CancelOutRNN(tfkl.Layer):
    '''
    CancelOut layer, keras implementation -> element wise multiplication of NN inputs and parameters
    The idea is that those weights are multiplied by the inputs, therefore, the inputs will only contribute to 
    the target prediction if its weight is 0 or the activation function of its weigth is 0
    Besides, regularization loss can be added to regularize training
    '''
    def __init__(self, activation='sigmoid', cancelout_loss=False, lambda1=0.002, lambda2=0.001):
        super(CancelOutRNN, self).__init__()
        self.lambda_1 = lambda1
        self.lambda_2 = lambda2
        self.cancelout_loss = cancelout_loss
        
        if activation == 'relu': self.activation = tf.nn.relu
        if activation == 'linear': self.activation = tfk.activations.linear
        if activation == 'sigmoid': self.activation = tf.math.sigmoid
        if activation == 'softmax': self.activation = tf.nn.softmax
        if activation == 'custom_relu': self.activation = custom_relu

    def build(self, input_shape):
        self.w = self.add_weight(
            shape=(input_shape[1], input_shape[2]),
            initializer=tf.keras.initializers.Constant(1),
            trainable=True,
        )
    def call(self, inputs):
        if self.cancelout_loss:
            self.add_loss( self.lambda_1 * tf.norm(self.w, ord=1) + self.lambda_2 * tf.norm(self.w, ord=2))
        return tf.math.multiply(inputs, self.activation(self.w))
    
    
    def get_config(self):
        return {"activation": self.activation}   
    

    


