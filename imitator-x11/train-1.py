import tensorflow as tf
import numpy as np
import re

ogrenme_dosyasi = input("Klonlanacak kişinin mesajlarının olduğu dosyayı giriniz:")

with open(ogrenme_dosyasi, 'r', encoding='utf-8') as f:
    messages = f.readlines()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

cleaned_messages = [clean_text(message) for message in messages]

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(cleaned_messages)
total_words = len(tokenizer.word_index) + 1

input_sequences = []
for line in cleaned_messages:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)

max_sequence_len = max([len(x) for x in input_sequences])
input_sequences = tf.keras.preprocessing.sequence.pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre')


input_sequences = np.array(input_sequences)
X, y = input_sequences[:,:-1], input_sequences[:,-1]
y = tf.keras.utils.to_categorical(y, num_classes=total_words)

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(total_words, 64, input_length=max_sequence_len-1),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
    tf.keras.layers.Dense(total_words, activation='softmax')
])


model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model_ismi = input("Model ismi ne olsun: ")
print("Tavsiye: İyi bir klonlama için programı üç kez çalıştırın ve birinin epoch değerini 20, diğerinin 40 bir diğerinin ise 60 olarak verin. 3 model üzerinden ilerlemenizi öneririm.")
model_epoch = int(input("Model epoch değeri kaç olsun:"))
history = model.fit(X, y, epochs=model_epoch, verbose=1)

model.save(model_ismi+'.h5')
