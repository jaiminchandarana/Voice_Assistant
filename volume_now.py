from comtypes import CLSCTX_ALL
from ctypes import (cast,POINTER)
from pycaw.pycaw import (AudioUtilities,IAudioEndpointVolume)
from audio import speak

def volume_now():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    current_volume_percent = current_volume * 100
    current_volume_percent = round(current_volume_percent)
    speak(f"Current system volume is {current_volume_percent} sir.")