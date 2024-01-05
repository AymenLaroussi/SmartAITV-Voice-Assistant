# SmartTV - Personal Assistant 

## Overview
This project aims to create a personalized Smart TV alternative solution using PyQt5 and exploring web content. The application includes a voice assistant feature activated by a specific wake word.

## Installation
1. Ensure you have Python installed. If not, download and install it from [Python's official website](https://www.python.org/).
2. Install the required packages:
    - PyQtWebEngine:
    ```bash
    pip install PyQtWebEngine
    ```
    - SpeechRecognition:
    ```bash
    pip install SpeechRecognition
    ```
    - setuptools:
    ```bash
    pip install setuptools
    ```
    - DeepSpeech:
    ```bash
    pip install deepspeech
    ```
    - Generate requirements.txt:
    ```bash
    pip freeze > requirements.txt
    ```
3. Install GPT4ALL: Visit [GPT4ALL](https://gpt4all.io/index.html) for offline installation. Download the GPT4ALL model and save it as a `.bin` file. Update the `.env` file with the model path.

## Features
- **Multi-tab Browsing:** Explore multiple websites simultaneously.
- **Cookie Management:** Set cookies for specific web sessions.
- **Custom User Agent:** Set a custom user agent for browsing.
- **Full-Screen Mode:** Enhance the viewing experience with fullscreen.
- **Voice Assistant:** Activated using the wake word 'Alex'.
- **Alex interaction:** 'Alex' trying to answer your questions and interact with you.

## Requirements
- Python 3.x
- PyQt5
- PyQtWebEngine
- PyAudio
- setuptools
- SpeechRecognition
- tqdm
- typing_extensions
- urllib3

## Usage
1. Clone or download this repository.
2. Run the `main.py` file to initiate the Smart TV interface.
3. Explore various functionalities and tabs within the application.
4. Customize and extend the code as needed for your Smart TV project.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
- [PyQt5](https://riverbankcomputing.com/software/pyqt/intro)
- [PyQtWebEngine](https://www.riverbankcomputing.com/software/pyqtwebengine/intro)
