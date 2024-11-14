# roland-d10-midi
MIDI Utilities for the Roland D10 LA Synth

This is a small selection of python functions to help deal with sending MIDI patches to and from the Roland D-10 synthesizer. Unless specified, they should work perfectly for the rest of the D-family too.

### Functions Provided ###

- send_patch_dump



### Other Files ###

- Original default factory patches for the D5/10/20. (A single .mid file from the archive available here: https://www.roland.com/us/support/by_product/all/general_apps_tools/4266cb94-59a1-46fe-8a00-96140588b02e/)

---
---

## How to Factory Reset using Default Patches

**Python Function:** send_patch_dump

I expect most new owners would want their keyboard back to a known good state. It was the first thing I wanted to do when I got my D-10! There are a lot of GUI based MIDI programs out there, but I had inconsistent  mixed results, so as usual I just coded my own.

The following is modified from the official Roland knowledgebase article linked below.  

The following procedures can be used to clear the internal memory and reload the factory settings:

**CAUTION: All USER information will be lost. Be sure to back up any information you wish to keep.**

D-10 and D-20 original factory data must be loaded in via MIDI or a Memory Card. 

#### Additional Notes: ####

> Note 1: Sysex MIDI data transfers require you to connect both MIDI In and Out cables. That means 'Out' from your interface to 'In' on the D-10, and vice versa.

```
PC  [OUT]  <-->  [IN]   D-10
    [IN]   <-->  [OUT] 
```


> Note 2: For factory reset, you need to set the D-10 to use MIDI Channel 1 for both TX and RX. This can be achieved using the 'Midi' button, then Value and Display to select the appropriate channel.  (Short video here: https://youtu.be/4E_Bs6xVZJQ)



### LOADING FACTORY SOUNDS VIA MIDI:

1. Press DATA TRANSFER.

2. Use DISPLAY buttons to select ONE-WAY BULK SEL.

3. Press UPPER to select LOAD.

4. Press UPPER again to select ALL.

5. Press ENTER.

6. If WRITE PROTECT is ON, turn OFF by pressing WRITE, then press ENTER.

7. The D-10 display will show "Waiting..."

8. Use the "send_patch_dump" function to send the patches.





Portions of the above text from this original article:
https://support.roland.com/hc/en-us/articles/201943799-D-20-D-10-Initializing-Restoring-the-D-10-D-20-Factory-Settings




