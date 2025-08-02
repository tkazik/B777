# B777

Some notes / memos for the CA B777

## Important stuff

Mnemonic 9/14/26/8:

* 9 memory items
* 14 quick action index (time critical)
* 26 unannunciated checklists (not sensed by acft, e.g. fuel leak)
* 8 non-normal maneuvers (e.g. stall, wind shear)

### Memory items

General:

* initiated with **"__ MEMORY ITEMS"**
* **"CONFIRM"** is used for items with irreversible or immediate effect
* terminated with **"__ MEMORY ITEMS COMPLETE"**
* separator symbol **"---"** separates memory items from reference items

Once FLY/NAV/COM is completed, the aircraft is no longer in a critical flight phase and all memory items are completed: continue with NNC (might be unannunciated).

### quick action index

* Aborted Engine Start L, R
* Airspeed Unreliable
* [] CABIN ALTITUDE
* Dual Eng Fail/Stall
* [] ENG AUTOSTART L, R
* Eng Lim/Surge/Stall L, R
* Eng Svr Damage/Sep L, R
* Evacuation
* [] FIRE APU
* [] FIRE ENG L, R
* Fire Eng on Ground L, R
* Fire Eng Tailpipe L, R
* Smoke, Fire or Fumes
* [] STABILIZER

### APPROACH TO STALL OR STALL RECOVERY

### ENGINE INOPERATIVE CRUISE / DRIFT DOWN PROCEDURE

### GROUND PROXIMITY WARNING SYSTEM (GPWS) RESPONSE

#### GPWS Caution

#### GPWS Warning

### REJECTED TAKEOFF

### RUNWAY AWARENESS AND ADVISORY SYSTEM (RAAS)

### TRAFFIC AVOIDANCE

### UPSET RECOVERY

### WINDSHEAR

#### Windshear Caution

Aural alert: "MONITOR RADAR DISPLAY"

| Pilot Flying | Pilot Monitoring |
| ------------ |------------------|
| Maneuver as required to avoid the windshear | monitor |

#### Windshear Warning

Multiple aural alerts possible:

* Predictive windshear (PWS):
  * during T/O: "WINDSHEAR AHEAD, WINDSHEAR AHEAD"
  * during APP: "GO-AROUND, WINDSHEAR AHEAD"
* (Actual) windshear encountered: "WINDSHEAR, WINDSHEAR, WINDSHEAR"

During T/O (PWS: "windshear ahead"):

* before V1: [reject T/O](#rejected-takeoff) (Note: RWY might still be insufficient)
* after V1: perform [windshear escape maneuver](#windshear-escape-maneuver) (Note: rotate latest 2'000ft before end of RWY)

During APP (PWS: "go-around, windshear ahead"):

* perform [windshear escape maneuver](#windshear-escape-maneuver) OR
* pilot discretion: normal go-around

##### Windshear Escape Maneuver

| Pilot Flying | Pilot Monitoring |
| ------------ |------------------|
| *MANUAL FLIGHT* <br>Call: **"WINDSHEAR, I have control"**<br>Disengage autopilot<br>Push either TO/GA switch<br>Aggressively apply maximum* thrust<br>Disconnect autothrottle(s)<br>Simultaneously roll wings level and rotate toward an initial pitch attitude of 15°<br>Retract speedbrakes<br>Follow flight director TO/GA guidance (if available)** | <br>Verify maximum* thrust<br>Call: **"THRUST SET"**<br>Verify all required actions have been completed and call out any omissions |
| *AUTOMATIC FLIGHT* <br>Call: **"WINDSHEAR, I have control"**<br> Push either TO/GA switch*** <br> Verify TO/GA mode annunciation<br> Verify GA* thrust<br> Retract speedbrakes<br>Monitor system performance**** | <br>Verify maximum* thrust<br>Call: **"THRUST SET"** <br>Verify all required actions have been completed and call out any omissions |

| Pilot Flying | Pilot Monitoring |
| ------------ |------------------|
| *MANUAL OR AUTOMATIC FLIGHT* <br>Do not change gear or flap configuration until windshear is no longer a factor<br> Maintain wings level to maximize climb gradient, unless a turn is required for obstacle clearance<br> Monitor vertical speed and altitude<br> Do not attempt to regain lost airspeed until windshear is no longer a factor | Monitor vertical speed and altitude<br>Call out any trend toward terrain contact, descending flight path, or significant airspeed changes |

Notes:
* max thrust, levers fully forward (ok if EEC in normal mode). If terrrain a factor: fully forward.
* Do not exceed pitch limit indication
* If TO/GA not avail, disengage AP and A/T and fly manually
* severe WS may exceed capabilities of AFDS: Prepare to disconnect AP & A/T