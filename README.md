# Home-Assistant Custom Components
Custom Components for Home-Assistant (http://www.home-assistant.io)

## TQ Energy - Energy Management Component
Custom component to connect to energy management devices from TQ Energy and fetch all via API available data and provide as sensor in Home Assistant.
The following models should work:

* EM1xx 
* EM2xx 
* EM3xx 

Tested and developed on EM 300 LR.
 
### Information sources
Due the lack of python coding skills, inspired by [ATAG One Thermostat Climate Component
Component](https://github.com/herikw/home-assistant-custom-components) from @herikw.
And infos from kruki out of https://www.photovoltaikforum.com/thread/128382-skript-zum-auslesen-des-b-control-energy-manager-em300/

Official JSON API documentation from TQ Group:
https://www.tq-group.com/filedownloads/files/products/automation/software_tools/energy-management/TQ_EM_JSON-API.0104.pdf
### Installation
* Create custom_components directory in Home Assistant config directory, if not exists.
* Create tqenergymanagement directory in custom_components directory
* Copy all files from this repository to custom_components/tqenergymanagement
* Create configuration.yaml entry (Details below)
* Restart Home-Assistant.

### Usage
Below are all sensors listed which are provided via TQ Energy JSON API. Availability vary on used model of Energy Monitor.
Only configured resources are shown in Home Assistant.

Could not figure out how to localize sensor names. Therefore exchange Line 95 in sensor.py for changing sensor names.

for german sensor names (default)
```python
from .sensor_names_de import SENSOR_NAMES
```

for english sensor names
```python
from .sensor_names_en import SENSOR_NAMES
```

### Example configuration.yaml entry

```
sensor:
  - platform: tqenergymanagement
    host: localhost
    [port: 80]
    password: password
    [scan_interval: 900]
    resources:
      - active_power_incoming
      - active_energy_incoming
      - active_power_outgoing
      - active_energy_outgoing      
      - apparent_power_incoming
      - apparent_energy_incoming      
      - apparent_power_outgoing
      - apparent_energy_outgoing
      - reactive_power_incoming
      - reactive_energy_incoming   
      - reactive_power_outgoing
      - reactive_energy_outgoing
      - power_factor
      - supply_frequency                  
      - active_power_incoming_l1
      - active_energy_incoming_l1
      - active_power_outgoing_l1
      - active_energy_outgoing_l1
      - reactive_power_incoming_l1
      - reactive_energy_incoming_l1
      - reactive_power_outgoing_l1
      - reactive_energy_outgoing_l1
      - apparent_power_incoming_l1
      - apparent_energy_incoming_l1
      - apparent_power_outgoing_l1
      - apparent_energy_outgoing_l1
      - current_l1
      - voltage_l1
      - power_factor_l1
      - active_power_incoming_l2
      - active_energy_incoming_l2
      - active_power_outgoing_l2
      - active_energy_outgoing_l2
      - reactive_power_incoming_l2
      - reactive_energy_incoming_l2
      - reactive_power_outgoing_l2
      - reactive_energy_outgoing_l2
      - apparent_power_incoming_l2
      - apparent_energy_incoming_l2
      - apparent_power_outgoing_l2
      - apparent_energy_outgoing_l2
      - current_l2
      - voltage_l2
      - power_factor_l2
      - active_power_incoming_l3
      - active_energy_incoming_l3
      - active_power_outgoing_l3
      - active_energy_outgoing_l3
      - reactive_power_incoming_l3
      - reactive_energy_incoming_l3
      - reactive_power_outgoing_l3
      - reactive_energy_outgoing_l3
      - apparent_power_incoming_l3
      - apparent_energy_incoming_l3
      - apparent_power_outgoing_l3
      - apparent_energy_outgoing_l3
      - current_l3
      - voltage_l3
      - power_factor_l3
```
