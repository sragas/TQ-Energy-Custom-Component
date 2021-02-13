"""
Adds Support for TQ Energy Management

Configuration for this platform:

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
"""

from datetime import timedelta
import voluptuous as vol
import async_timeout

from .tqenergymanagementapi import TQEnergyManagementApi
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from homeassistant.components.sensor import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as config_validation
from homeassistant.const import (
    CONF_HOST,
    CONF_PORT,
    CONF_RESOURCES,
    CONF_PASSWORD,
    CONF_NAME,
    CONF_SCAN_INTERVAL
)

from homeassistant.helpers.entity import Entity

from .const import DEFAULT_NAME, _LOGGER, MIN_UPDATE_INTERVAL, DEFAULT_UPDATE_INTERVAL
from .sensor_names_de import SENSOR_NAMES

SENSOR_TYPES = {
    "active_power_incoming" : ["W", "mdi:flash"],
    "active_energy_incoming" : ["Wh", "mdi:flash"],
    "apparent_power_outgoing" : ["W", "mdi:flash"],
    "apparent_energy_outgoing" : ["VAh", "mdi:flash"],
    "apparent_power_incoming" : ["W", "mdi:flash"],
    "apparent_energy_incoming" : ["VAh", "mdi:flash"],
    "active_power_outgoing" : ["W", "mdi:flash"],
    "active_energy_outgoing" : ["Wh", "mdi:flash"],
    "power_factor" : ["", "mdi:flash"],
    "supply_frequency" : ["Hz", "mdi:flash"],
    "active_power_incoming_l1" : ["W", "mdi:flash"],
    "active_energy_incoming_l1" : ["Wh", "mdi:flash"],
    "active_power_outgoing_l1" : ["W", "mdi:flash"],
    "active_energy_outgoing_l1" : ["Wh", "mdi:flash"],
    "reactive_power_incoming_l1" : ["Var", "mdi:flash"],
    "reactive_energy_incoming_l1" : ["Varh", "mdi:flash"],
    "reactive_power_outgoing_l1" : ["Var", "mdi:flash"],
    "reactive_energy_outgoing_l1" : ["Varh", "mdi:flash"],
    "apparent_power_incoming_l1" : ["W", "mdi:flash"],
    "apparent_energy_incoming_l1" : ["VAh", "mdi:flash"],
    "reactive_power_incoming" : ["Var", "mdi:flash"],
    "reactive_energy_incoming" : ["Varh", "mdi:flash"],
    "apparent_power_outgoing_l1" : ["W", "mdi:flash"],
    "apparent_energy_outgoing_l1" : ["VAh", "mdi:flash"],
    "current_l1" : ["A", "mdi:flash"],
    "voltage_l1" : ["V", "mdi:flash"],
    "power_factor_l1" : ["", "mdi:flash"],
    "reactive_power_outgoing" : ["Var", "mdi:flash"],
    "reactive_energy_outgoing" : ["Varh", "mdi:flash"],
    "active_power_incoming_l2" : ["W", "mdi:flash"],
    "active_energy_incoming_l2" : ["Wh", "mdi:flash"],
    "active_power_outgoing_l2" : ["W", "mdi:flash"],
    "active_energy_outgoing_l2" : ["Wh", "mdi:flash"],
    "reactive_power_incoming_l2" : ["Var", "mdi:flash"],
    "reactive_energy_incoming_l2" : ["Varh", "mdi:flash"],
    "reactive_power_outgoing_l2" : ["Var", "mdi:flash"],
    "reactive_energy_outgoing_l2" : ["Varh", "mdi:flash"],
    "apparent_power_incoming_l2" : ["W", "mdi:flash"],
    "apparent_energy_incoming_l2" : ["VAh", "mdi:flash"],
    "apparent_power_outgoing_l2" : ["W", "mdi:flash"],
    "apparent_energy_outgoing_l2" : ["VAh", "mdi:flash"],
    "current_l2" : ["A", "mdi:flash"],
    "voltage_l2" : ["V", "mdi:flash"],
    "power_factor_l2" : ["", "mdi:flash"],
    "active_power_incoming_l3" : ["W", "mdi:flash"],
    "active_energy_incoming_l3" : ["Wh", "mdi:flash"],
    "active_power_outgoing_l3" : ["W", "mdi:flash"],
    "active_energy_outgoing_l3" : ["Wh", "mdi:flash"],
    "reactive_power_incoming_l3" : ["Var", "mdi:flash"],
    "reactive_energy_incoming_l3" : ["Varh", "mdi:flash"],
    "reactive_power_outgoing_l3" : ["Var", "mdi:flash"],
    "reactive_energy_outgoing_l3" : ["Varh", "mdi:flash"],
    "apparent_power_incoming_l3" : ["W", "mdi:flash"],
    "apparent_energy_incoming_l3" : ["VAh", "mdi:flash"],
    "apparent_power_outgoing_l3" : ["W", "mdi:flash"],
    "apparent_energy_outgoing_l3" : ["VAh", "mdi:flash"],
    "current_l3" : ["A", "mdi:flash"],
    "voltage_l3" : ["V", "mdi:flash"],
    "power_factor_l3" : ["", "mdi:flash"]
}

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_HOST): config_validation.string,
        vol.Required(CONF_PASSWORD): config_validation.string,
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): config_validation.string,
        vol.Optional(CONF_PORT, default=80): config_validation.positive_int,
        vol.Optional(CONF_SCAN_INTERVAL, default=DEFAULT_UPDATE_INTERVAL): (
            vol.All(config_validation.time_period, vol.Clamp(min=MIN_UPDATE_INTERVAL))
        ),
        vol.Required(CONF_RESOURCES, default=[]): vol.All(
            config_validation.ensure_list, [vol.In(SENSOR_TYPES)]
        ),
    }
)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Setup sensors."""

    api = TQEnergyManagementApi(config.get(CONF_HOST), config.get(CONF_PORT), config.get(CONF_PASSWORD))

    async def async_update_data():
        async with async_timeout.timeout(10):
            data = await hass.async_add_executor_job(api.fetch_data)
            return data
    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name="tqenergymanagement_sensor",
        update_method=async_update_data,
        update_interval=config.get(CONF_SCAN_INTERVAL),
    )

    await coordinator.async_refresh()

    entities = []
    sensor_prefix = config.get(CONF_NAME)

    for resource in config[CONF_RESOURCES]:
        sensor_type = resource.lower()

        if sensor_type not in SENSOR_TYPES:
            SENSOR_TYPES[sensor_type] = ["", "mdi:flash"]

        entities.append(TQEnergySensor(coordinator, sensor_type, sensor_prefix))

    async_add_entities(entities)


class TQEnergySensor(Entity):
    def __init__(self, coordinator, sensor_type, sensor_prefix):
        """Initialize the sensor."""
        self.coordinator = coordinator
        self.type = sensor_type
        self._last_updated = None
        self._sensor_prefix = sensor_prefix
        self._entity_type = self.type
        if self.type in SENSOR_NAMES:
            self._name = SENSOR_NAMES[self.type]
        else:    
           self._name = "{} {}".format(sensor_prefix, self.type)
        self._unit = SENSOR_TYPES[self.type][0]
        self._icon = SENSOR_TYPES[self.type][1]
        self._state = self.state

    @property
    def should_poll(self):
        """No need to poll. Coordinator notifies entity of updates."""
        return False

    @property
    def available(self):
        """Return if entity is available."""
        return self.coordinator.last_update_success

    async def async_added_to_hass(self):
        """When entity is added to hass."""
        self.coordinator.async_add_listener(self.async_write_ha_state)

    async def async_will_remove_from_hass(self):
        """When entity will be removed from hass."""
        self.coordinator.async_remove_listener(self.async_write_ha_state)

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def unique_id(self):
        """Return the unique ID of the binary sensor."""
        return f"{self._sensor_prefix}_{self._entity_type}"

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return self._icon

    @property
    def state(self):
        """Return the state of the sensor."""
        try:
            if self.coordinator.data:
                return self.coordinator.data[self.type]
        except KeyError:
            _LOGGER.error("can't find %s", self.type)
        return None

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement of this entity, if any."""
        return self._unit

    @property
    def device_state_attributes(self):
        """Return the state attributes of this device."""
        attr = {}
        if self._last_updated is not None:
            attr["Last Updated"] = self._last_updated
        return attr

    async def async_update(self):
        """Update Entity
        Only used by the generic entity update service."""
        await self.coordinator.async_request_refresh()