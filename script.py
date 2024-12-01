import ctypes
from ctypes import wintypes
import win32gui
import win32con
import time


def is_window_maximized():
    hwnd = win32gui.GetForegroundWindow()
    if hwnd:
        placement = win32gui.GetWindowPlacement(hwnd)
        return placement[1] == win32con.SW_SHOWMAXIMIZED
    return False



# Constants
ABS_AUTOHIDE = 0x1
ABM_GETSTATE = 0x4
ABM_SETSTATE = 0xA

# Import user32 and shell32
user32 = ctypes.WinDLL('user32', use_last_error=True)
shell32 = ctypes.WinDLL('shell32', use_last_error=True)

import ctypes
from ctypes import wintypes

# Constants
ABM_SETSTATE = 0xA

# Load shell32.dll
shell32 = ctypes.WinDLL('shell32', use_last_error=True)

def set_autohide(bstate: bool):

    if bstate:
        state = 1
    else:
        state = 0
    

    """
    Sets the taskbar's state using a raw integer value.
    :param state: The raw state to set (e.g., 0 for disabled, 1 for enabled).
    """
    # Define APPBARDATA structure
    class APPBARDATA(ctypes.Structure):
        _fields_ = [
            ("cbSize", ctypes.c_uint),
            ("hWnd", wintypes.HWND),
            ("uCallbackMessage", ctypes.c_uint),
            ("uEdge", ctypes.c_uint),
            ("rc", wintypes.RECT),
            ("lParam", ctypes.c_int),
        ]

    # Initialize APPBARDATA
    abd = APPBARDATA()
    abd.cbSize = ctypes.sizeof(APPBARDATA)

    # Pass the new state
    abd.lParam = state

    # Apply the state using SHAppBarMessage
    shell32.SHAppBarMessage(ABM_SETSTATE, ctypes.byref(abd))





previous = False

while True:
    current = is_window_maximized()
    if current:
        if previous != current:
            set_autohide(True)
            previous = True
    else:
        if previous != current:
            set_autohide(False)
            previous = False


    time.sleep(0.5)
