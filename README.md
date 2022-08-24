# CoquiTTSGui
These source files are gui for users who use the coqui-TTS vits model.

![image](https://user-images.githubusercontent.com/87223285/186101795-75a3194f-5e2e-46a4-b61d-e64bdc50dfea.png)

## This Project
* It is designed to make it easy to use the model obtained by performing voice synthesis with Vits.
* Model file (.pth), speakers (.pth), language_ids (.json), config(.json) are required.
* Model file, speakers file, language_ids file, config file must be in the same location.
* Just copy the `UI.py` file and the `design.ui` file to the location where `setup.py` is located.
* When you run the `UI.py` file, the gui runs.

## Prerequisites
* pyqt5
* playsound==1.2.2
```
pip install pyqt5
pip install playsound==1.2.2
```

# How To Use
![guinum](https://user-images.githubusercontent.com/87223285/186298934-7556c59d-363a-4707-be3e-ff83c5f07f19.png)

1. Press the path button to select the model file.
2. Select speaker and language from the box .
3. Type text in the text box for voice synthesis.
4. If necessary, write the name of the wav file to be printed in the output file name. The default value is output.wav.
5. If necessary, check the running voice box. If checked, play the voice as soon as the synthesis is complete.
6. Press the systhesis button

# Note
* Total time is the time taken from the time the synthesis button is clicked to the time the wav file is generated.
* Audio time is the length of the generated audio.
* The output file is located in the same location as the model.
* The filename of speakers file, language_ids file, config file follows the default value. If you want to change the file name above, please modify the values of config_name, lang_id_name, and speak_id_name in the code.

