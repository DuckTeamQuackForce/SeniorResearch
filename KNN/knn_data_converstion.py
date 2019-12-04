import cv2
import os


card_dir = 'C:\\Users\\marchandsaw\\Desktop\\Full\\'


name_list = os.listdir(card_dir)
name_list_2 = name_list


j = 0
for i in name_list:
    image = cv2.imread(card_dir + name_list_2[j], cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (50, 50))
    #print(type(image))
    cv2.imwrite(os.getcwd() + '\\Grayscale\\{}'.format(i), image)
#   
    j = j + 1