import numpy as np
import matplotlib.pyplot as plt
import cv2
import base64

def data_uri_to_cv2_img(uri):
   encoded_data = uri.split(',')[1]
   nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
   img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
   return img

def image_colorizer(datauri):

    prototxt = "./model/colorization_deploy_v2.prototxt"
    model = "./model/colorization_release_v2.caffemodel"
    points = "./model/pts_in_hull.npy"
    image = data_uri_to_cv2_img(datauri)
    
    net = cv2.dnn.readNetFromCaffe(prototxt, model)
    pts = np.load(points)

    class8 = net.getLayerId("class8_ab")
    conv8 = net.getLayerId("conv8_313_rh")
    pts = pts.transpose().reshape(2, 313, 1, 1)
    net.getLayer(class8).blobs = [pts.astype("float32")]
    net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

    scaled = image.astype("float32") / 255.0
    lab = cv2.cvtColor(scaled, cv2.COLOR_RGB2LAB)
    resized = cv2.resize(lab, (224, 224))
    L = cv2.split(resized)[0]
    L -= 50
    
    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0, :, :, :].transpose((1, 2, 0))
    ab = cv2.resize(ab, (image.shape[1], image.shape[0]))

    L = cv2.split(lab)[0]
    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)

    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
    colorized = np.clip(colorized, 0, 1)
    colorized = (255 * colorized).astype("uint8")

    cv2.imshow('image',colorized)
    cv2.waitKey(0)

    _, encoded_img = cv2.imencode('.jpg', colorized)
    base64_img = base64.b64encode(encoded_img)
    return {"imgObject": base64_img}