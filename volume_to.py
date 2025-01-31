from comtypes import CLSCTX_ALL
from ctypes import (cast,POINTER)
from pycaw.pycaw import (AudioUtilities,IAudioEndpointVolume)

def set_volume_level(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(level / 100, None)