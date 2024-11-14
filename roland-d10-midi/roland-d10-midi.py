import mido 

print (f"Output Ports: {mido.get_output_names()}")
print (f"Input Ports: {mido.get_input_names()}")

midiport_out = 'Studio 1810c:Studio 1810c MIDI 1 20:0'
midiport_in = 'Studio 1810c:Studio 1810c MIDI 1 20:0'
midipatch_file = 'patches/d5-d10-d20-factory/D5__ORIG.MID'

port = mido.open_output(midiport_out)

mid = mido.MidiFile(midipatch_file)
for msg in mid.play():
    port.send(msg)