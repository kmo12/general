import ctypes
import win32api

# Узнаём текущее разрешение монитора
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Меняем разрешение
if screensize[0] == 1920:
    mode = win32api.EnumDisplaySettings()
    mode.PelsWidth = 1600
    mode.PelsHeight = 900
    mode.BitsPerPel = 32

    win32api.ChangeDisplaySettings(mode, 0)

elif screensize[0] == 1600:
    mode = win32api.EnumDisplaySettings()
    mode.PelsWidth = 1920
    mode.PelsHeight = 1080
    mode.BitsPerPel = 32

    win32api.ChangeDisplaySettings(mode, 0)

else:
    print("Изначальное разрешение экрана не установлено на 1920х1080 или на 1600х900!")
    input("")
