import argparse
import subprocess
import os
import re
import shutil

def run_command(command):
    """Run a command in the shell and return its output."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        raise Exception(f"Error executing command: {command}\n{stderr.decode('utf-8')}")
    return stdout.decode('utf-8')

def extract_raw_lyrics(srt_file_path, output_file_path):
    """Extract raw text from the SRT file and save to output file."""
    with open(srt_file_path, 'r') as file:
        lines = file.readlines()

    # Extract only the text lines (ignoring timestamps and empty lines)
    text_lines = [re.sub(r'\d', '', line).strip() for line in lines if not re.match(r'^\d+|^\s*$', line)]

    with open(output_file_path, 'w') as file:
        file.write("\n".join(text_lines))

def main():
    parser = argparse.ArgumentParser(description="Process an audio file with spleeter and extract lyrics.")
    parser.add_argument("--name", required=True, help="Name of the audio file (e.g., song.mp3)")
    parser.add_argument("--language", default="auto", help="Language for the subtitles (default: auto). Supported languages: auto,af,am,ar,as,az,ba,be,bg,bn,bo,br,bs,ca,cs,cy,da,de,el,en,es,et,eu,fa,fi,fo,fr,gl,gu,ha,haw,he,hi,hr,ht,hu,hy,id,is,it,ja,jw,ka,kk,km,kn,ko,la,lb,ln,lo,lt,lv,mg,mi,mk,ml,mn,mr,ms,mt,my,ne,nl,nn,no,oc,pa,pl,ps,pt,ro,ru,sa,sd,si,sk,sl,sn,so,sq,sr,su,sv,sw,ta,te,tg,th,tk,tl,tr,tt,uk,ur,uz,vi,yi,yo,zh")
    args = parser.parse_args()

    audio_file = args.name
    language = args.language
    audio_file_path = os.path.join("input", audio_file)
    song_name = os.path.splitext(audio_file)[0]
    
    # Run spleeter
    spleeter_command = f"spleeter separate -o audio_output -p spleeter:5stems-16kHz {audio_file_path}"
    run_command(spleeter_command)

    # Run auto_subtitle with the specified language
    vocals_path = os.path.join("audio_output", song_name, "vocals.wav")
    subtitle_command = f"auto_subtitle {vocals_path} --model large --srt_only TRUE --language {language}"
    run_command(subtitle_command)
    
    # Move and rename the subtitles file
    original_srt_path = "vocals.srt"
    srt_file_path = os.path.join("audio_output", song_name, "lyrics_with_timestamp.txt")
    shutil.move(original_srt_path, srt_file_path)
    
    # Process the SRT file to extract raw lyrics
    raw_lyrics_path = os.path.join("audio_output", song_name, "lyrics_raw.txt")
    extract_raw_lyrics(srt_file_path, raw_lyrics_path)

    print("Processing complete. Raw lyrics saved to:", raw_lyrics_path)

if __name__ == "__main__":
    main()
