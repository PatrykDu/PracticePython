import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print('Width: {}, Height: {}'.format(screensize[0], screensize[1]))
