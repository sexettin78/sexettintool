import pandas as pd
import numpy as np
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

def load_passwords(file_path):
    with open(file_path, encoding="latin-1") as file:
        passwords = file.readlines()
    passwords = [password.strip() for password in passwords]
    return passwords

def clean_passwords(passwords):
    cleaned_passwords = [password for password in passwords if password and len(password) > 3]
    return cleaned_passwords

def extract_features(password):
    length = len(password)
    digit_count = len(re.findall(r"\d", password))
    upper_count = len(re.findall(r"[A-Z]", password))
    lower_count = len(re.findall(r"[a-z]", password))
    symbol_count = len(re.findall(r"[!@#$%^&*(),.?\":{}|<>]", password))
    return [length, digit_count, upper_count, lower_count, symbol_count]

def create_feature_matrix(passwords):
    features = [extract_features(password) for password in passwords]
    return np.array(features)

def train_model(X, y):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

def main(file_path, model_path=None):
    if model_path and os.path.exists(model_path):
        print(f"Mevcut model '{model_path}' yüklendi.")
        model = joblib.load(model_path)
    else:
        print("Yeni bir model eğitiliyor...")
        passwords = load_passwords(file_path)
        cleaned_passwords = clean_passwords(passwords)

        weak_passwords = cleaned_passwords[:10000]  
        strong_passwords = [pwd for pwd in cleaned_passwords if len(pwd) > 8][:10000]  

        passwords = weak_passwords + strong_passwords
        labels = [0] * len(weak_passwords) + [1] * len(strong_passwords) 

        X = create_feature_matrix(passwords)
        y = np.array(labels)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = train_model(X_train, y_train)

        y_pred = model.predict(X_test)
        print(classification_report(y_test, y_pred))
        model_ismi = input("Model ismi ne olsun: ")
        tam_model_ismi = model_ismi+".pkl"
        joblib.dump(model, tam_model_ismi)
        print(f"Model başarıyla eğitildi ve {tam_model_ismi} olarak kaydedildi.")
    
    return model

def score_password_strength(password, model):
    features = np.array(extract_features(password)).reshape(1, -1)
    strength = model.predict(features)
    
    if strength[0] == 1:
        score = np.random.randint(500, 1001)
        strength_label = "Güçlü"
    else:
        score = np.random.randint(0, 500)
        strength_label = "Zayıf"
    
    return strength_label, score

if __name__ == "__main__":
    print('''Bu model içerisine eklediğiniz şifreleri zayıf olarak kabul eder ve girdiğiniz şifreleri önceki zayıf şifrelerle kıyaslayarak şifre gücünü söyler.''')
    model_path = input("Mevcut bir model dosyası adını ve uzantısını giriniz (yoksa boş bırakın): ")
    
    if model_path == "":
        model_path = None
        wordlist_dosya = input("Modelde kullanılacak wordlist dosyasını giriniz: ")
        model = main(wordlist_dosya, model_path)
        password = input("Bir şifre girin: ")
        strength_label, score = score_password_strength(password, model)
        print(f"Şifrenizin gücü: {strength_label} (Skor: {score}/1000)")
    else:
        wordlist_dosya = ""
        model = main(wordlist_dosya, model_path)
        password = input("Bir şifre girin: ")
        strength_label, score = score_password_strength(password, model)
        print(f"Şifrenizin gücü: {strength_label} (Skor: {score}/1000)")
