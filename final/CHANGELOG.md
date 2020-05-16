# CHANGELOG - Compared to the original implementation

- For better numerical stability
    - For [mlp](text_recognizer/networks/mlp.py) and [lenet](text_recognizer/networks/lenet.py) network, I discard the softmax activation at the final layer
    - Change [loss function](text_recognizer/models/base.py) from `CategoricalCrossentropy()` to `CategoricalCrossentropy(from_logits=True)`
    - Apply softmax for prediction to get probability in [character_model](text_recognizer/models/character_model.py)
- Fix deprecated API usage
    - Change from `fit_generator()` to `fit()` for [model training](text_recognizer/models/base.py)
- Change all tf1 syntax to tf2 syntax, ex: tf.XX -> tf.compat.v1.XX
- Fix duplicated model summary showing when running [`run_experiment`](training/run_experiment.py) function
- Allow getting fitting history form the [`run_experiment`](training/run_experiment.py) function
- Add [`plot_learning_curves`](training/util.py) utility function
- Add [02-character-model.ipynb](notebooks/02-character-model.ipynb) for demonstrating training a character model using mlp or lenet