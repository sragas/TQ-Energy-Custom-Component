import requests
import simplejson

from .const import _LOGGER, BASE_URL, LOGIN_PATH, READ_PATH


class TQEnergyManagementApi(object):
    def __init__(self, host, port, password):
        self._host = host
        self._port = port
        self._password = password
        self.session_id = ''
        self.serial_number = ''
        self.authenticated = False

    def send_request(self):
        url = BASE_URL.format(self._host, self._port, READ_PATH)
        try:
            cookies = {'PHPSESSID': self.session_id}
            response = requests.get(url, timeout=30, cookies=cookies)
            if response.status_code == 200:
                dataObj = response.json()
                if 'authentication' in dataObj and dataObj['authentication'] == False:
                    self.authenticated = False
                    self.login()
                else:
                    return dataObj
        except requests.exceptions.HTTPError as errh:
            _LOGGER.error("Http Error: %s", errh)
        except requests.exceptions.ConnectionError as errc:
            _LOGGER.error("Error Connecting: %s", errc)
        except requests.exceptions.Timeout as errt:
            _LOGGER.error("Timeout Error: %s", errt)
        except requests.exceptions.RequestException as err:
            _LOGGER.error("Something went wrong: %s", err)
        except simplejson.errors.JSONDecodeError as jerr:
            _LOGGER.error("Could not decode json: %s", jerr)
        except Exception as error:
            _LOGGER.error("Something else went wrong: %s", error)
        return None

    def login(self):
        self.init_session()
        self.authenticate()

    def init_session(self):
        url = BASE_URL.format(self._host, self._port, LOGIN_PATH)
        response = requests.get(url, timeout=30)
        if response.status_code == 200 and response.cookies['PHPSESSID']:
            self.session_id = response.cookies['PHPSESSID']
            init_obj = response.json()
            if init_obj['serial']:
                self.serial_number = init_obj['serial']
            else:
                raise Exception("Could not init session!")
        else:
            raise Exception("Could not init session!")

    def authenticate(self):
        url = BASE_URL.format(self._host, self._port, LOGIN_PATH)
        post_params = {'login': self.serial_number, 'password': self._password}
        cookies = {'PHPSESSID': self.session_id}
        response = requests.post(url, timeout=30, data=post_params, cookies=cookies)
        if response.status_code == 200:
            authentication_obj = response.json();
            if authentication_obj['authentication'] == True:
                self.authenticated = True
        else:
            raise Exception("Could not login!")

    def changeobiskeys(self, response):
        jsoninput = response
        jsoninput["active_power_incoming"] = jsoninput.pop("1-0:1.4.0*255")
        jsoninput["active_energy_incoming"] = jsoninput.pop("1-0:1.8.0*255")
        jsoninput["apparent_power_outgoing"] = jsoninput.pop("1-0:10.4.0*255")
        jsoninput["apparent_energy_outgoing"] = jsoninput.pop("1-0:10.8.0*255")
        jsoninput["power_factor"] = jsoninput.pop("1-0:13.4.0*255")
        jsoninput["supply_frequency"] = jsoninput.pop("1-0:14.4.0*255")
        jsoninput["active_power_outgoing"] = jsoninput.pop("1-0:2.4.0*255")
        jsoninput["active_energy_outgoing"] = jsoninput.pop("1-0:2.8.0*255")
        jsoninput["active_power_incoming_l1"] = jsoninput.pop("1-0:21.4.0*255")
        jsoninput["active_energy_incoming_l1"] = jsoninput.pop("1-0:21.8.0*255")
        jsoninput["active_power_outgoing_l1"] = jsoninput.pop("1-0:22.4.0*255")
        jsoninput["active_energy_outgoing_l1"] = jsoninput.pop("1-0:22.8.0*255")
        jsoninput["reactive_power_incoming_l1"] = jsoninput.pop("1-0:23.4.0*255")
        jsoninput["reactive_energy_incoming_l1"] = jsoninput.pop("1-0:23.8.0*255")
        jsoninput["reactive_power_outgoing_l1"] = jsoninput.pop("1-0:24.4.0*255")
        jsoninput["reactive_energy_outgoing_l1"] = jsoninput.pop("1-0:24.8.0*255")
        jsoninput["apparent_power_incoming_l1"] = jsoninput.pop("1-0:29.4.0*255")
        jsoninput["apparent_energy_incoming_l1"] = jsoninput.pop("1-0:29.8.0*255")
        jsoninput["reactive_power_incoming"] = jsoninput.pop("1-0:3.4.0*255")
        jsoninput["reactive_energy_incoming"] = jsoninput.pop("1-0:3.8.0*255")
        jsoninput["apparent_power_outgoing_l1"] = jsoninput.pop("1-0:30.4.0*255")
        jsoninput["apparent_energy_outgoing_l1"] = jsoninput.pop("1-0:30.8.0*255")
        jsoninput["current_l1"] = jsoninput.pop("1-0:31.4.0*255")
        jsoninput["voltage_l1"] = jsoninput.pop("1-0:32.4.0*255")
        jsoninput["power_factor_l1"] = jsoninput.pop("1-0:33.4.0*255")
        jsoninput["reactive_power_outgoing"] = jsoninput.pop("1-0:4.4.0*255")
        jsoninput["reactive_energy_outgoing"] = jsoninput.pop("1-0:4.8.0*255")
        jsoninput["active_power_incoming_l2"] = jsoninput.pop("1-0:41.4.0*255")
        jsoninput["active_energy_incoming_l2"] = jsoninput.pop("1-0:41.8.0*255")
        jsoninput["active_power_outgoing_l2"] = jsoninput.pop("1-0:42.4.0*255")
        jsoninput["active_energy_outgoing_l2"] = jsoninput.pop("1-0:42.8.0*255")
        jsoninput["reactive_power_incoming_l2"] = jsoninput.pop("1-0:43.4.0*255")
        jsoninput["reactive_energy_incoming_l2"] = jsoninput.pop("1-0:43.8.0*255")
        jsoninput["reactive_power_outgoing_l2"] = jsoninput.pop("1-0:44.4.0*255")
        jsoninput["reactive_energy_outgoing_l2"] = jsoninput.pop("1-0:44.8.0*255")
        jsoninput["apparent_power_incoming_l2"] = jsoninput.pop("1-0:49.4.0*255")
        jsoninput["apparent_energy_incoming_l2"] = jsoninput.pop("1-0:49.8.0*255")
        jsoninput["apparent_power_outgoing_l2"] = jsoninput.pop("1-0:50.4.0*255")
        jsoninput["apparent_energy_outgoing_l2"] = jsoninput.pop("1-0:50.8.0*255")
        jsoninput["current_l2"] = jsoninput.pop("1-0:51.4.0*255")
        jsoninput["voltage_l2"] = jsoninput.pop("1-0:52.4.0*255")
        jsoninput["power_factor_l2"] = jsoninput.pop("1-0:53.4.0*255")
        jsoninput["active_power_incoming_l3"] = jsoninput.pop("1-0:61.4.0*255")
        jsoninput["active_energy_incoming_l3"] = jsoninput.pop("1-0:61.8.0*255")
        jsoninput["active_power_outgoing_l3"] = jsoninput.pop("1-0:62.4.0*255")
        jsoninput["active_energy_outgoing_l3"] = jsoninput.pop("1-0:62.8.0*255")
        jsoninput["reactive_power_incoming_l3"] = jsoninput.pop("1-0:63.4.0*255")
        jsoninput["reactive_energy_incoming_l3"] = jsoninput.pop("1-0:63.8.0*255")
        jsoninput["reactive_power_outgoing_l3"] = jsoninput.pop("1-0:64.4.0*255")
        jsoninput["reactive_energy_outgoing_l3"] = jsoninput.pop("1-0:64.8.0*255")
        jsoninput["apparent_power_incoming_l3"] = jsoninput.pop("1-0:69.4.0*255")
        jsoninput["apparent_energy_incoming_l3"] = jsoninput.pop("1-0:69.8.0*255")
        jsoninput["apparent_power_outgoing_l3"] = jsoninput.pop("1-0:70.4.0*255")
        jsoninput["apparent_energy_outgoing_l3"] = jsoninput.pop("1-0:70.8.0*255")
        jsoninput["current_l3"] = jsoninput.pop("1-0:71.4.0*255")
        jsoninput["voltage_l3"] = jsoninput.pop("1-0:72.4.0*255")
        jsoninput["power_factor_l3"] = jsoninput.pop("1-0:73.4.0*255")
        jsoninput["apparent_power_incoming"] = jsoninput.pop("1-0:9.4.0*255")
        jsoninput["apparent_energy_incoming"] = jsoninput.pop("1-0:9.8.0*255")
        # serial
        # status
        return jsoninput

    def fetch_data(self):
        return self.update()

    def update(self):
        sensors = {}
        if not self.authenticated:
            self.login()

        if self.authenticated:
            response = self.send_request()
            if response:
                sensors = self.changeobiskeys(response)

        return sensors
