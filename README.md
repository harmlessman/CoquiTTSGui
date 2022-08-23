# CoquiTTSGui
These source files are gui for users who use the coqui-TTS vits model.

![image](https://user-images.githubusercontent.com/87223285/186101795-75a3194f-5e2e-46a4-b61d-e64bdc50dfea.png)

## This Project
* It is designed to make it easy to use the model obtained by performing voice synthesis with Vits.
* Model files (.pth), speakers (.pth), language_ids (.json) are required.
* Just copy the `UI.py` file and the `design.ui` file to the location where `setup.py` is located.
* When you run the UI.py file, the gui runs.

## Prerequisites
* pyqt5
```pip install pyqt5```

# How To Use
![image](https://user-images.githubusercontent.com/87223285/186101795-75a3194f-5e2e-46a4-b61d-e64bdc50dfea.png)
1. Press the path button to select the model file.
2. Select speaker and language from the box at the top right.
3. Type text in the text box for voice synthesis.
4. If necessary, write the name of the wav file to be printed in the output file name at the bottom left. The default value is output.wav.
5. If necessary, check the running voice box at the top left. If checked, play the voice as soon as the synthesis is complete.
6. Press the systhesis button



