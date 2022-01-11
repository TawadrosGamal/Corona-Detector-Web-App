import eel
import numpy as np
#from keras.models import load_model
#model = load_model("bestmodel.h5")
from keras.preprocessing import image


def get_img_array(img_path):
    """
    Input : Takes in image path as input
    Output : Gives out Pre-Processed image
    """
    path = img_path
    img = image.load_img (path, target_size=(224, 224, 3))
    img = image.img_to_array (img) / 255
    img = np.expand_dims (img, axis=0)

    return img


# to display the image
def close_callback(route, websockets):
    if not websockets:
        print('Bye!')
        exit()

eel.init('web')


eel.start('index.html', mode='chrome',
                        host='localhost',
                        port=27000,
                        block=True,
                        size=(700, 480),
                        position=(0,0),
                        disable_cache=True,
                        close_callback=close_callback,
                        )

def print_return(n):
    print('Return from Javascript: ', n)
eel.checkImage()(print_return)  # This immediately returns the value
#print('Got this from Javascript:', n)
class_type = {0:'Covid',  1 : 'Normal'}
path
img = get_img_array(path)

res = class_type[np.argmax(model.predict(img))]
print(f"The given X-Ray image is of type = {res}")
print()
print(f"The chances of image being Covid is : {model.predict(img)[0][0]*100} percent")
print()
print(f"The chances of image being Normal is : {model.predict(img)[0][1]*100} percent")