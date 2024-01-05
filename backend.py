import grpc

from emotion_types.emotion_speech_service_pb2 import AudioRequest, EmotionResponse
from emotion_types.emotion_speech_service_pb2_grpc import EmotionSpeechServiceStub


class Recognizer:
    def __init__(self):
        
        self.channel = grpc.insecure_channel('[::]:5002')
        self.stub = EmotionSpeechServiceStub(self.channel)
        
    def run(self, audio):
        audio_request = AudioRequest(audio=audio)
        
        result = self.stub.RecognizeEmotion(audio_request)
        
        return result.emotion