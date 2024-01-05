import numpy as np
import streamlit as st
from st_audiorec import st_audiorec
from backend import Recognizer
from audiorecorder import audiorecorder

from io import BytesIO
import soundfile as sf
from pydub import effects


def main():
    st.title("Audio Recorder with Streamlit")
    
    st.session_state['recognizer'] = Recognizer()
    
    audio = audiorecorder("Click to record", "Click to stop recording")
    if len(audio) > 0:
        st.audio(audio.export().read())  
        audio_array = np.array(audio.get_array_of_samples(), dtype='float32')
    # wav_audio_data = st_audiorec()
    # if wav_audio_data is not None:
    #     audio = BytesIO(wav_audio_data)
    #     audio_array, _ = sf.read(audio, always_2d=False)
        if st.button("Send to Server"):
            st.info("Sending audio to the server...")
            
            if 'recognizer' in st.session_state:
                recognizer = st.session_state['recognizer']
                
                result = recognizer.run(audio_array.tobytes())
                
                st.info("The emotion of this audio is : {}".format(result.upper()))
    #     wav_audio_data = None



if __name__ == "__main__":
    main()
