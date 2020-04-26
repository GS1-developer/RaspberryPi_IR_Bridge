# RaspberryPi_IR_Bridge
Raspberry PI based IR bridge between SONY RMT-TX100D and PIONNER A-30 (AXD7644)

## Overview
# Hardware:
Raspberry PI
Configurazione hardware:
Pin 26 --> Ricevitore
Pin 14 --> Trasmettitore

# Software:
Python3

# Development plattform:
Visual Studio Code

# Target plattform:
Raspberry Pi

## Download
git command to download repository content on target is following:
**first time**
git clone <link to repository>
**then**
git pull 

## Configurazione Raspberry
Seguiamo le istruzioni qui:
https://gist.github.com/billpatrianakos/708e461491b038b6e274448ca7daa154

con le seguenti varianti:
# Variante 1
L'installazione semrbra non avvenire correttamente, forse perchè manca i file di configurazione che non vengono creati correttamente...
# Variante 2
Add the following lines in /boot/config.txt
dtoverlay=gpio-ir,gpio_pin=26
dtoverlay=gpio-ir-tx,gpio_pin=14


