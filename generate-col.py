from random import random
from unicodedata import name
from PIL import Image
import numpy as np
import os

# make a direactory to save generated faces 
if (os.path.isdir('generated_faces') == False):
    os.mkdir('generated_faces')

faces_generated = []

# faces_len = len(os.listdir('face-cut'))
hair_len = len(os.listdir('traits/hair'))
eyes_len = len(os.listdir('traits/eyes'))
mouth_len = len(os.listdir('traits/mouth'))
beard_len = len(os.listdir('traits/beard'))
nose_len = len(os.listdir('traits/nose'))

face_file = os.path.join('traits/face', 'face.png')

hairs=[]
eye_pairs = []
noses = []
mouths = []
beards = []

i = 0
while i <= hair_len:
    if ('hair-'+str(i) + '.png') in os.listdir('traits/hair'):
        hairs.append({'id': i, 'name': 'hair-'+ str(i) + '.png'})
        i += 1
    else:
        i+=1
        continue
i = 0
while i <= eyes_len:
    if ('eye-'+str(i) + '.png') in os.listdir('traits/eyes'):
        eye_pairs.append({'id': i, 'name': 'eye-'+ str(i) + '.png'})
        i += 1
    else:
        i+=1
        continue
i = 0
while i <= mouth_len:
    if ('mouth-'+str(i) + '.png') in os.listdir('traits/mouth'):
        mouths.append({'id': i, 'name': 'mouth-'+ str(i) + '.png'})
        i += 1
    else:
        i+=1
        continue

i = 0
while i <= beard_len:
    if('beard-'+str(i) + '.png') in os.listdir('traits/beard'):
        beards.append({'id': i, 'name': 'beard-'+ str(i) + '.png'})
        i += 1
    else:
        i+=1
        continue

i=0
while i <= nose_len:
    if('nose-'+str(i) + '.png') in os.listdir('traits/nose'):
        noses.append({'id': i, 'name': 'nose-'+ str(i) + '.png'})
        i += 1
    else:
        i+=1
        continue

# len(eye_pairs)*len(hairs)*len(mouths)*len(noses)
no_of_unique_possibilities = (500)
while len(faces_generated) < no_of_unique_possibilities:
    # random_eyes = np.random.randint(0, len(eyes))
  
    random_face = 1
    # we added +1 at the end of each randint function of numpy coz it chooses from low(inclusive) to open (exclusive)
    random_hair = np.random.randint(1, len(hairs)+1)
    random_mouth = np.random.randint(1, len(mouths)+1)
    random_eye = np.random.randint(1, len(eye_pairs)+1)
    random_nose = np.random.randint(1, len(noses)+1)
    random_beard = np.random.randint(1, len(beards)+1)
    print(len(faces_generated), (no_of_unique_possibilities))
    # the way to generate face as tuple is (face-index, hair-index, eye-index, mouth-index)
    index = [random_face, random_hair, random_eye,random_nose, random_mouth, random_beard]
    if(tuple(index) in  faces_generated):
        continue
    this_face = face_file
    this_hair = hairs[random_hair-1]
    this_eye = eye_pairs[random_eye-1]
    this_nose = noses[random_nose-1]
    this_mouth = mouths[random_mouth-1]
    this_beard = beards[random_beard-1]
    # pillow logic of overlaying hair on face-outline 
   
    hair_layer = Image.open(os.path.join('traits/hair/',f"{this_hair['name']}"))
    eye_layer = Image.open(os.path.join('traits/eyes/',f"{this_eye['name']}"))
    nose_layer = Image.open(os.path.join('traits/nose/',f"{this_nose['name']}"))
    mouth_layer = Image.open(os.path.join('traits/mouth/',f"{this_mouth['name']}"))
    beard_layer = Image.open(os.path.join('traits/beard/',f"{this_beard['name']}"))

    

    

    background = Image.open(face_file)

    # print(background.size)

    # # resize the image
    size = background.size
    # hair_layer = hair_layer.resize(size,Image.ANTIALIAS)
    # mouth_layer = mouth_layer.resize(size,Image.ANTIALIAS)
    

    background.paste(hair_layer, (0, 0), hair_layer)

    # saving the face 
    faces_generated_dir = os.listdir('generated_faces')
    generated_face_filename = f'generated_faces/face-{random_face}-{random_hair}-{random_eye}-{random_nose}-{random_mouth}-{random_beard}.png'
    if(generated_face_filename not in faces_generated_dir):
        open(generated_face_filename, 'wb')
        # print(generated_face_filename, 'generated just now')
    # print(len(faces_generated) , (len(eye_pairs)*len(hairs)*(len(mouths))))

    background.save(generated_face_filename,"PNG")
    background.paste(mouth_layer, (0, 0), mouth_layer)
    background.save(generated_face_filename,"PNG")
    background.paste(eye_layer, (0, 0), eye_layer)
    background.save(generated_face_filename,"PNG")
    background.paste(nose_layer, (0, 0), nose_layer)
    background.save(generated_face_filename,"PNG")
    background.paste(beard_layer, (0, 0), beard_layer)
    print(int(size[0]*1.2),int( size[1]*1.2))
    new_image = Image.new("RGBA", (int(size[0]*1.2),int( size[1]*1.2)), color=(np.random.randint(40, 266), np.random.randint(40, 266), np.random.randint(40, 266)))
    new_image.paste(background, (int((new_image.size[0]/2)-(size[0]/2)), int((new_image.size[1]/2)-size[1]/2)), background)  
    new_image.convert('RGB').save(generated_face_filename, "PNG")  
    faces_generated.append((random_face, random_hair, random_eye, random_mouth))


print('hey')




