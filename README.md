# Vani
Voice your Actions

## Working 
Run 2 files capture.py and imgtospeech.py simultaneously
the first script saves a frame every 20 seconds 
the second script generates text describing that image using TinyLLava model and then generates/plays the audio using Coqui TTS model 

## Hardware Requirments
A simple nvidia GPU is the best way OR CPU with atleast 16BG RAM

## Run Locally

Clone the project

```bash
  git clone https://github.com/yashmerchant23/Vani.git
```

Go to the project directory

```bash
  cd Vani/Voices
```

Create virtual environment

```bash
  python -m pip install virtualenv
  python -m virtualenv tts
  source tts/Scripts/Acivate.ps1
```

install dependencies 


```bash
  # download and install python 3.9 and add it to the path in environment variables
  pip install -r requirements.txt
```

run the scripts

```bash
  # open 2 separate terminals 
  
  # first terminal
  python capture.py

  # second terminal 
  python imgtospeech.py
```

## Acknowledgements

 - [Awesome Readme Templates](https://www.youtube.com/watch?v=wOEz5xRLaRA)

