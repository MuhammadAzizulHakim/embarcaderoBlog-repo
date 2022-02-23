import tensorflow as tf
 
# Load and prepare the dataset
mnist = tf.keras.datasets.mnist
 
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
 
# Build the tf.keras.Sequential model by stacking layers.
# Choose an optimizer and loss function for training:
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])
 
predictions = model(x_train[:1]).numpy()
predictions
 
# Convert the logits to probabilities for each class
tf.nn.softmax(predictions).numpy()
 
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
 
loss_fn(y_train[:1], predictions).numpy()
 
# Compile the deep learning model
model.compile(optimizer='adam',
                loss=loss_fn,
                metrics=['accuracy'])
 
# Fitting, adjust the model parameters to minimize the loss:
model.fit(x_train, y_train, epochs=5)
 
# Evaluate the model
model.evaluate(x_test,  y_test, verbose=2)
 
# Attach the softmax layer
probability_model = tf.keras.Sequential([
  model,
  tf.keras.layers.Softmax()
])
 
probability_model(x_test[:5])