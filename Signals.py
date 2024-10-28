import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider, IntSlider

print('Here is a lesson on Signals.')
print('Use the sliders to adjust the frequency, amplitude ,and time')

# Signal function
def signal(f,a,t):
    time = np.linspace(0,t,1000)
    pi = 3.14
    y = a*np.sin(2*pi*f*time)
    return time, y

# Plotting function
def plot_signal(f,a,t):
    time, y=signal(f,a,t)
    plt.figure(figsize=(10, 6))
    plt.plot(time, y)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.title(f"Signal(Frequency: {f} Hz, Amplitude: {a}, Time {t} s)")
    plt.grid(True)
    plt.ylim(-aval.max,aval.max)
    plt.xlim(0, t)
    plt.show()

#Interactive Plot
aval= FloatSlider(min=0.0, max=5.0, step=0.1, description='Amplitude')
fval= FloatSlider(min=0.0, max=10.0, step=0.1, description='Frequency(Hz)')
tval= FloatSlider(min=0.0, max=10.0, step=0.1, description='Time(s)')
interact(plot_signal,f=fval,a=aval,t=tval)

################################################################################

print('Now lets look at signal damping')
print('Use the sliders to adjust the damping ratio, frequency, and time')

def damped(c,f,t):
    time = np.linspace(0,t,1000)
    pi = 3.14
    y = 5*np.exp(-c*time)*np.sin(2*pi*f*time)
    return time, y

def plot_damped(c,f,t):
    time, y=damped(c,f,t)
    plt.figure(figsize=(10, 6))
    plt.plot(time, y)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.title(f"Damped Signal(Damping Ratio: {c}, Frequency: {f} Hz, Time {t} s)")
    plt.grid(True)
    plt.ylim(-5,5)
    plt.xlim(0, t)
    plt.show()

fval= FloatSlider(min=0.0, max=10.0, step=0.1, description='Frequency(Hz)')
tval= FloatSlider(min=0.0, max=1.0, step=0.1, description='Time(s)')
cval= FloatSlider(min=0.0, max=10.0, step=0.1, description='Damping Ratio')
interact(plot_damped,f=fval,t=tval,c=cval)

###################################################################################

print('Now lets look at signal amplification')
print('Use the sliders to adjust the amplification, frequency, and time')

def amplification(c,f,t):
    time = np.linspace(0,t,1000)
    pi = 3.14
    y = 5*np.exp(c*time)*np.sin(2*pi*f*time)
    return time, y

def plot_amplification(c,f,t):
    time, y=amplification(c,f,t)
    plt.figure(figsize=(10, 6))
    plt.plot(time, y)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.title(f"Damped Signal(Amplication: {c}, Frequency: {f} Hz, Time {t} s)")
    plt.grid(True)
    plt.ylim(-100,100)
    plt.xlim(0, t)
    plt.show()

fval= FloatSlider(min=0.0, max=20.0, step=0.1, description='Frequency(Hz)')
tval= FloatSlider(min=0.0, max=1.0, step=0.1, description='Duration(s)')
cval= FloatSlider(min=0.0, max=3.0, step=0.1, description='Amplification')
interact(plot_amplification,f=fval,t=tval,c=cval)