from dataclasses import dataclass
import os
from text_to_speech.constant import *
CURRENT_DIR = os.getcwd()

@dataclass
class TTSConfig:
    app_name = APPLICATION_NAME
    artifact_dir:str = os.path.join(CURRENT_DIR, app_name, ARTIFACT_DIR_KEY)
    audio_dir:str = os.path.join(artifact_dir,AUDIO_DIR)
    text_dir:str = os.path.join(artifact_dir,TEXT_DIR)