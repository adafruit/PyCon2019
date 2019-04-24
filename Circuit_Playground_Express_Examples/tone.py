"""This example uses the speaker, the grey square next to the picture of musical notes. It
generates a sine wave sample, and then plays a tone for 1 second."""
import time
import array
import math
import audioio
import board
import digitalio

FREQUENCY = 440  # 440 Hz middle 'A'
SAMPLERATE = 8000  # 8000 samples/second, recommended!

# Generate one period of sine wav.
length = SAMPLERATE // FREQUENCY
sine_wave = array.array("H", [0] * length)
for i in range(length):
    sine_wave[i] = int(math.sin(math.pi * 2 * i / 18) * (2 ** 15) + 2 ** 15)

# Enable the speaker.
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = digitalio.Direction.OUTPUT
speaker_enable.value = True

# Set up audio to use the speaker.
audio = audioio.AudioOut(board.SPEAKER)
sine_wave_sample = audioio.RawSample(sine_wave)

# Play the sine_wave sample repeatedly for 1 second and stop.
audio.play(sine_wave_sample, loop=True)
time.sleep(1)
audio.stop()
