import math
from random import random
from unicodedata import name
from PIL import Image
import numpy as np
import os



picked_faces = []
face_files = os.listdir('generated_faces')
example_face = Image.open('generated_faces/' + face_files[0])
new_image = Image.new("RGBA", (2000, 2000), color=(255, 255, 255))
example_face = example_face.resize((int(new_image.size[0]/15), int(new_image.size[1]/15)))

no_of_images_in_collage = 225
image_pos = (0, 0)
rows_filled = 1
images_fit_in_a_row = math.floor(new_image.size[0]/example_face.size[0])
print(images_fit_in_a_row)
# pick 50 random faces 
i = 1
while (i <= no_of_images_in_collage+1):
    random_face = face_files[int(random()*len(face_files))]
    if((random_face in picked_faces) == False):
        face_filename = Image.open(os.path.join('generated_faces/', random_face)).convert("RGBA")
        current_row = math.ceil(i/images_fit_in_a_row)
        new_img_pos = None
        face_filename = face_filename.resize((int(new_image.size[0]/15), int(new_image.size[1]/15)))
        if(current_row > rows_filled):
            print(i)
            new_img_pos = (0, image_pos[1]+face_filename.size[1])
            rows_filled+=1
        else:
            new_img_pos = (image_pos[0] + face_filename.size[0], image_pos[1])
        # pasting image on collage canvas 
        
        new_image.paste(face_filename, image_pos, face_filename)
        new_image.save("nft_collection_collage"+'.png', "PNG")

        image_pos = new_img_pos
        picked_faces.append(random_face)
        i+=1
random_face = face_files[int(random()*len(face_files))]
random_face = Image.open(os.path.join('generated_faces/', random_face)).convert("RGBA")
random_face = random_face.resize((int(random_face.size[0]*2), int(random_face.size[1]*2)))
new_image.paste(random_face, (int((new_image.size[0]/2)-(random_face.size[0]/2)), int((new_image.size[1]/2)-(random_face.size[1]/2))), random_face)
new_image.save("nft_collection_collage"+'.png', "PNG")