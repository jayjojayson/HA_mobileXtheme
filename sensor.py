from homeassistant.helpers.entity import Entity
from homeassistant.const import CONF_NAME
import logging

_LOGGER = logging.getLogger(__name__)

# Beispiel für einen einfachen Sensor
class MobileXThemeSensor(Entity):
    """Sensor für HA mobileXTheme."""

    def __init__(self, name: str, state: str):
        """Initialisierung des Sensors."""
        self._name = name
        self._state = state

    @property
    def name(self):
        """Der Name des Sensors."""
        return self._name

    @property
    def state(self):
        """Der Zustand des Sensors."""
        return self._state

    @property
    def icon(self):
        """Das Icon des Sensors."""
        return "mdi:theme-light-dark"

    async def async_update(self):
        """Aktualisierung des Sensorzustands."""
        # Hier können Logik und API-Aufrufe implementiert werden, um den Sensorstatus zu aktualisieren.
        _LOGGER.debug("Aktualisiere Sensor %s", self._name)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Setze die Plattform für den Sensor um."""
    # Hier fügen wir den Sensor zum Home Assistant hinzu
    sensors = []
    sensors.append(MobileXThemeSensor(name="MobileXTheme Sensor", state="Online"))
    
    async_add_entities(sensors)
    _LOGGER.info("MobileXTheme-Sensoren wurden hinzugefügt.")

