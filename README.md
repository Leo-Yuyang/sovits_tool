# sovits-tool
This repo is a toolkit designed for training AI models using <a href="https://github.com/svc-develop-team/so-vits-svc/tree/4.0">Sovits-v4</a>. If you are training with pure human voice audio, this is all you need to train your Sovits model. If you need to extract audio from songs or music videos and remove accompaniment, you will also need the UVR(https://github.com/Anjok07/ultimatevocalremovergui) tool.

## audioseg
The script audioseg.py segments all .wav files in the input folder based on pauses and creates several segments that contain only human speech. The duration of each .wav file is controlled to be between 10 to 15 seconds, meeting the training data requirements of <a href="https://github.com/svc-develop-team/so-vits-svc/tree/4.0">Sovits-v4</a>. Also, it dumps a .json that contains the periods of time in which the slice occours, in the following format: 

{sample nº : [cut start, cut end]}. Ex.:

{"0": ["0:0:0", "0:0:3"], "1": ["0:0:3", "0:0:10"], "2": ["0:10:0", "0:0:22"], "3": ["0:0:22", "0:0:32"]}

The code was taken from <b>/andrewphillipdoss.</b> Thanks!


## transform
This script includes format conversion tools for training and inference stages of sovits-v4 that may be used to convert various data formats such as mp3, wav, m4a, and so on.

## filter_short_wav
Filter out all wav files in the specified folder that are less than 4 seconds in duration.

<h2> Python 3.11.0 </h2>

numpy (1.24.1)

scypi (1.10.0)

tqdm (4.64.1)

uuid

loguru

moviepy

pydub

<h2> Usage </h2>
To run this code, just change the path of the <b>input_dir</b> and <b>output_dir</b> inside the code.
<br/><br/>
:exclamation:Ps: Please note that in order for your audio file to be cut into samples, it should contain periods of "silence". 
<br /><br />
Depending on the level of noise in your audio, the algorithm may skip the silence windows, resulting in missed cuts. Ensure that your audio is free from unwanted noise and that the silences are clearly defined. You can adjust the parameters of <b>min_silence_length</b>, <b>silence_threshold</b>, and <b>step_duration</b> to modify the length, amplitude, and duration of the silence window in order to better match your audio
