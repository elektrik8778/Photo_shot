import numpy as np
import cv2
import time
import datetime
import speech_recognition


def shot():

    # Включаем первую камеру
    cap = cv2.VideoCapture(0)
    # "Прогреваем" камеру, чтобы снимок не был тёмным
    for i in range(10):
        cap.read()
    # Делаем снимок
    ret, frame = cap.read()
    # Записываем в файл
    cv2.imwrite('cam.png', frame)
    # Отключаем камеру

    cv2.imshow('frame_photo', frame)
    cap.release()
    time.sleep(3)

    cv2.destroyWindow('frame_photo')





if __name__ == "__main__":

    shot()




