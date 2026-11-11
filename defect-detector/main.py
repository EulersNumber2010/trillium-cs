import wave
from vocab import Vocabulary

def generate_silence(basefile, duration=1):
    num_frames = int(duration * basefile.getframerate())
    bytes_per_frame = basefile.getnchannels() * basefile.getsampwidth()
    return b'\x00' * (num_frames * bytes_per_frame)

def generate_audio(script_file, output_file):
    with wave.open(output_file, 'wb') as output, open(script_file, "r") as script:

        initsample = "defect-detector/Vocabulary/Standard Voice/Railroads/bnsf_detector.wav"
        with wave.open(initsample) as paramfile:
            params = paramfile.getparams()
            output.setparams(params)

        for line in script:
            for word in line.split():
                if word == "pause":
                    output.writeframes(generate_silence(output))
                else:
                    with wave.open(Vocabulary[word], 'rb') as voiceline:
                        data = voiceline.readframes(voiceline.getnframes())
                        output.writeframes(data)

if __name__ == "__main__":
    output_file = "ddout.wav"
    script_file = "defect-detector/script.txt"
    generate_audio(script_file, output_file)