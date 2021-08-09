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

import async_timeout
import homeassistant.helpers.config_validation as config_validation
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA, SensorEntity
from homeassistant.const import (CONF_HOST, CONF_NAME, CONF_PASSWORD,
                                 CONF_PORT, CONF_RESOURCES, CONF_SCAN_INTERVAL)
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import (_LOGGER, DEFAULT_NAME, DEFAULT_UPDATE_INTERVAL,
                    MIN_UPDATE_INTERVAL)
from .definitions import SENSORS, TQEnergyManagementSensorEntityDescription
from .sensor_names_de import SENSOR_NAMES
from .tqenergymanagementapi import TQEnergyManagementApi

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_HOST): config_validation.string,
        vol.Required(CONF_PASSWORD): config_validation.string,
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): config_validation.string,
        vol.Optional(CONF_PORT, default=80): config_validation.positive_int,
        vol.Optional(CONF_SCAN_INTERVAL, default=DEFAULT_UPDATE_INTERVAL): (
            vol.All(config_validation.time_period, vol.Clamp(min=MIN_UPDATE_INTERVAL))
        ),
         vol.Required(CONF_RESOURCES, default=[]): vol.All(),
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
        update_interval=config.get(CONF_SCAN_INTERVAL)
    )

    await coordinator.async_refresh()

    entities = []
    sensor_prefix = config.get(CONF_NAME)

    for sensor in SENSORS:
        if sensor.key in config[CONF_RESOURCES]:
            entities.append(TQEnergySensor(sensor, coordinator, sensor_prefix))

    async_add_entities(entities)


class TQEnergySensor(SensorEntity):
    entity_description: TQEnergyManagementSensorEntityDescription

    def __init__(self, description: TQEnergyManagementSensorEntityDescription, coordinator, sensor_prefix):
        """Initialize the sensor."""
        self.coordinator = coordinator
        self.entity_description = description
        self.key = description.key
        self._last_updated = None
        self._sensor_prefix = sensor_prefix
        self._attr_should_poll = False

        if description.key in SENSOR_NAMES:
            self._name = SENSOR_NAMES[description.key]
        else:
            self._name = "{} {}".format(sensor_prefix, self.key)

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
    def unique_id(self):
        """Return the unique ID of the binary sensor."""
        return f"{self._sensor_prefix}_{self.key}"

    @property
    def state(self):
        """Return the state of the sensor."""
        try:
            if self.coordinator.data:
                return self.coordinator.data[self.key]
        except KeyError:
            _LOGGER.error("can't find %s", self.key)
        return None

    async def async_update(self):
        """Update Entity
        Only used by the generic entity update service."""
        await self.coordinator.async_request_refresh()
