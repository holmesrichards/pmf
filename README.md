This is a work in progress; better README to come soon. Meanwhile:

**Untested hardware and software — Do not assume anything works!**

This is a multimode VCF based on a [design](https://electricdruid.net/multimode-filters-part-2-pole-mixing-filters) by Electric Druid. It uses pole mixing to achieve multiple filter behaviors.

## Design notes

### Changes from ED design

* Added 51k resistor missing from original schematics (see comment section for ED post)
* 82k resistors (RF) changed to 100k; 91k resistors (RC) to 82k + 20k trimmers.
* 1.1k resistor on VEE changed to 1k + 500R trimmer.
* Added variable bias voltage to VRES pin.
* Added AC coupling capacitor on input signal to resonance compensation mixer.
* Added second inverting stage on input to preserve phase
* Changed ordering of 1st to 6th mixes.
* In 4P HP mix, changed 4.99k resistor to sum of 2k and 3k which are much easier and cheaper to obtain.
* Changed BP resistors for unity gain at peak.
* Changed 7th mix to {1, 2, 2, 0, 0} notch.
* Original had incorrect resistances for 8th mix; fixed.
* 7th and 8th mix have enough resistor footprints to implement any desired mix.
* Multiplexer replaced with rotary switch.
* Added header for expansion.

### Discussion

As discussed [here](Docs/tolerances.md), it is important that filter stages have unity DC gain and mixer ratios be correct at a level of about 1% or better, preferably more like 0.1%.

The 82k feedback resistors used in the ED design are a puzzle: Per the CEM3320 datasheet, they result in a gain of around 0.82. In the datasheet circuit these resistors are 100k giving gain 0.999. On the breadboard I found some gain variation, so I replaced the 91k resistors (RI, RC) with 82k + 20k trimmers.

The datasheet also suggests using a trimmer on the VEE pin, and adding a variable bias on the VRES pin, to null out frequency and resonance CV feedthroughs.

Since a DC bias on VRES affects resonance CV feedthrough, the ED design's resonance compensation mixer can lead to problems if there is a DC offset on the input signal. I have added a capacitor to AC couple that signal.

ED's mixers have been re-ordered, the resistors in the BP mixers have been reduced to get unity gain at the peaks, and the seventh filter (a rather weird combination of things giving rise to a sort of band pass plus notch response) has been replaced with a second notch filter.

### Choose your own

To accommodate other builders with other preferences (or future me with other preferences), in the last two filters enough resistor (or jumper) footprints have been provided to build almost any mixer allowing whatever filter responses you want. Each of the LP1, LP2, LP3, and LP4 signals has two footprints in series. For example, to re-create ED's seventh filter, [0, 1, 3, 6, 4]: Omit the R<sub>IN</sub> resistor, use 30k and a wire jumper for the two R<sub>LP1</sub> resistors, 10k+jumper for R<sub>LP2</sub>, 2k+3K for R<sub>LP3</sub>, and 7.5k+jumper for R<sub>LP4</sub>. To build the filters shown in the schematic, follow the silkscreen: Use wire jumpers for the jumper footprints and leave the DNF footprints empty.

### Expansion

There is an expansion header on the PCB. This could be used to mount a daughterboard giving more mixes. Or it could be used for a cable connection to an expansion module, which could e.g. provide user-changeable mixes (5 rotary switches?) or a microcontroller-based variable mixer, potentially even with CV input to switch mixes. This repo includes a design for a daughterboard providing four additional builder-defined mixes. As with filters 7 and 8 on the main module, there are two footprints for each of the LP1, LP2, LP3, and LP4 signals and you can populate both with resistors, use one resistor and one jumper, or omit both to get the mixes you desire.

### Filters

The filters are as follows. Numbers indicate coefficients for input, -LP1, LP2, -LP3, and LP4 mixing.

* 0, 0, 1, 0, 0 — 2 pole low pass
* 0, 0, 0, 0, 1 — 4 pole low pass
* 1, 2, 1, 0, 0 — 2 pole high pass
* 1, 4, 6, 4, 1 — 4 pole high pass
* 0, 2, 2, 0, 0 — 2 pole band pass
* 0, 0, 4, 8, 4 — 4 pole band pass
* 1, 2, 2, 0, 0 — Notch A
* 1, 2, 2, 2, 2 — Notch B

Here are Bode plots for these filters:

![Low pass](Images/Figure_1.png)
![High pass](Images/Figure_2.png)
![Band pass](Images/Figure_3.png)
![Notch](Images/Figure_4.png)

### Cancellation and tolerances

See discussion [here](Docs/tolerances.md).

## Software

The plots above were produced with a Python script included in this repo's Software folder. For a usage example see plots.sh in that folder. Libraries matplotlib, numpy, sys, and re are required. 

For the formulas for pole mixing upon which these plots are based, see [https://expeditionelectronics.com/Diy/Polemixing/math](https://expeditionelectronics.com/Diy/Polemixing/math). I believe there are some errors: the formulas for the imaginary parts of the numerator and denominator should have the opposite sign.

## Current draw
 mA +12 V,  mA -12 V


## Photos

![]()

![]()

## Documentation

* [Schematic](Docs/pmf.pdf)
* PCB layout: [front](Docs/pmf_layout_front.pdf), [back](Docs/pmf_layout_back.pdf)
* [BOM](Docs/pmf_bom.md)
* [Daughterboard schematic](Docs/pmf_daughter.pdf)
* Daughterboard PCB layout: [front](Docs/pmf_daughter_layout_front.pdf), [back](Docs/pmf_daughter_layout_back.pdf)
* [Daughterboard BOM](Docs/pmf_daughter_bom.md)
* [Build notes](Docs/build.md)

## GitHub repository

* [https://github.com/holmesrichards/](https://github.com/holmesrichards/pmf)

## Submodules

This repo uses submodules aoKicad and Kosmo_panel, which provide needed libaries for KiCad. To clone:

```
git clone git@github.com:holmesrichards/pmf.git
git submodule init
git submodule update
```


Alternatively do

```
git clone --recurse-submodules git@github.com:holmesrichards/pmf.git
```

Or if you download the repository as a zip file, you must also click on the "aoKicad" and "Kosmo\_panel" links on the GitHub page (they'll have "@ something" after them) and download them as separate zip files which you can unzip into this repo's aoKicad and Kosmo\_panel directories.

If desired, copy the files from aoKicad and Kosmo\_panel to wherever you prefer (your KiCad user library directory, for instance, if you have one). Then in KiCad, go into Edit Symbols and add symbol libraries

```
aoKicad/ao_symbols
Kosmo_panel/Kosmo
```
and go into Edit Footprints and add footprint libraries
```
aoKicad/ao_tht
Kosmo_panel/Kosmo_panel.
```
