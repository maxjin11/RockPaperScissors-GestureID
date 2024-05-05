import os
import cv2
import string
import time


# image collection/directory setup
image_directory = './images'

if not os.path.exists(image_directory):
	os.makedirs(image_directory)

class_quantity = 4
dataset_size = 50

class_labels = ['Rock', 'Paper', 'Scissors', 'Play Again']

print(class_labels)

# opencv implementation
cap = cv2.VideoCapture(0)
for j in range(class_quantity):
	if not os.path.exists(os.path.join(image_directory, class_labels[j])):
		os.makedirs(os.path.join(image_directory, class_labels[j]))

	print("Collecting images for " + class_labels[j])

	while True:
		ret, frame = cap.read()
		cv2.imshow('frame', frame)
		print("Press 'q' to start collecting images.")
		if cv2.waitKey(25) == ord('q'):
			break

	counter = 0
	while counter < dataset_size:
		ret, frame = cap.read()
		print(class_labels[j] + " " + str(counter))
		cv2.imshow('frame', frame)
		cv2.waitKey(25)
		cv2.imwrite(os.path.join(image_directory, class_labels[j], '{}.jpg'.format(counter)), frame)
		counter += 1
		time.sleep(1)

cap.release()
cv2.destroyAllWindows()

