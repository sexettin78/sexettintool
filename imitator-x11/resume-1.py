import tensorflow as tf
import numpy as np
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text
ogrenme_dosyasi = input("Klonlamayı yaptığınız mesajların olduğu dosyayı giriniz:")
with open(ogrenme_dosyasi, 'r', encoding='utf-8') as f:
    messages = f.readlines()

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
model_ismi = input("Model dosyası giriniz (sonuna .h5 eklemeyi unutmayınız):")
model = tf.keras.models.load_model(model_ismi)

def generate_text(seed_text, next_words, max_sequence_len):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = tf.keras.preprocessing.sequence.pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted = model.predict(token_list, verbose=0)
        predicted_word_index = np.argmax(predicted, axis=1)[0]
        output_word = tokenizer.index_word[predicted_word_index]
        seed_text += " " + output_word
    return seed_text

while True:
    yazilacak_yazi = input("Modele birkaç kelime verin: ")
    uzunluk = int(input("Yazı uzunluğunu giriniz (1-15 arası idealdir): "))
    print(generate_text(yazilacak_yazi, uzunluk, max_sequence_len))
