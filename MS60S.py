"""
MS60S_Reader Library

Usage:
1. Create an instance of the MS60S_Reader class.
   Example: reader = MS60S_Reader('/dev/ttyUSB0', 25)

2. Call the read_all_values() method to read all values.
   Example: values = reader.read_all_values()

3. To read individual values, call the respective methods.
   Example: comp_irr = reader.read_compensated_irradiance()

4. After use, call the close() method to close the connection.
   Example: reader.close()

Note: Before using this library, install the 'minimalmodbus' library.
Installation command: pip install minimalmodbus
"""

import minimalmodbus
import serial

class MS60S_Reader:
    def __init__(self, port, device_id): # From Datasheet, MS60S
        self.instrument = minimalmodbus.Instrument(port, device_id)
        self.instrument.serial.baudrate = 19200
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity = serial.PARITY_EVEN
        self.instrument.serial.stopbits = 1
        self.instrument.serial.timeout = 1
        self.instrument.mode = minimalmodbus.MODE_RTU

    def read_compensated_irradiance(self): #Reg 2~3 
        return self.instrument.read_float(2, functioncode=3, number_of_registers=2)

    def read_x_tilt(self):                 #Reg 14~15
        return self.instrument.read_float(14, functioncode=3, number_of_registers=2)

    def read_y_tilt(self):                 #Reg 16~17
        return self.instrument.read_float(16, functioncode=3, number_of_registers=2)

    def read_raw_irradiance(self):         #Reg 18~19
        return self.instrument.read_float(18, functioncode=3, number_of_registers=2)

    def read_analogue_voltage(self):       #Reg 20~21
        return self.instrument.read_float(20, functioncode=3, number_of_registers=2)

    def read_internal_temperature(self):   #Reg 22~23
        return self.instrument.read_float(22, functioncode=3, number_of_registers=2)

    def read_internal_humidity(self):      #Reg 24~25
        return self.instrument.read_float(24, functioncode=3, number_of_registers=2)

    def read_all_values(self):
        return {
            'compensated_irradiance': self.read_compensated_irradiance(),
            'x_tilt': self.read_x_tilt(),
            'y_tilt': self.read_y_tilt(),
            'raw_irradiance': self.read_raw_irradiance(),
            'analogue_voltage': self.read_analogue_voltage(),
            'internal_temperature': self.read_internal_temperature(),
            'internal_humidity': self.read_internal_humidity()
        }

    def read_all_values_abb(self):
        return {
            'eko_pyra-comp_irr': self.read_compensated_irradiance(),
            'eko_pyra-x_tilt': self.read_x_tilt(),
            'eko_pyra-y_tilt': self.read_y_tilt(),
            'eko_pyra-raw_irr': self.read_raw_irradiance(),
            'eko_pyra-ad_mv': self.read_analogue_voltage(),
            'eko_pyra-inter_temp': self.read_internal_temperature(),
            'eko_pyra-inter_humi': self.read_internal_humidity()
        }

    def close(self):
        self.instrument.serial.close()

# Usage example
if __name__ == "__main__":
    try:
        reader = MS60S_Reader('/dev/ttyUSB0', 25)
        values = reader.read_all_values()
        print(f"Compensated Irradiance: {values['compensated_irradiance']:.2f}")
        print(f"X-axis Tilt Angle: {values['x_tilt']:.2f}")
        print(f"Y-axis Tilt Angle: {values['y_tilt']:.2f}")
        print(f"Internal Temperature: {values['internal_temperature']:.2f}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        reader.close()