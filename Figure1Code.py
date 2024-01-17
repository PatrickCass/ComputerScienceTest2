import matplotlib.pyplot as plt
import numpy as np

def main():
    c=400
    m=300
    k=2000
    x = np.arange(0, 8, 0.05)
    xstep = np.arange(-3*np.pi, 4*np.pi, np.pi)
    y1 = np.exp(-(c/(2*m))*x)*np.cos(np.sqrt((k/m)-(c/(2*m))**2)*x)
    y2 = np.exp(-(c/(2*m))*x)
    y3 = -np.exp(-(c/(2*m))*x)
    plt.plot(x, y1, label = "$e^{-\\frac{c}{2m}t}cos \\left(\\sqrt{\\frac{k}{m}-\\left(\\frac{c}{2m}\\right)^2}t\\right)$")
    plt.plot(x, y2, linestyle = 'dashed', label = "$e^{-\\frac{c}{2m}t}$")
    plt.plot(x, y3, linestyle = 'dashed', label = "$-e^{-\\frac{c}{2m}t}$")
    plt.ylabel('X')
    plt.xlabel('Time')
    plt.style.use('ggplot')
    plt.axhline(color = 'black')
    plt.margins(0)
    plt.legend()
    plt.show()

main()