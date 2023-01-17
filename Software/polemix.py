#!/usr/bin/python3

# display pole mixing Bode plots

# polemix.py arg [arg...]

# where arg is
#     '[list] label'  or   '[list]' (label defaults to 'list')
# list being coefficients of input, -lp1, lp2, -lp3, lp4...
#
# or
#
#     a or b or p
# indicates break, show the preceding plots in one figure and start
# a new figure with the following plot. If a show only amplitude plot,
# if p show only phase plot, if b show both plots. Default behavior is
# equivalent to b as last arg.

import matplotlib.pyplot as plt
import numpy as np
from sys import argv
import re

def Hn(f, fc, n):
    # Low pass transfer function for n poles, input frequency f,
    # corner frequency fc
    w = 2*np.pi*f
    wc = 2*np.pi*fc
    return (-1.0 / (1.0 + 1j * w / wc)) ** n

def H1(f, fc):
    return Hn(f, fc, 1)

def H2(f,fc):
    return Hn(f, fc, 2)

def polemix (f, fc, a):
    # Pole mixing transfer function
    pm = 0
    for ia in range(len(a)):
        pm += a[ia] * Hn (f, fc, ia)
    return pm

def main():
#    fig = plt.figure()
#    fig, ax_lst = plt.subplots(2, 1)  # a figure with a 1x2 grid of Axes

    f = np.logspace(1,5,num=500) # frequencies from 10**1 to 10**5
    lis = [[]]
    lab = [[]]
    pm = [[]]
    pt = ['b']
    for a in argv[1:]:
        if a == 'b' or a == 'a' or a == 'p':
            # Start the next figure
            lis.append([])
            lab.append([])
            pm.append([])
            pt[-1] = a
            pt.append ('b')
            continue

        res = re.search ('^\[(.*?)\] *(\S.*)$', a)
        if res != None and len(res.groups()) == 2:
            g1 = res.group(1)
            g2 = res.group(2)
        else:
            res = re.search ('^\[(.*?)\]$', a)
            if res == None:
                continue
            elif len(res.groups()) == 1:
                g1 = res.group(1)
                g2 = str(g1)
            else:
                continue

        lis[-1].append ([float (i) for i in re.split (", *", g1)])
        lab[-1].append (g2)
        pm[-1].append (polemix (f, 1000, lis[-1][-1]))
        
    for j in range (len(pm)):
        if len(pm[j]) == 0:
            continue

        if pt[j] == 'b':
            plt.subplot(211)
        if pt[j] == 'a' or pt[j] == 'b':
            for i in range(len(pm[j])):
                plt.plot(f, 20*np.log10(abs(pm[j][i])), label=lab[j][i])
            plt.xscale('log')

            plt.xlabel('frequency (Hz)')
            plt.ylabel('amplitude (dB)')
            plt.grid(True)
            plt.legend()

        if pt[j] == 'b':
            plt.subplot(212)
        if pt[j] == 'p' or pt[j] == 'b':
            for i in range(len(pm[j])):
                plt.plot(f, 180./np.pi*np.angle(pm[j][i]), label=lab[j][i])
            plt.xscale('log')

            plt.xlabel('frequency (Hz)')
            plt.ylabel('phase shift (deg)')
            plt.grid(True)
            plt.legend()

        plt.show()

main()
