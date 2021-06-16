from thinkdsp import decorate
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import TriangleSignal
from thinkdsp import read_wave

triangle = TriangleSignal(440).make_wave(duration=0.01)
plt.subplot(211)
triangle.plot()
decorate(xlabel='Time (s)')
spectrum = triangle.make_spectrum()
print(spectrum.hs[0])

plt.subplot(212)
spectrum.hs[0] = 100
triangle.plot(color='gray')
spectrum.make_wave().plot()
decorate(xlabel='Time (s)')
plt.show()