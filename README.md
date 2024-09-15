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
Make sure to run the following commandsin order to setup the DB for the first run:
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

### Celery
Celery is used to asynchronously run tasks to update HDD usage and estimated wattage. In order to run celery alongside the Django server, execute the following commands in separate terminals:
```bash
celery -A powerapi worker --loglevel=error
```

```bash
celery -A powerapi beat --loglevel=error
```