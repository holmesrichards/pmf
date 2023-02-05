# Analog Output KiCad Libraries

KiCad symbol and footprint libraries I use all the time:

## ao_symbols.kicad_sym

Symbols include (among others):

* **+12V_1, +5V_1, -12V_1** - Alternate power symbols for second board
* **2_pin_Molex_connector, 2_pin_Molex_header, 3_pin_Molex_connector, 3_pin_Molex_header** - Connectors identified as Molex
* **AS3340** - Alfa VCO chip
* **Board** - Board marker for KiKit utility
* **Graphic** - Graphics for PCB
* **LED_green, LED_red** - LEDs labeled for color
* **OLED_128X64** - OLED display
* **R_POT** Potentiometer symbol modified to include arrow and "CW" (clockwise) indicator (see note below)
* **SW_Push_black, SW_Push_red** - Push buttons labeled for color
* **Synth_power_2x5** - Euro/Kosmo power connector with power output pins
* **Synth_power_2x5_passive** - Euro/Kosmo power connector with all passive pins
* **Vactrol** - Resistive optocoupler for synth circuits

In addition to these there are numerous symbols that more or less replicate standard ones, but with my preferred footprints (from ao_tht) and added fields including Vendor and SKU.

Note regarding R_POT: This shows an arrow pointing in the pin 1 to pin 3 direction, labeled CW. I believe all the horizontal board mount pots in the KiCad Potentiometer_THT footprints library have pin 1 CCW and pin 3 CW. However, inexplicably, most of the vertical pots in the same library have pin 1 CW and pin 3 CCW. There are only a few exceptions including Potentiometer_Alpha_RD901F-40-00D_Single_Vertical, a version of which is in ao_tht.pretty. That library also has Potentiometer_Alpha_16mm_Single_Vertical, which also has pin 1 CCW. These, and slight variants, are the only pot footprints I use. Using others with the R_POT symbol from ao_symbols could lead to mistakes and confusion. 

This is a KiCad 6 version symbol library. If you need a KiCad 5 library you must use release 1.0.

## ao_tht.pretty

Footprints include many common THT packages with revised silkscreen (both reference and value in most cases). Also:

* Board_Marker for KiKit utility
* CC0, OSHW, and Analog Output logos
* DIN5 board mount
* DPDT and SPDT toggle switches
* 17x17 mm heat sink (for Tayda heat sink)
* 1/4" audio jacks, including two variants of the commonly used vertical one (with round or oval holes) and a horizontal one matching ones sold by Tayda
* Euro/Kosmo 10-pin shrouded power header, with ±12 V and Red Stripe on silkscreen
* Alpha type rotary switch
* Hand soldering SOT-23 (yes, I know the library says THT)
* Some terminal blocks I use

The footprints expect their 3D models to be found under `${KICAD_AOKICAD}/ao_tht_3d/`. `KICAD_AOKICAD` is not a standard KiCad environment variable; you can define it at **Preferences >> Configure paths...** to be the path to the aoKicad directory.

Many of these symbols and footprints are based on versions from the KiCad distribution. Some are based on ones collected from other sources — I haven't kept good track of where they came from. If any are covered by licenses not compatible with CC0 please let me know.
