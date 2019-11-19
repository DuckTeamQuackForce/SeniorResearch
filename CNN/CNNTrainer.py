import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import matplotlib.pyplot as plt
import pickle
import datetime


log_dir="logs\\fit\\" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)

pickle_in = open("x_training.pickle","rb")
X_training = pickle.load(pickle_in)

pickle_in = open("y_training.pickle","rb")
y_training = pickle.load(pickle_in)

pickle_in = open("x_test.pickle","rb")
X_test = pickle.load(pickle_in)

pickle_in = open("y_test.pickle","rb")
y_test = pickle.load(pickle_in)

X_training = X_training/255.0
X_test = X_test/255.0

model = Sequential() # for initial run

model = Sequential()

model.add(Conv2D(32, (3, 3), activation='relu', input_shape=X_training.shape[1:]))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))

model.add(Flatten())

model.add(Dense(64, activation='relu'))

model.add(Dense(3, activation='softmax'))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(x=X_training, y=y_training, batch_size=64, epochs=10, 
                    validation_data=(X_training, y_training), 
                    callbacks=[tensorboard_callback])

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')

model.summary()

test_loss, test_acc = model.evaluate(X_test,  y_test, verbose=2)
print(test_acc)
model.save('my_model.h5')