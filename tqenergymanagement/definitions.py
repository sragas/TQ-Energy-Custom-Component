from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Tuple

from homeassistant.components.sensor import (STATE_CLASS_MEASUREMENT,
                                             SensorEntityDescription)
from homeassistant.const import (DEVICE_CLASS_CURRENT, DEVICE_CLASS_ENERGY,
                                 DEVICE_CLASS_POWER, DEVICE_CLASS_POWER_FACTOR,
                                 DEVICE_CLASS_VOLTAGE, ELECTRIC_CURRENT_AMPERE,
                                 ELECTRIC_POTENTIAL_VOLT, ENERGY_WATT_HOUR,
                                 FREQUENCY_HERTZ, POWER_WATT)
from homeassistant.util import dt as dt_util

APPARENT_ENERGY = "VAh"
REACTIVE_POWER = "Var"
REACTIVE_ENERGY = "Varh"

@dataclass
class TQEnergyManagementSensorEntityDescription(SensorEntityDescription):
    """Sensor entity description for TQ Energy Management."""

    state: Callable | None = None

SENSORS: Tuple[TQEnergyManagementSensorEntityDescription, ...] = (
    TQEnergyManagementSensorEntityDescription(
        key="active_power_incoming",
        unit_of_measurement=POWER_WATT,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="active_energy_incoming",
        unit_of_measurement=ENERGY_WATT_HOUR,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_MEASUREMENT,
        last_reset=dt_util.utc_from_timestamp(0)
    ),
    TQEnergyManagementSensorEntityDescription(
        key="apparent_power_outgoing",
        unit_of_measurement=POWER_WATT,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="apparent_energy_outgoing",
        unit_of_measurement=APPARENT_ENERGY,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY
    ),
    TQEnergyManagementSensorEntityDescription(
        key="apparent_power_incoming",
        unit_of_measurement=POWER_WATT,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="apparent_energy_incoming",
        unit_of_measurement=APPARENT_ENERGY,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_MEASUREMENT,
        last_reset=dt_util.utc_from_timestamp(0)
    ),
    TQEnergyManagementSensorEntityDescription(
        key="active_power_outgoing",
        unit_of_measurement=POWER_WATT,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="active_energy_outgoing",
        unit_of_measurement=ENERGY_WATT_HOUR,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY
    ),
    TQEnergyManagementSensorEntityDescription(
        key="power_factor",
        unit_of_measurement="",
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER_FACTOR
    ),
    TQEnergyManagementSensorEntityDescription(
        key="supply_frequency",
        unit_of_measurement=FREQUENCY_HERTZ,
        icon="mdi:flash"
    ),
    TQEnergyManagementSensorEntityDescription(
        key="active_power_incoming_l1",
        unit_of_measurement=POWER_WATT,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="active_energy_incoming_l1",
        unit_of_measurement=ENERGY_WATT_HOUR,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_MEASUREMENT,
        last_reset=dt_util.utc_from_timestamp(0)
    ),
    TQEnergyManagementSensorEntityDescription(
        key="active_power_outgoing_l1",
        unit_of_measurement=POWER_WATT,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="active_energy_outgoing_l1",
        unit_of_measurement=ENERGY_WATT_HOUR,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY
    ),
    TQEnergyManagementSensorEntityDescription(
        key="reactive_power_incoming_l1",
        unit_of_measurement=REACTIVE_POWER,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="reactive_energy_incoming_l1",
        unit_of_measurement=REACTIVE_ENERGY,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY
    ),
    TQEnergyManagementSensorEntityDescription(
        key="reactive_power_outgoing_l1",
        unit_of_measurement=REACTIVE_POWER,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="reactive_energy_outgoing_l1",
        unit_of_measurement=REACTIVE_ENERGY,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_MEASUREMENT,
        last_reset=dt_util.utc_from_timestamp(0)
    ),
    TQEnergyManagementSensorEntityDescription(
        key="apparent_power_incoming_l1",
        unit_of_measurement=POWER_WATT,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="apparent_energy_incoming_l1",
        unit_of_measurement=APPARENT_ENERGY,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_MEASUREMENT,
        last_reset=dt_util.utc_from_timestamp(0)
    ),
    TQEnergyManagementSensorEntityDescription(
        key="reactive_power_incoming",
        unit_of_measurement=REACTIVE_POWER,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="reactive_energy_incoming",
        unit_of_measurement=REACTIVE_ENERGY,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY
    ),
    TQEnergyManagementSensorEntityDescription(
        key="apparent_power_outgoing_l1",
        unit_of_measurement=POWER_WATT,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="apparent_energy_outgoing_l1",
        unit_of_measurement=APPARENT_ENERGY,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY
    ),
    TQEnergyManagementSensorEntityDescription(
        key="current_l1",
        unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_CURRENT
    ),
    TQEnergyManagementSensorEntityDescription(
        key="voltage_l1",
        unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_VOLTAGE
    ),
    TQEnergyManagementSensorEntityDescription(
        key="power_factor_l1",
        unit_of_measurement="",
        icon="mdi:flash"
    ),
    TQEnergyManagementSensorEntityDescription(
        key="reactive_power_outgoing",
        unit_of_measurement=REACTIVE_POWER,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="reactive_energy_outgoing",
        unit_of_measurement=REACTIVE_ENERGY,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_MEASUREMENT,
        last_reset=dt_util.utc_from_timestamp(0)
    ),
    TQEnergyManagementSensorEntityDescription(
        key="active_power_incoming_l2",
        unit_of_measurement=POWER_WATT,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="active_energy_incoming_l2",
        unit_of_measurement=ENERGY_WATT_HOUR,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_MEASUREMENT,
        last_reset=dt_util.utc_from_timestamp(0)
    ),
    TQEnergyManagementSensorEntityDescription(
        key="active_power_outgoing_l2",
        unit_of_measurement=POWER_WATT,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="active_energy_outgoing_l2",
        unit_of_measurement=ENERGY_WATT_HOUR,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY
    ),
    TQEnergyManagementSensorEntityDescription(
        key="reactive_power_incoming_l2",
        unit_of_measurement=REACTIVE_POWER,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="reactive_energy_incoming_l2",
        unit_of_measurement=REACTIVE_ENERGY,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY
    ),
    TQEnergyManagementSensorEntityDescription(
        key="reactive_power_outgoing_l2",
        unit_of_measurement=REACTIVE_POWER,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="reactive_energy_outgoing_l2",
        unit_of_measurement=REACTIVE_ENERGY,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_MEASUREMENT,
        last_reset=dt_util.utc_from_timestamp(0)
    ),
    TQEnergyManagementSensorEntityDescription(
        key="apparent_power_incoming_l2",
        unit_of_measurement=POWER_WATT,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="apparent_energy_incoming_l2",
        unit_of_measurement=APPARENT_ENERGY,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_MEASUREMENT,
        last_reset=dt_util.utc_from_timestamp(0)
    ),
    TQEnergyManagementSensorEntityDescription(
        key="apparent_power_outgoing_l2",
        unit_of_measurement=POWER_WATT,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="apparent_energy_outgoing_l2",
        unit_of_measurement=APPARENT_ENERGY,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY
    ),
    TQEnergyManagementSensorEntityDescription(
        key="current_l2",
        unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_CURRENT
    ),
    TQEnergyManagementSensorEntityDescription(
        key="voltage_l2",
        unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_VOLTAGE
    ),
    TQEnergyManagementSensorEntityDescription(
        key="power_factor_l2",
        unit_of_measurement="",
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER_FACTOR
    ),
    TQEnergyManagementSensorEntityDescription(
        key="active_power_incoming_l3",
        unit_of_measurement=POWER_WATT,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="active_energy_incoming_l3",
        unit_of_measurement=ENERGY_WATT_HOUR,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_MEASUREMENT,
        last_reset=dt_util.utc_from_timestamp(0)
    ),
    TQEnergyManagementSensorEntityDescription(
        key="active_power_outgoing_l3",
        unit_of_measurement=POWER_WATT,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="active_energy_outgoing_l3",
        unit_of_measurement=ENERGY_WATT_HOUR,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY
    ),
    TQEnergyManagementSensorEntityDescription(
        key="reactive_power_incoming_l3",
        unit_of_measurement=REACTIVE_POWER,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="reactive_energy_incoming_l3",
        unit_of_measurement=REACTIVE_ENERGY,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY
    ),
    TQEnergyManagementSensorEntityDescription(
        key="reactive_power_outgoing_l3",
        unit_of_measurement=REACTIVE_POWER,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="reactive_energy_outgoing_l3",
        unit_of_measurement=REACTIVE_ENERGY,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_MEASUREMENT,
        last_reset=dt_util.utc_from_timestamp(0)
    ),
    TQEnergyManagementSensorEntityDescription(
        key="apparent_power_incoming_l3",
        unit_of_measurement=POWER_WATT,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="apparent_energy_incoming_l3",
        unit_of_measurement=APPARENT_ENERGY,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_MEASUREMENT,
        last_reset=dt_util.utc_from_timestamp(0)
    ),
    TQEnergyManagementSensorEntityDescription(
        key="apparent_power_outgoing_l3",
        unit_of_measurement=POWER_WATT,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER
    ),
    TQEnergyManagementSensorEntityDescription(
        key="apparent_energy_outgoing_l3",
        unit_of_measurement=APPARENT_ENERGY,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_ENERGY
    ),
    TQEnergyManagementSensorEntityDescription(
        key="current_l3",
        unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_CURRENT
    ),
    TQEnergyManagementSensorEntityDescription(
        key="voltage_l3",
        unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        icon="mdi:flash",
        device_class=DEVICE_CLASS_VOLTAGE
    ),
    TQEnergyManagementSensorEntityDescription(
        key="power_factor_l3",
        unit_of_measurement="",
        icon="mdi:flash",
        device_class=DEVICE_CLASS_POWER_FACTOR
    )
)
