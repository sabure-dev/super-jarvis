import speech_recognition as sr
import pyttsx3
import time

def round_price(price: float, cents_mod: int = 5) -> float:
    price_in_cents = price * 100
    rounded_price = (price_in_cents - price_in_cents % cents_mod) / 100
    return rounded_price

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen_for_price():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите цену...")
        speak("Говорите цену")
        audio = recognizer.listen(source, timeout=8, phrase_time_limit=8)
    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        print(f"Распознано: {text}")
        return float(text.replace(",", "."))
    except sr.UnknownValueError:
        print("Не удалось распознать речь. Повторите еще раз.")
        speak("Не удалось распознать.")
        return None
    except ValueError:
        print("Распознано, но не удалось преобразовать в число. Повторите еще раз.")
        speak("Не удалось преобразовать.")
        return None

print("Программа для установки цен в SuperMarket Together")
speak("Программа для установки цен запущена")

while True:
    try:
        price = None
        while price is None:
            price = listen_for_price()
            time.sleep(0.5)

        new_price = round_price(price * 2)
        print(f"Новая цена: {new_price}")
        speak(f"Новая цена: {new_price}")

    except KeyboardInterrupt:
        print("\nВыходим...")
        speak("Выход из программы")
        break