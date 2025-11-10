"""
| Command        | Action                                                   |
| -------------- | -------------------------------------------------------- |
| `n`            | **Next** — execute next line (stays in current function) |
| `s`            | **Step into** — enter a called function                  |
| `c`            | **Continue** — run until next breakpoint                 |
| `l`            | **List** current lines of code                           |
| `p variable`   | **Print** a variable’s value                             |
| `! expression` | Run a Python expression                                  |
| `q`            | **Quit** the debugger                                    |

"""

# debug_demo_pdb.py

import pdb  # Python debugger

def calculate_average(numbers):
    pdb.set_trace()  # Debugger stops here
    total = 0
    for num in numbers:
        total += num
    avg = total / len(numbers)
    return avg


def find_max(numbers):
    max_num = 0
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num


def main():
    data = [5, 10, 15, -2, 8]

    print("Calculating average...")
    average = calculate_average(data)
    print("Average:", average)

    print("\nFinding maximum value...")
    pdb.set_trace()  # Stop here before calling find_max
    maximum = find_max(data)
    print("Maximum:", maximum)

    print("\nCalculating average of an empty list (intentional bug!)")
    empty_data = []
    average_empty = calculate_average(empty_data)
    print("Average of empty list:", average_empty)


if __name__ == "__main__":
    main()
