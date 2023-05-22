import os

from moviepy.editor import *
from pydub import AudioSegment


def trans_wav_to_mp3(filepath):
    new_filepath = filepath.replace(".wav", ".mp3")
    song = AudioSegment.from_mp3(filepath)
    print(new_filepath)
    song.export(new_filepath, format="mp3")


def trans_m4a_to_mp3(filepath):
    new_filepath = filepath.replace(".m4a", ".mp3")
    song = AudioSegment.from_mp3(filepath)
    print(new_filepath)
    song.export(new_filepath, format="mp3")


def trans_mp3_to_wav(filepath):
    new_filepath = filepath.replace(".mp3", ".wav")
    song = AudioSegment.from_mp3(filepath)
    song.export(new_filepath, format="wav")


def trans_wav_to_mp3(filepath):
    new_filepath = filepath.replace(".wav", ".mp3")
    song = AudioSegment.from_mp3(filepath)
    print(new_filepath)
    song.export(new_filepath, format="mp3")


def trans_m4a_to_wav(filepath):
    new_filepath = filepath.replace(".m4a", ".wav")
    command = f"ffmpeg -i {filepath} -acodec pcm_s16le -ac 2 -ar 44100 {new_filepath}"
    os.system(command)


def trans_mp4_to_wav(filepath):
    new_filepath = filepath.replace(".mp4", ".wav")
    video = VideoFileClip(filepath)
    audio = video.audio
    audio.write_audiofile(new_filepath)


def trans_mp4_to_mp3(filepath):
    new_filepath = filepath.replace(".mp4", ".mp3")
    video = VideoFileClip(filepath)
    audio = video.audio
    audio.write_audiofile(new_filepath)
