import ctypes
import subprocess


user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

print(screensize)

subprocess.call(['xrandr', '-s', '%dx%d' % resolution])

