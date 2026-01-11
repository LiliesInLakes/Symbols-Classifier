import onnxruntime as ort
import cv2 as cv
import numpy as np
import tensorflow as tf
from skimage.transform import resize
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
sess = ort.InferenceSession("/Users/avni/desktop/mobilenet/model.onnx")
input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[0].name
camera= cv.VideoCapture(0)
label_name= ["robocon logo", "oracle bone", "random"]
while True:
    isTrue, frame=camera.read()
    sample_image= cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    sample_image= cv.cvtColor(sample_image, cv.COLOR_GRAY2BGR)
    #img = tf.keras.utils.load_img(frame, target_size=(224, 224))
    img= preprocess_input(sample_image)
    img_arr= np.empty((1, 224, 224, 3))
    img_arr[0]= resize(img, output_shape=(224, 224))
    
    pred = sess.run([label_name], {input_name: X.astype(np.float32)})[0]
    
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
camera.release()
cv.destroyAllWindows()

