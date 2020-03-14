#21/11/2014
'''Recoded and simplified AudioRecorder from the previous
version.
YouTube example-Author-Leon-NetPwn '''
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch
from jnius import autoclass
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.properties import StringProperty, NumericProperty


class MyRecording:
    def __init__(self):
        '''Recorder object To access Android Hardware'''
        self.MediaRecorder = autoclass('android.media.MediaRecorder')
        self.AudioSource = autoclass('android.media.MediaRecorder$AudioSource')
        self.OutputFormat = autoclass('android.media.MediaRecorder$OutputFormat')
        self.AudioEncoder = autoclass('android.media.MediaRecorder$AudioEncoder')
 
        # create out recorder
        self.mRecorder = self.MediaRecorder()
        self.mRecorder.setAudioSource(self.AudioSource.MIC)
        self.mRecorder.setOutputFormat(self.OutputFormat.THREE_GPP)
        self.mRecorder.setOutputFile('/sdcard/MYAUDIO.3gp')
        self.mRecorder.setAudioEncoder(self.AudioEncoder.AMR_NB)
        self.mRecorder.prepare()
 
 
class RecordingScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(RecordingScreen, self).__init__(**kwargs)
        self.start_button = self.ids['start_button']
        
    a = NumericProperty(10)  # seconds

   
    def startRecording_clock(self):
        
        self.mins = 0 #Reset the minutes
        self.zero = 1 # Reset if the function gets called more than once
        self.duration = int(10) #Take the input from the user and convert to a number
        self.start_button.disabled = True # Prevents the user from clicking start again which may crash the program
        Clock.schedule_once(self.startRecording) ## NEW start the recording
        
        Animation.cancel_all(self)  # stop any current animations
        self.anim = Animation(a=0, duration=self.a)
        def finish_callback(animation, incr_crude_clock):
          self.stopRecording()
        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self)
        def on_a(self, instance, value):
          self.text = str(round(value, 1))
   
    def startRecording(self, dt): #NEW start the recorder
        self.r = MyRecording()
        self.r.mRecorder.start()
        
        
    def stopRecording(self):
        self.r.mRecorder.stop() #NEW RECORDER VID 6
        self.r.mRecorder.release() #NEW RECORDER VID 6
       
        Clock.unschedule(self.startRecording) #NEW stop the recording of audio VID 6

class MyrecorderApp(App):
    def build(self):
        return RecordingScreen()
 
if __name__ == '__main__':
   
   MyrecorderApp().run()
   
   