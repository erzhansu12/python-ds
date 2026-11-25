# ✍️ MNIST Handwritten Digit Classifier

A neural network that recognises handwritten digits (0–9) from the MNIST dataset,
with the best model saved as a checkpoint to Google Drive during training.

📓 Notebook: [`mnist_digit_classifier.ipynb`](mnist_digit_classifier.ipynb)

## Result

**97.99 % accuracy on the test set** (the task required > 96 %).

| Epoch | Train acc | Test acc |
|---|---|---|
| 1 | 90.79 % | 94.25 % |
| 5 | 98.13 % | 97.65 % |
| 9 | 99.22 % | **97.99 %** ← best checkpoint |
| 10 | 99.37 % | 97.85 % |

## What's inside

- **Data:** 60,000 training and 10,000 test images (28×28), loaded with `tf.keras.datasets.mnist`,
  scaled to [0, 1] and flattened to 784-value vectors
- **Model** (PyTorch): `Linear(784 → 128) → ReLU → Linear(128 → 10)`
- **Training:** Adam (lr = 0.001), cross-entropy loss, batch size 64, 10 epochs
- **Checkpointing:** after each epoch the model is saved to Google Drive if its test accuracy
  is the best so far — protection against losing progress when Colab disconnects
- **Check:** the best checkpoint is reloaded and re-evaluated on the test set
- **Plots:** sample digits, plus accuracy and loss curves for train vs test

## Tech stack
`PyTorch` · `TensorFlow / Keras` (dataset) · `numpy` · `matplotlib` · Google Colab

## How to run
Open in Google Colab. The notebook mounts Google Drive to save checkpoints
to `My Drive/Skillbox/model_1/` — change `path` in cell 7 to save somewhere else.
