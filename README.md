# MS60S_Reader Library

## Overview

The MS60S_Reader library provides a Python interface for reading data from the EKO MS60S Pyranometer using Modbus RTU communication. This library simplifies the process of retrieving various measurements from the pyranometer, including irradiance, tilt angles, temperature, and humidity.

## Features

- Easy-to-use interface for the EKO MS60S Pyranometer
- Supports reading individual values or all values at once
- Provides methods for reading:
  - Compensated Irradiance
  - X and Y Tilt Angles
  - Raw Irradiance
  - Analogue Voltage
  - Internal Temperature
  - Internal Humidity

## Installation

Before using this library, you need to install the `minimalmodbus` library. You can install it using pip:

```bash
pip install minimalmodbus
```

## Usage

### Importing the Library

```python
from ms60s_reader import MS60S_Reader
```

### Creating an Instance

Create an instance of the MS60S_Reader class by specifying the serial port and device ID:

```python
reader = MS60S_Reader('/dev/ttyUSB0', 25)
```

### Reading All Values

To read all available values from the pyranometer:

```python
values = reader.read_all_values()
print(values)
```

### Reading Individual Values

You can read individual values using specific methods:

```python
comp_irr = reader.read_compensated_irradiance()
x_tilt = reader.read_x_tilt()
temperature = reader.read_internal_temperature()
```

### Closing the Connection

Always close the connection after use:

```python
reader.close()
```

## Input Parameters

- `port` (str): The serial port to which the pyranometer is connected (e.g., '/dev/ttyUSB0')
- `device_id` (int): The Modbus device ID of the pyranometer

## Output

The `read_all_values()` method returns a dictionary with the following keys:

- `compensated_irradiance` (float): Compensated irradiance measurement
- `x_tilt` (float): X-axis tilt angle
- `y_tilt` (float): Y-axis tilt angle
- `raw_irradiance` (float): Raw irradiance measurement
- `analogue_voltage` (float): Analogue voltage reading
- `internal_temperature` (float): Internal temperature of the pyranometer
- `internal_humidity` (float): Internal humidity of the pyranometer

## Example

```python
from ms60s_reader import MS60S_Reader

try:
    reader = MS60S_Reader('/dev/ttyUSB0', 25)
    values = reader.read_all_values()
    print(f"Compensated Irradiance: {values['compensated_irradiance']:.2f} W/m²")
    print(f"X-axis Tilt Angle: {values['x_tilt']:.2f}°")
    print(f"Y-axis Tilt Angle: {values['y_tilt']:.2f}°")
    print(f"Internal Temperature: {values['internal_temperature']:.2f}°C")
except Exception as e:
    print(f"Error: {e}")
finally:
    reader.close()
```

## Error Handling

The library uses try-except blocks to handle potential errors. Make sure to implement proper error handling in your code when using this library.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions to improve the MS60S_Reader library are welcome. Please feel free to submit pull requests or open issues on the GitHub repository.

## Support

If you encounter any problems or have any questions, please open an issue on the GitHub repository.
