# RaspberryPi_Configuration

## Configurazione Raspberry Tentativo 1
Seguiamo le istruzioni qui:
https://gist.github.com/billpatrianakos/708e461491b038b6e274448ca7daa154

con le seguenti varianti:
### Variante 1
L'installazione semrbra non avvenire correttamente, forse perchè manca i file di configurazione che non vengono creati correttamente...
### Variante 2
Add the following lines in /boot/config.txt
dtoverlay=gpio-ir,gpio_pin=26
dtoverlay=gpio-ir-tx,gpio_pin=14

Purtroppo semrba esserci il problema che non legge da lirc0 ma solo da lirc 1
# Test that you can get IR data
$ sudo systemctl stop lircd.service
$ sudo systemctl stop lircd.socket
$ sudo mode2 --driver default --device /dev/lirc0



## Configurazione raspberry Tentativo 2
Seguiamo le istruzioni qui:
https://gist.github.com/billpatrianakos/cb72e984d4730043fe79cbe5fc8f7941





