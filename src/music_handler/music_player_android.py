import cv2
import label_image
import os,random,subprocess
import  numpy as np
from urllib.request import  urlopen
import time
from playsound import playsound
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

size = 4

# We load the xml file
cascade_fn = args.get('--cascade', "../image_utils/haarcascade_frontalface_alt.xml")
classifier = cv2.CascadeClassifier(cascade_fn)
mobile_video="http://192.168.0.109:8080/shot.jpg"
now = time.time()
future = now + 15
  # Using default WebCam connected to the PC.

while True:

    img_resp = urlopen(mobile_video)
    img_arr = np.array(bytearray(img_resp.read()), dtype=np.uint8)

    cap = cv2.imdecode(img_arr, -1)
    im=cv2.flip(cap,1,0)
    mini = cv2.resize(im, (int(im.shape[1] / size), int(im.shape[0] / size)))

    # detect MultiScale / faces
    faces = classifier.detectMultiScale(mini)
    global text

    # Draw rectangles around each face
    for f in faces:
        (x, y, w, h) = [v * size for v in f]  # Scale the shapesize backup
        sub_face = im[y:y + h, x:x + w]
        FaceFileName = "output_emotion.jpg"  # Saving the current image from the webcam for testing.
        cv2.imwrite(FaceFileName, sub_face)
        text = label_image.main(FaceFileName)  # Getting the Result from the label_image file, i.e., Classification Result.
        text = text.title()  # Title Case looks Stunning.
        font = cv2.FONT_HERSHEY_TRIPLEX

        if text == "Calmness":
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0, 25, 255), 2)

        if text == "Happy":
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0, 260, 0), 2)

        if text == "Excited":
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 255), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0, 255, 255), 2)

        if text == "Sad":
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 191, 255), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0, 191, 255), 2)

    # Show the image/
    cv2.imshow('Music player with Emotion recognition', im)
    key = cv2.waitKey(30)& 0xff
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.set_volume(1.9)
    if time.time() > future:
                try:
            print(text)
            if text == "Calmness":
                randomfile = random.choice(
                    os.listdir(
                        "/Users/RaghulJayan/Qube/Repo/emotion-player/datasets/Songs/Calmness/"
                    )
                )
                print(
                    "You are very calm !!!! please cheer up:) ,I will cheer you by playing a song for you :"
                    + randomfile
                )
                file = (
                    "/Users/RaghulJayan/Qube/Repo/emotion-player/datasets/Songs/Calmness/"
                    + randomfile
                )
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
                pygame.quit()
                print("done")
                exit()

            if text == "Happy":
                randomfile = random.choice(
                    os.listdir(
                        "/Users/RaghulJayan/Qube/Repo/emotion-player/datasets/Songs/Happy/"
                    )
                )
                print(
                    "You are smiling :) ,I'm playing a special song for you: "
                    + randomfile
                )
                file = (
                    "/Users/RaghulJayan/Qube/Repo/emotion-player/datasets/Songs/Happy/"
                    + randomfile
                )
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
                pygame.quit()
                print("done")
                exit()

            if text == "Excited":
                randomfile = random.choice(
                    os.listdir(
                        "/Users/RaghulJayan/Qube/Repo/emotion-player/datasets/Songs/Fear/"
                    )
                )
                print("You have excited ,Let me make you more excited: " + randomfile)
                file = (
                    "/Users/RaghulJayan/Qube/Repo/emotion-player/datasets/Songs/Excited/"
                    + randomfile
                )
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
                pygame.quit()
                print("done")
                exit()

            if text == "Sad":
                randomfile = random.choice(
                    os.listdir(
                        "/Users/RaghulJayan/Qube/Repo/emotion-player/datasets/Songs/Sad/"
                    )
                )
                print("You are sad,dont worry:) ,I playing song for you: " + randomfile)
                file = (
                    "/Users/RaghulJayan/Qube/Repo/emotion-player/datasets/Songs/Sad/"
                    + randomfile
                )
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
                pygame.quit()
                print("done")
                exit()
            break

        except:
            print(
                "Please stay focus in Camera frame atleast 10 seconds & run again this program:)"
            )
            break

    if key == 27:  # The Esc key
        break