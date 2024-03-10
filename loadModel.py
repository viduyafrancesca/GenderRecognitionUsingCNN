# Modify 'test1.jpg' and 'test2.jpg' to the images you want to predict on
import cv2
from keras.models import load_model
# from keras.models import load_weights
from keras.preprocessing import image
import matplotlib  
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt  
import numpy as np
import re
import pandas as pd
# import image_preprocess as pre
# import numpy as np
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array
from keras.models import model_from_json
import image_preprocess as pre
from keras.preprocessing.image import ImageDataGenerator
model_name = 'models/model50v2cropped7.h5'
def predict(filename):
    model = load_model(model_name)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    output = []
    try:
    # file = cv2.imread(filename)
    # file = cv2.resize(file, (32, 32))
        file = pre.process(filename)
        # cv2.imshow('a', file)
        # cv2.waitKey(0)
        test_image = image.img_to_array(file)
        test_image = np.expand_dims(test_image, axis=0)
        test_image = test_image.astype("float") /255.0
        # print(test_image)

        (female, male) = model.predict(test_image)[0]
        acc = model.predict_proba(test_image)

        label = "Female" if female > male else "Male"
        proba = female if female > male else male
        proba = "%.2f" % round(proba*100, 2) + "%"
        output.append(label)
        output.append(proba)
    except Exception as e:
        output.append('Face not found')
        output.append('Face not found')
    return output

if __name__ == '__main__':
    directory = 'Cropped1/Testing'
    model = load_model(model_name)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    test_data_generator = ImageDataGenerator(rescale=1./255)
    test_generator = test_data_generator.flow_from_directory(
        directory,
        target_size=(32, 32),
        batch_size=1,
        class_mode=None, 
        shuffle=False)
    test_generator.reset()

    filenames = test_generator.filenames
    nb_samples = len(filenames)
    print(nb_samples)
    pred=model.predict_generator(test_generator, steps = nb_samples, verbose=1)
    predicted_class_indices=np.argmax(pred, axis=1)
    labels = {'female':0, 'male':1}
    labels = dict((v,k) for k,v in labels.items())
    predictions = [labels[k] for k in predicted_class_indices]
    print(predictions)

    filenames=test_generator.filenames
    results=pd.DataFrame({"Filename":filenames,
                        "Predictions":predictions})
    results.to_csv("confusion2.csv",index=False)