# This is a simple API expoing my homelab's power draw. 

### I am using Linear Interpolation to extrapolate power draw for components that do not report their power consumption.

Devices using Interpolation:
```
HGST 12TB Drive x2
WD HGST 12TB Drive x 1
NVIDIA Quadro P400 PNY
```

### I am using PSU efficiency data to normalize my readings to different load levels, using results of riggorous testing of the same power supply by GamersNexus.


## Django Setup
Make sure to run the following commands in order to setup the DB for the first run:
```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

Make sure to edit the initial_data.json file with your hardware specifications, and then run:

```bash
python manage.py loaddata initial_data.json
```

Finally, before running the app for the first time, make sure to rename the .env.example file to .env and update the relevant values within it.

## Celery
Celery is used to asynchronously run tasks to update HDD usage and estimated wattage. In order to run celery alongside the Django server, execute the following commands in separate terminals:
```bash
celery -A powerapi worker --loglevel=error
```

```bash
celery -A powerapi beat --loglevel=error
```

### CPU Power Draw

*Please consult the following GitHub page to see compatability and updated installation instructions.* 

As of writing this, the following commands can be run to install Likwid to measure CPU PKG power draw, as well as DRAM power draw.

```bash
VERSION=stable
wget http://ftp.fau.de/pub/likwid/likwid-$VERSION.tar.gz
tar -xaf likwid-$VERSION.tar.gzcd likwid
cd likwid-*
make
sudo make install
```