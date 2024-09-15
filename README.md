# This is a simple API expoing my homelab's power draw. 
## I am using Linear Interpolation to extrapolate power draw for components that do not report their power consumption.

Devices using Interpolation:
```
HGST 12TB Drive x2
Seagase 12TB Drive
NVIDIA Quadro P400 PNY  
```

### I am using PSU efficiency data to normalize my readings to different load levels, using results of riggorous testing of the same power supply by GamersNexus.


### Django Setup
Make sure to edit the initial_data.json file with your hardware specifications.
Once you've done that, perform the makemigrations and then migrate commands.