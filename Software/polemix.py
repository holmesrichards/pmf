#!/usr/bin/python3

# display pole mixing Bode plots

# polemix.py arg [arg...]

# where arg is
#     '[list] label'  or   '[list]' (label defaults to 'list')
# list being coefficients of input, -lp1, lp2, -lp3, lp4...
#
# or
#
#     a[:path] or b[:path] or p[:path]
# indicates break, show the preceding plots in one figure and start
# a new figure with the following plot. If a show only amplitude plot,
# if p show only phase plot, if b show both plots. Default behavior is
# equivalent to b as last arg. If path is given write plot to that path.

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

def usage():
    print ('Usage:')
    print ('python polemix.py args...')
    print ("where each arg is '[i,l1,l2,l3,l4] label' (label defaults to '[i,l1,l2,l3,l4]')")
    print ('or -f:<freq> to specify corner frequency for following curves')
    print ('or -<plots>[:<path>] to specify page settings for following plots')
    print ('<plots> = a for amplitude, p for phase, b for both')
    print ('<path> = path for output file, no output if blank')
    print ('Default is -b')
    
def main():
#    fig = plt.figure()
#    fig, ax_lst = plt.subplots(2, 1)  # a figure with a 1x2 grid of Axes

    f = np.logspace(1,5,num=500) # frequencies from 10**1 to 10**5

    corner = 1000
    page = [[[], [], [], 'b', '']] # each entry is list of coefs, list of labels, list of polemix results, plots, path
    for a in argv[1:]:
        if a[0] == '-':
            if len(a) < 2:
                usage()
                return
            if a[1] == 'f':
                if len(a) < 4:
                    usage()
                    return
                corner = float(a[3:])
            if a[1] == 'b' or a[1] == 'a' or a[1] == 'p':
                page.append([[], [], [], 'b', ''])
                # Start the next figure
                path = ""
                if len(a) > 2:
                    if a[2] == ':':
                        path = a[3:]
                    else:
                        usage()
                        return
                page[-1][3] = a[1]
                page[-1][4] = path
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

        page[-1][0].append([float (i) for i in re.split (", *", g1)])
        page[-1][1].append(g2)
        page[-1][2].append(polemix (f, corner, page[-1][0][-1]))
        
    for j in range (len(page)):
        if len(page[j][0]) == 0:
            continue

        if page[j][3] == 'b':
            plt.subplot(211)
        if page[j][3] == 'a' or page[j][3] == 'b':
            for i in range(len(page[j][2])):
                plt.plot(f, 20*np.log10(abs(page[j][2][i])), label=page[j][1][i])
            plt.xscale('log')

            plt.xlabel('frequency (Hz)')
            plt.ylabel('amplitude (dB)')
            plt.grid(True)
            plt.legend()

        if page[j][3] == 'b':
            plt.subplot(212)
        if page[j][3] == 'p' or page[j][3] == 'b':
            for i in range(len(page[j][2])):
                plt.plot(f, 180./np.pi*np.angle(page[j][2][i]), label=page[j][1][i])
            plt.xscale('log')

            plt.xlabel('frequency (Hz)')
            plt.ylabel('phase shift (deg)')
            plt.grid(True)
            plt.legend()

        if page[j][4] != "":
            plt.savefig(page[j][4], dpi=150)
        plt.show()
main()
