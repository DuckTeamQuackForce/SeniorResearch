# -*- coding: utf-8 -*-
import Augmentor
pokemon = ["\\Mudkip", "\\Eevee", "\\Pikachu"]

for pok in pokemon:
    p = Augmentor.Pipeline(
            "Insert_Folder_Path_For_Test_set" + pok
            )
    ######################### Rotate  ######################################
    p.rotate(probability=1.0, max_left_rotation=5, max_right_rotation=10)
    p.sample(50)
    #########################  Zoom   ######################################
    p.zoom(probability=0.3, min_factor=0.7, max_factor=.9)
    p.sample(50)
    #########################  Skew   ######################################
    p.skew(probability=.3, magnitude=1)
    p.sample(50)
    #########################  Shear  ######################################
    p.shear(probability=.3, max_shear_left=25, max_shear_right=25)
    p.sample(50)
    #########################  Flip   ######################################
    p.flip_random(probability=.3)
    p.sample(50)




