from datetime import datetime
APPLICATION_NAME = 'text_to_speech'
ARTIFACT_DIR_KEY = 'artifat'
AUDIO_DIR ='tts_audio'
TEXT_DIR = 'tts_text'

TEXT_FILE_NAME='userinput.txt'
fmt = "%Y-%m-%d %H%M%S"
CURRENT_TIME_STAMP = f"{datetime.now().strftime(fmt)}"