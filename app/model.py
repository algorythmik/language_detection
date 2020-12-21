import os
import pickle

import tensorflow as tf

model_dir = os.path.join("app", "models")


class LangClassifier:

    MAX_SEQUENCE_LENGTH = 100

    _classes = {0: "DA", 1: "NO", 2: "SE"}

    def __init__(self):
        with open(os.path.join(model_dir, "tokenizer.pickle"), "rb") as handle:
            tokenizer = pickle.load(handle)
        self.tokenizer = tokenizer
        self.model = tf.keras.models.load_model(
            os.path.join(model_dir, "saved_model.h5")
        )

    def predict(self, text):
        tokenized = self.tokenizer.texts_to_sequences([text])
        padded_seq = tf.keras.preprocessing.sequence.pad_sequences(
            tokenized, maxlen=self.MAX_SEQUENCE_LENGTH
        )
        return {
            "perdiction": self._classes[
                self.model.predict_classes(padded_seq).squeeze().item()
            ]
        }
