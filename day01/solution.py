#!/usr/bin/env python3
import argparse

def main(filename, count_intermediate):
    current_position = 50
    max_position = 99
    zeroes_encountered = 0
    with open(filename, "r") as file:
        for line in file:
            command = line.strip("\n")
            if (command == ""):
                print("Ommiting empty line.")
                continue
            dial_direction = 1 if command[0] == 'R' else -1
            dial_number = int(command[1:])
            old_position = current_position
            new_position = current_position + dial_direction * dial_number
            if (count_intermediate):
                if (new_position * old_position < 0):
                    zeroes_encountered += 1
                if (new_position > max_position):
                    zeroes_encountered += new_position // (max_position + 1)
                elif (new_position < 0):
                    zeroes_encountered += (-new_position) // (max_position + 1)
            if (new_position == 0):
                zeroes_encountered += 1
            new_position = new_position % (max_position+1)
            current_position = new_position
            print(f"{command}:{dial_direction} {dial_number}: {old_position} -> {new_position}")
    print(f"Zeroes encountered: {zeroes_encountered}")


if __name__ == "__main__":

    argument_parser = argparse.ArgumentParser(description="Solve problem.")

    argument_parser.add_argument(
        "filename",
        type = str,
        help = "Path to the file holding the challenge input.")

    argument_parser.add_argument(
        "--count_intermediate",
        help="Switch on counting not only ending zeroes, but intermediate zeroes.",
        action="store_true")

    arguments = argument_parser.parse_args()
    main(arguments.filename, arguments.count_intermediate)
