import os
import platform
import subprocess
from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
load_dotenv()
def text_to_speech_with_gtts(input_text, output_filepath):
    """
    Generate speech from text using Google Text-to-Speech and play it.
    For Windows, converts MP3 to WAV before playing.
    """
    language = "en"
    
    # Generate MP3 file
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    
    # Play the audio according to OS
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            # Windows Media.SoundPlayer only supports WAV format
            wav_filepath = output_filepath.replace(".mp3", ".wav")
            # Convert MP3 to WAV using ffmpeg
            subprocess.run(['ffmpeg', '-y', '-i', output_filepath, wav_filepath], 
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            # Play the WAV file
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['mpg123', output_filepath])  # Using mpg123 instead of aplay for MP3 support
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
    
    return output_filepath

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    """
    Generate speech from text using ElevenLabs and play it.
    For Windows, converts MP3 to WAV before playing.
    """
    # Get API key from environment
    ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")
    
    # Generate MP3 file with ElevenLabs
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Laura",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    
    # Play the audio according to OS
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            # Windows Media.SoundPlayer only supports WAV format
            wav_filepath = output_filepath.replace(".mp3", ".wav")
            # Convert MP3 to WAV using ffmpeg
            subprocess.run(['ffmpeg', '-y', '-i', output_filepath, wav_filepath], 
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            # Play the WAV file
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['mpg123', output_filepath])  # Using mpg123 instead of aplay for MP3 support
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
    
    return output_filepath

# Optional: function that directly returns audio without playing
def text_to_speech_for_gradio(input_text, output_filepath):
    """
    Generate speech from text using ElevenLabs without playing it.
    For Gradio interfaces, just return the filepath.
    """
    # Get API key from environment
    ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")
    
    # Generate MP3 file with ElevenLabs
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Laura",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    
    return output_filepath