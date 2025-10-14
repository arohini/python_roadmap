
# Datatypes

# integer data type, which can hold +, - values and has no limits except for RAM or ROM space
speed_kph = 80
rpm = 3000
print(f"speed kilometer per hour is {speed_kph} \
      and its type is : {type(speed_kph)}")  # <class 'int'>

engine_temp = 98.6
battery_voltage = 12.4
print(engine_temp, "==>", battery_voltage)
print(type(engine_temp))  # <class 'float'>

# Boolean - Logical values, either True or False.
engine_on = True
doors_closed = False
print(engine_on, "==>", doors_closed)
print(type(engine_on))  # <class 'bool'>

# String - A sequence of characters (letters, numbers, symbols).
vehicle_model = "Tesla Model 3"
vin = "5YJ3E1EA7HF000316"
print(vehicle_model, "==>", vin)
print(type(vehicle_model))  # <class 'str'>

# List - Ordered, changeable collection of items. Can hold any data types.
sensor_readings = [21.4, 22.0, 21.9, 22.3]
can_ids = [0x120, 0x1F2, 0x0A3]
print(sensor_readings, "CAN IDS", can_ids)
print(sensor_readings[1])     # Accessing 2nd element from the sensor_readings list
print(type(can_ids))          # <class 'list'>

# Tuple - Like a list, but immutable (cannot be changed after creation).
gps_coordinates = (52.5200, 13.4050)
print(gps_coordinates)
print(gps_coordinates[1])  # 52.5200

# Dict - A collection of key-value pairs.
vehicle_data = {
    "model": "Ford F-150",
    "speed_kph": 90,
    "rpm": 2500,
    "fuel_level": 54.3,
    "engine_on": True,
    "error_codes": {"P0171", "P0301"},
    "gps": (40.7128, -74.0060)
}

print(f"{vehicle_data['model']} is going {vehicle_data['speed_kph']} km/h")