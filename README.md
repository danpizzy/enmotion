#Enmotion

Enmotion is a Python-based tool for detecting emotions in text using Natural Language Processing (NLP). The tool utilizes the SentimentIntensityAnalyzer from the nltk library to detect the emotion in the given text. Enmotion is also bundled with an executable file that can be run on any Windows computer without requiring the installation of Python or any dependencies. The executable file was created using the auto-py-to-exe module in Python.
Installation

To use Enmotion, follow these steps:

    Clone the repository
    Install the required dependencies

Usage

To use Enmotion, you can run either the enmotion.py script or the bundled executable file enmotion.exe. The enmotion.py script launches a graphical user interface (GUI) where you can enter the text for which you want to detect the emotion. Click the "Detect Emotion" button to obtain the emotion for the given text. The enmotion.exe file can be run directly without any dependencies or Python installation.
Dependencies

Enmotion requires the following dependencies to run:

    os
    tkinter
    sys
    nltk

Make sure to install these dependencies before running the tool. You can use the following commands to install these dependencies:

sh

pip install os
pip install tkinter
pip install sys
pip install nltk

Features

Enmotion has the following features:

    Simple and easy-to-use graphical user interface (GUI) for entering text and obtaining the emotion.
    Utilizes Natural Language Processing (NLP) to accurately detect the emotion in the given text.
    Supports detection of three emotions: positive, negative, and neutral.
    Bundled executable file for running Enmotion on any Windows computer without requiring Python or any dependencies.

How it works

Enmotion works by using the SentimentIntensityAnalyzer from the nltk library to analyze the given text and determine the emotion. The analyzer returns a sentiment score for the given text, which is then used to determine the emotion. If the compound score is greater than or equal to 0.05, the emotion is considered positive. If the compound score is less than or equal to -0.05, the emotion is considered negative. Otherwise, the emotion is considered neutral.
Contributions

Contributions to Enmotion are welcome! If you find any bugs or have any suggestions for improvement, feel free to open an issue or submit a pull request.
License

Enmotion is licensed under the 
