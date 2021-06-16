from thinkdsp import decorate
from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import SquareSignal
from thinkdsp import TriangleSignal
from thinkdsp import read_wave


square = SquareSignal(1100).make_wave(duration=0.5, framerate=10000)
square.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
square.write(filename="2.3.wav")


plt.show()