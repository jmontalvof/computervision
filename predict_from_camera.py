
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

model = load_model('modelo.h5')
labels = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

def predict_character(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (28, 28))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=[0, -1])
    prediction = model.predict(img)
    return labels[np.argmax(prediction)]

cam = cv2.VideoCapture(0)
print("Presiona 's' para escanear o 'q' para salir")

while True:
    ret, frame = cam.read()
    cv2.imshow("Detector de Caracteres", frame)
    key = cv2.waitKey(1)
    if key % 256 == ord('s'):
        roi = frame[100:200, 100:200]  # zona de interés para caracteres
        char = predict_character(roi)
        print(f"Caracter detectado: {char}")
    elif key % 256 == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
