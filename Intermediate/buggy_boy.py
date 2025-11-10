# debug_demo.py

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    avg = total / len(numbers)
    return avg


def find_max(numbers):
    max_num = 0
    max_num = numbers[0]
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
    maximum = find_max(data)
    print("Maximum:", maximum)

    print("\nCalculating average of an empty list (intentional bug!)")
    empty_data = []
    average_empty = calculate_average(empty_data)
    print("Average of empty list:", average_empty)


if __name__ == "__main__":
    main()
