import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        joy_resp = emotion_detector("I am glad this happened")
        self.assertEqual(joy_resp['dominant_emotion'], 'joy')
        
        anger_resp = emotion_detector("I am really mad about this")
        self.assertEqual(anger_resp['dominant_emotion'], 'anger')

        disgust_resp = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(disgust_resp['dominant_emotion'], 'disgust')
        
        sad_resp = emotion_detector("I am so sad about this")
        self.assertEqual(sad_resp['dominant_emotion'], 'sadness')
        
        fear_resp = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(fear_resp['dominant_emotion'], 'fear')

unittest.main()
