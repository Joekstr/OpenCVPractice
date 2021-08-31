import numpy as np
import cv2

rectangle = np.zeros((300,300),dtype="uint8")
cv2.rectangle(rectangle,(25,25),(275,275),255,-1)
cv2.imshow("Square :)",rectangle)

circle = np.zeros((300,300),dtype="uint8")
cv2.circle(circle,(150,150),150,255,-1)
cv2.imshow("Circle :)",circle)

#pixels they have in common
And = cv2.bitwise_and(rectangle,circle)
cv2.imshow("¿por qué no los dos?", And)

#all the pixels they have combined
Or = cv2.bitwise_or(rectangle,circle)
cv2.imshow("OR3O", Or)

#pixels they do not have in common
Xor = cv2.bitwise_xor(rectangle,circle)
cv2.imshow("shadow dee dee", Xor)

#every pixel it doesn't have
Not = cv2.bitwise_not(circle)
cv2.imshow("PSYCHE!", Not)

cv2.waitKey(0)
