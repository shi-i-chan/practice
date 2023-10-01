import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from tensorflow.keras import layers

from numpy.typing import NDArray
from typing import Tuple, NoReturn
from tensorflow.keras import Model
from tensorflow.keras import optimizers


def limit_memory(gb: int) -> NoReturn:
    import tensorflow as tf
    from tensorflow.config.experimental import set_virtual_device_configuration
    from tensorflow.config.experimental import VirtualDeviceConfiguration

    gpus = tf.config.list_physical_devices('GPU')

    if gpus:
        for gpu in gpus:
            set_virtual_device_configuration(gpu, [VirtualDeviceConfiguration(memory_limit=gb * 1024)])



class DefAutoencoder:
    def __init__(self,
                 x_train_in: NDArray,
                 x_test_in: NDArray,
                 x_train_out: NDArray = None,
                 x_test_out: NDArray = None,
                 optimizer: str = 'Adam',
                 learning_rate: float = 1e-3,
                 loss: str = 'mse',
                 activation: str = 'relu',
                ):
        self.optimizer: optimizers = getattr(optimizers, optimizer)(learning_rate=learning_rate)
        self.loss: str = loss
        self.activation: str = activation
        self.x_train_in: NDArray = x_train_in
        self.x_train_out: NDArray = x_train_in if x_train_out is None else x_train_out
        self.x_test_in: NDArray = x_test_in
        self.x_test_out: NDArray = x_test_in if x_test_out is None else x_test_out
        self.encoder: Model = None
        self.decoder: Model = None
        self.autoencoder: Model = None

    def compile(self) -> NoReturn:
        self.autoencoder.compile(loss=self.loss, optimizer=self.optimizer)
        
    def fit(self,
            epochs: int,
            batch_size: int) -> NoReturn:
        self.autoencoder.fit(self.x_train_in,
                             self.x_train_out,
                             validation_data=(self.x_test_in, self.x_test_out),
                             epochs=epochs,
                             batch_size=batch_size)
        
    def encode(self, data: NDArray) -> NDArray:
        if self.encoder is None:
            self.get_encoder()
        return self.encoder.predict(data)

    def decode(self, data: NDArray) -> NDArray:
        if self.decoder is None:
            self.get_decoder()
        return self.decoder.predict(data)
    
    def show_examples(self, n: int = 10) -> NoReturn:
        decoded_imgs = self.autoencoder.predict(self.x_test_in)
        plt.figure(figsize=(20, 4))
        for i in range(n):
            ax = plt.subplot(2, n, i + 1)
            plt.imshow(self.x_test_in[i].reshape(28, 28))
            plt.gray()
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)

            ax = plt.subplot(2, n, i + 1 + n)
            plt.imshow(decoded_imgs[i].reshape(28, 28))
            plt.gray()
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
        plt.show()


class DenseAutoencoder(DefAutoencoder):
    def __init__(self,
                 input_shape: int,
                 encoding_dim: int,
                 layers_config: dict,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.input_shape: int = input_shape
        self.encoding_dim: int = encoding_dim
        self.layers_config: dict = layers_config

    def init_model(self) -> Model:
        input_ = keras.Input(shape=(self.input_shape,))
        autoencoder = input_
        for n_units in self.layers_config['encoder_layers']:
            autoencoder = layers.Dense(n_units, activation=self.activation)(autoencoder)

        autoencoder = layers.Dense(self.encoding_dim, activation=self.activation)(autoencoder)

        for n_units in self.layers_config['decoder_layers']:
            autoencoder = layers.Dense(n_units, activation=self.activation)(autoencoder)

        autoencoder = layers.Dense(self.input_shape, activation='sigmoid')(autoencoder)

        self.autoencoder = keras.Model(input_, autoencoder)
        return self

    def get_encoder(self) -> Model:
        input_layer = keras.Input(shape=(self.input_shape,))
        encoder = input_layer
        for layer in self.autoencoder.layers[1: len(self.layers_config['encoder_layers']) + 2]:
            encoder = layer(encoder)
        self.encoder = keras.Model(input_layer, encoder)
        return self.encoder

    def get_decoder(self) -> Model:
        input_layer = keras.Input(shape=(self.encoding_dim,))
        decoder = input_layer
        for layer in self.autoencoder.layers[len(self.layers_config['decoder_layers']) + 2:]:
            decoder = layer(decoder)
        self.decoder = keras.Model(input_layer, decoder)
        return self.decoder


class CNNAutoencoder(DefAutoencoder):
    def __init__(self,
                 input_shape: Tuple[int],
                 layers_config: dict,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_shape: Tuple[int] = input_shape
        self.layers_config: dict = layers_config
    
        self.encoder_len: int = len(self.layers_config['encoder_layers'])
        self.decoder_len: int = len(self.layers_config['decoder_layers'])
    
    def init_model(self) -> Model:
        input_ = keras.layers.Input(shape=self.input_shape)
        autoencoder = input_
        for n_units in self.layers_config['encoder_layers']:
            autoencoder = layers.Conv2D(n_units, (3, 3), activation=self.activation, padding='same')(autoencoder)
            autoencoder = layers.MaxPooling2D((2, 2), padding='same')(autoencoder)

        for idx, n_units in enumerate(self.layers_config['decoder_layers'], 1):
            autoencoder = layers.Conv2D(n_units, (3, 3), activation=self.activation,
                                        padding='same' if idx < self.decoder_len else 'valid')(autoencoder)
            autoencoder = layers.UpSampling2D((2, 2))(autoencoder)

        autoencoder = layers.Conv2D(1, (3, 3), activation='sigmoid', padding='same')(autoencoder)
        self.autoencoder = keras.Model(input_, autoencoder)
        return self
    
    def get_encoder(self):
        input_img = keras.Input(shape=self.input_shape)
        encoder = input_img
        for layer in self.autoencoder.layers[1: self.encoder_len * 2 + 1]:
            encoder = layer(encoder)
        self.encoder = keras.Model(input_img, encoder)
        return self.encoder

    def get_decoder(self):
        decoder_input = keras.Input(shape=self.encoder.layers[-1].output_shape[1:])
        decoder = decoder_input
        for layer in self.autoencoder.layers[self.encoder_len * 2 + 1:]:
            decoder = layer(decoder)
        self.decoder = keras.Model(decoder_input, decoder)
        return self.decoder

