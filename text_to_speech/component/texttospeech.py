from text_to_speech.exception import TTSException
from text_to_speech.logger import logger
from text_to_speech.entity.config_entity import TTSConfig
from text_to_speech.constant import TEXT_FILE_NAME, CURRENT_TIME_STAMP
import os
import sys
from gtts import gTTS
import base64


class TTSapplication():
    def __init__(self,app_config = TTSConfig())-> None:
        try:
            self.app_config = app_config
            self.artifact_dir = app_config.artifact_dir
            self.audio_dir = app_config.audio_dir
            self.text_dir = app_config.text_dir
        except Exception as e:
            raise TTSException(e,sys)
      
    def text2speech(self,text,accent):
        try:
            text_filename= TEXT_FILE_NAME
            text_filepath = os.path.join(self.text_dir,TEXT_FILE_NAME)
            with open(text_filepath,'a+') as text:
                text.write(f'\n{text}')
        
            tts = gTTS(text=text,lang='en', tid = accent,slow =False)
            
            file_name = f"converted_file_{CURRENT_TIME_STAMP}.mp3"
            audio_path = os.path.join(self.audio_dir,file_name)
            
            tts.save(audio_path)
            
            with open(audio_path,'rb') as file:
                my_string = base64.base64encode(file.read())
            return my_string
        
        except Exception as e:
            raise TTSException(e,sys)