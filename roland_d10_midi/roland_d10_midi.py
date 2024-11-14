#      _                                       _     _ _     _
#   __| | __ _  ___ _ __ ___   ___  _ __   ___| |__ (_) | __| |
#  / _` |/ _` |/ _ \ '_ ` _ \ / _ \| '_ \ / __| '_ \| | |/ _` |
# | (_| | (_| |  __/ | | | | | (_) | | | | (__| | | | | | (_| |
#  \__,_|\__,_|\___|_| |_| |_|\___/|_| |_|\___|_| |_|_|_|\__,_|
#
#
#  	Title:		            Roland D10 Midi Utilities
#

import mido
from colorama import Fore, Back, Style


# Send a complete patch dump file (factory reset)
def send_patch_dump (midi_out_port_name, midi_file_name):

    port = mido.open_output(midi_out_port_name)
    midi_data = mido.MidiFile(midi_file_name)
    for msg in midi_data.play():
        print (".", end='')
        port.send(msg)
    print ()


def display_info ():

    print (Fore.CYAN + "Local MIDI Hardware ports:" + Style.RESET_ALL)
    print (f"Output Ports: {mido.get_output_names()}")
    print (f"Input Ports: {mido.get_input_names()}")
    print ()
    print (f"Use these full strings to reference MIDI ports.")
    print ()

display_info()
factory_patches_filename = 'patches/d5-d10-d20-factory/D5__ORIG.MID'

# Example using Presonus 1810 USB-C interface:
# midi_port_name = 'Studio 1810c:Studio 1810c MIDI 1 20:0'
# send_patch_dump (midi_port_name, factory_patches_filename)

