
# EMOTION BASED MUSIC PLAYER

A Python based Project which detects our face emotion using webcam or android cam and detects emotion and plays a random song for a particular emotion using pygame inbuilt music player.

### Requirement:
- Python 2 or Python 3 is required
- Used CV2 (Open CV) and Tensor Flow as important dependencies
- Other Imports are specified in Requirements.txt
- Needed `trained_graph.pb` so that it can be pre-learned or else it need to be trained with help of tensorflow with image as the datasets.


### Pre-Trained Model:
 - Trained Model will be working assuming that `trained_graph.pb` and `trained_labels.txt` is available.
 - Music Handler will use this files and help in detecting the emotion and playing the song

### Training a model:
 - training the model requires image datasets for each type of emotions (atleast 15 to 20 images in each helps in accuracy)
 - The actual colored images need to converted into gray-scale images thus `Face_crop.py` helps in cropping the face and converting it to gray-scale.
  - Using the above gray-scale images `train.py` generates `trained_graph.pb` and `trained_labels.txt`.

Music Handlers:
- The music handlers folders helps in startign the camera and detecting the faces and comparing with the previous generated `trained_graph.pb` and based on that the switch case is created to play the actual song of the emotion.
- Pygame plays the role in playing the song actually got from the switch case.

