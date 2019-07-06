# USAGE
# python recognize_faces_image.py --encodings encodings.pickle --image examples/example_01.png

# import the necessary packages
import face_recognition
import argparse
import pickle
import cv2
import imutils

# 1) construct the argument parser for encodings and image and parse the arguments


ap = argparse.ArgumentParser()

ap.add_argument("-e", "--encodings", required=True, help="input the encoding pickle file")
ap.add_argument("-i", "--images", required=True, help="enter your image to recognize")
ap.add_argument("-d", "--detection_method", type=str, default="cnn",
                help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())

# load the known faces and embeddings
print("[INFO] loading encodings...")
data = pickle.loads(open(args["encodings"], "rb").read())

# imagePaths = list(paths.list_images(args["images"]))
# print(imagePaths)

# 2) load the input image and convert it from BGR to RGB

pic = args["images"]
image = cv2.imread(pic)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
rgb = cv2.resize(rgb, (500, 500))

# detect the (x, y)-coordinates of the bounding boxes corresponding
# to each face in the input image, then compute the facial embeddings
boxes = face_recognition.face_locations(rgb, model=args["detection_method"])
encodings = face_recognition.face_encodings(rgb, boxes)

# for each face
print("[INFO] recognizing faces...")
####3) complete this watching encodings.py it will be similar

# initialize the list of names for each face detected
names = []

# 4) loop over the facial embeddings
image = rgb
for encoding in encodings:
    # attempt to match each face in the input image to our known
    # encodings
    matches = face_recognition.compare_faces(data["encodings"], encoding)
    name = "Unknown"

    # check to see if we have found a match
    if True in matches:
        # find the indexes of all matched faces then initialize a
        # dictionary to count the total number of times each face
        # was matched
        matchedIdxs = [i for (i, b) in enumerate(matches) if b]
        counts = {}

        # loop over the matched indexes and maintain a count for
        # each recognized face face
        for i in matchedIdxs:
            name = data["names"][i]
            counts[name] = counts.get(name, 0) + 1

        # determine the recognized face with the largest number of
        # votes (note: in the event of an unlikely tie Python will
        # select first entry in the dictionary)
        name = max(counts, key=counts.get)

    # update the list of names
    names.append(name)

# loop over the recognized faces

for ((top, right, bottom, left), name) in zip(boxes, names):
    # 5) draw the predicted face name on the image
    cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)  # -- complete this
    y = top - 15 if top - 15 > 15 else top + 15
    cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                0.75, (0, 255, 0), 2)

# show the output image

cv2.imshow("OUTPUT IMAGE", image)  # - complete this
cv2.waitKey(0)