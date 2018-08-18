
      #nural network class definition
class neuralNetwork:
    
    #initialise the neural network
    def_init_(self, inputnodes, hiddennodes, outputnodes, learningrate):
        #set number of nodes in each input, hidden, output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        
        #learning rate
        self.lr = learningrate
        pass
    #train the neural network
    def train():
        pass
    #query the neural network
    def query():
        pass
        
        
        #number of input, hidden and output notes
input_notes =3
hiden_nodes =3
output_nodes =3

#learning rate is 0.3
learning_rate = 0.3

#create instance of neural network
n= neuralNetwork (input_nodes, hidden_nodes, output_nodes, learning_rate)


import numpy
numpy.random.rand(3,2)


import numpy as np
numpy.random.rand(3,3)-0.5


import numpy as np

def get_tile_images(image, width=8, height=8):
    _nrows, _ncols, depth = image.shape
    _size = image.size
    _strides = image.strides

    nrows, _m = divmod(_nrows, height)
    ncols, _n = divmod(_ncols, width)
    if _m != 0 or _n != 0:
        return None

    return np.lib.stride_tricks.as_strided(
        np.ravel(image),
        shape=(nrows, ncols, height, width, depth),
        strides=(height * _strides[0], width * _strides[1], *_strides),
        writeable=False



        
        
        
