import os

from scipy.io import wavfile

root = "output_dir"  # path to the directory containing the wav files
for file in os.listdir(root):
    if ".wav" not in file:
        continue
    input_filename = os.path.join(root, file)
    sample_rate, samples = input_data = wavfile.read(filename=input_filename, mmap=True)
    if len(samples) / sample_rate < 4:
        os.remove(input_filename)
