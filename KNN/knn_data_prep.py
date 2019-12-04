# Original code found: https://www.reddit.com/r/learnprogramming/comments/4w1duu/how_can_i_loop_through_every_pixel_in_an_image/
# Code was altered for project


# from PIL import Image
import cv2 # Imports OpenCV for image manipulation
import os # Imports the os class to use for directory navigation
from PIL import Image # Imports Pillow to get average pixel count

name_list = os.listdir('Grayscale') # Navigates to a folder called grayscale (this has all the rezised grayscale images)
num = 0 # Used this to itertate through the array of image names

# Iterates through every image in the folder
for i in name_list:
     print('Starting image {0}'.format(i))
     # im = Image.open(name_list[num])
     im = Image.open('Grayscale\\{}'.format(name_list[num])) # Opens the current image   
     average = 0 # This is used hold the pixel color value
     width, height = im.size # Get's the dimiensions of the images
     
     # Iterates through each pixel
     for x in range(width):
          for y in range(height):
                    r = im.getpixel((x,y)) # Get's the pixel color data
                    average = average + r # Add all the pixel color data together
     name = name_list[num] # Get's the name of the current card
     save_name = ''

     # Looks to find if either 'Eevee' or 'Mudkip' or 'Pikachu' is in the name
     # It does this to append the name of the card to the dataset
     if 'Squirtle' in name:
          #print('Eevee Found')
          save_name = 'Squirtle'
     elif 'Charmander' in name:
          #print('Mudkip Found')
          save_name = 'Charmander'
     elif 'Bulbasaur' in name:
          #print("Pikachu found")
          save_name = 'Bulbasaur'
     with open('new_dataset_pool.txt', 'a+') as f:
          f.write('{0}, {1}\n'.format(average, save_name)) # Saves the data to a file that looks like this '12341234123, pokemon_name' where {0} is total pixel image and {1} is the image name
     num = num + 1 # Incriments num to go to the next image