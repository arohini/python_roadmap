"""
Common Methods In Dictionary

| Method                       | Description                                                   | Example                                        |
| ---------------------------- | ------------------------------------------------------------- | ---------------------------------------------- |
| `get(key[, default])`        | Returns the value for a key; returns default if key not found | `hil_signals.get("engine_temp", 0)`            |
| `keys()`                     | Returns a view of all keys                                    | `hil_signals.keys()`                           |
| `values()`                   | Returns a view of all values                                  | `hil_signals.values()`                         |
| `items()`                    | Returns a view of key-value pairs (tuples)                    | `hil_signals.items()`                          |
| `update(dict2)`              | Updates current dictionary with another                       | `hil_signals.update({"abs_status": "ACTIVE"})` |
| `pop(key[, default])`        | Removes key and returns its value                             | `hil_signals.pop("gear_position")`             |
| `popitem()`                  | Removes and returns the **last** inserted key-value pair      | `hil_signals.popitem()`                        |
| `clear()`                    | Removes all items from the dictionary                         | `hil_signals.clear()`                          |
| `copy()`                     | Returns a shallow copy of the dictionary                      | `backup = hil_signals.copy()`                  |
| `setdefault(key[, default])` | Returns key value, sets it if not present                     | `hil_signals.setdefault("engine_temp", 90)`    |

"""

hil_signals = {
    "speed_kph": 85,
    "rpm": 3000,
    "brake_pedal": 0.8,
    "fuel_level": 42.5
}


# Access signal safely
rpm = hil_signals.get("rpm", 0)

# Add new signal
hil_signals["engine_temp"] = 95.2

# Update multiple signals
hil_signals.update({
    "speed_kph": 90,
    "gear": "D"
})

# Check all signals
for name, value in hil_signals.items():
    print(f"{name} → {value}")

print(hil_signals.keys())
print(hil_signals.values())
