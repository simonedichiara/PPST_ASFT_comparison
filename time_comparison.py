from datetime import datetime
import sys

##adding a comment to test
## second test comment

def parse_file(filename):
    data = {}

    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()

            # Ensure correct number of columns
            if len(parts) != 15:
                continue

            # Column 7 must be "DragPointing"
            if parts[6] != "DragPointing":
                continue

            try:
                # Combine date + time
                start_time = datetime.strptime(parts[0] + " " + parts[1], "%Y-%m-%d %H:%M:%S")
                end_time = datetime.strptime(parts[2] + " " + parts[3], "%Y-%m-%d %H:%M:%S")

                # Drag pointing ID (column 8)
                drag_id = parts[7]

                data[drag_id] = {
                    "start": start_time,
                    "end": end_time
                }

            except Exception as e:
                print(f"Skipping line due to error: {e}")
                continue

    return data


def compute_differences(file1_data, file2_data):
    RED = "\033[91m"
    RESET = "\033[0m"
    for drag_id in file1_data:
        if drag_id in file2_data:
            start_diff = int((file2_data[drag_id]["start"] - file1_data[drag_id]["start"]).total_seconds())
            end_diff = int((file2_data[drag_id]["end"] - file1_data[drag_id]["end"]).total_seconds())

            print(f"DragPointing ID: {drag_id}")
            # RED if difference is greather than 30 s
            if abs(start_diff) > 30:
                print(f"{RED}  Start time difference: {start_diff}{RESET}")
            else:
                print(f"  Start time difference: {start_diff}")

            if abs(end_diff) > 30:
                print(f"{RED}  End time difference:   {end_diff}{RESET}")
            else:
                print(f"  End time difference:   {end_diff}")

#            print(f"  Start time difference: {start_diff}")
#            print(f"  End time difference:   {end_diff}")
            print("-" * 40)


import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 time_comparison.py  <PPST file> <ASFT file>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    data1 = parse_file(file1)
    data2 = parse_file(file2)

    compute_differences(data1, data2)

#def main():
#    file1 = "march17ppst.txt"
#    file2 = "march17asft.txt"
#
#    data1 = parse_file(file1)
#    data2 = parse_file(file2)
#
#    compute_differences(data1, data2)


if __name__ == "__main__":
    main()
