import cv2
from PIL import Image

body_path = 'body.jpg'
people_path = 'people2.jpg'

image_body = cv2.imread(body_path)
image_people = cv2.imread(people_path)

person_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
smile_face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

persons_face = person_face_cascade.detectMultiScale(image_people)
smiling_face = smile_face_cascade.detectMultiScale(image_body)

cv2.imshow('People', image_people)
cv2.waitKey(2000)

for (x, y, w, h) in persons_face:
    cv2.rectangle(image_people, (x, y), (x+w, y+h), (0, 255, 0), 3)

cv2.imshow('People', image_people)
cv2.waitKey(0)

cv2.imshow('Full-Body', image_body)
cv2.waitKey(2000)

for (x, y, w, h) in smiling_face:
    cv2.rectangle(image_body, (x, y), (x+w, y+h), (0, 255, 0), 3)

cv2.imshow('Full-Body', image_body)
cv2.waitKey(0)