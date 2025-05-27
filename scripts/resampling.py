import os
import glob
import librosa
import soundfile as sf
from tqdm import tqdm

def main():
    input_dir = 'data/presampled'
    output_dir = 'data/resampled'
    orig_sr = 44100
    target_sr = 22050

    os.makedirs(output_dir, exist_ok=True)
    wav_files = glob.glob(os.path.join(input_dir, '*.wav'))

    for wav_path in tqdm(wav_files, desc="Resampling", unit="file"):
        y, sr = librosa.load(wav_path, sr=orig_sr, mono=False)
        if y.ndim > 1:
            y = y.mean(axis=0)  # Convert to mono by averaging channels
        y_resampled = librosa.resample(y, orig_sr=sr, target_sr=target_sr)
        out_path = os.path.join(output_dir, os.path.basename(wav_path))
        sf.write(out_path, y_resampled, target_sr)

if __name__ == "__main__":
    main()
