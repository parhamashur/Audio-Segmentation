import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

#cutting into the small files
sound_file = AudioSegment.from_wav("filename.wav")
audio_chunks = split_on_silence(sound_file,
    # must be silent for at least a 1500 milliseconds (1.5s)
    min_silence_len=1500,

    # consider it silent if quieter than -40 dBFS
    silence_thresh=-40
    
    # (in ms) amount of silence to leave at the beginning and
    # end of the chunks. Keeps the sound from sounding like it is abruptly cut off.
    keep_silence=150
)

for i, chunk in enumerate(audio_chunks):

    out_file = ".//foldername//chunk{0}.wav".format(i)
    print "exporting", out_file
    chunk.export(out_file, format="wav")
