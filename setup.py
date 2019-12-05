from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["tensorflow", "pygame", "cv2"]

setup(
    name="EmotionPlayer",
    version="0.0.1",
    description="A Music Player that recognizes face emotions and play situational Songs",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=["Programming Language :: Python :: 3.7"],
)

# run this code to execute
# python train.py --output_graph=trained_graph.pb --output_labels=trained_labels.txt --architecture=MobileNet_1.0_224 --image_dir=datasets/Images