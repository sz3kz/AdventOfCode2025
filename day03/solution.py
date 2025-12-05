#!/usr/bin/env python3
import argparse

#conditional_print(verbose, )
READ_ONLY = 'r'
TRAILING_NEWLINE = '\n'

def conditional_print(condition, *args, **kwargs):
    if condition:
        print(*args,**kwargs)

def find_max_battery_rindex(bank):
    # index from the right!
    max_joltage = 0
    max_index = None
    index = -1
    while (bank != 0):
        index += 1
        joltage = bank % 10
        bank //= 10
        if (joltage >= max_joltage):
            max_joltage = joltage
            max_index = index

    return max_index
    

def main(filename, count, verbose):
    suma = 0
    with open(filename, READ_ONLY) as file:
        for line in file:
            bank = line.strip(TRAILING_NEWLINE)
            conditional_print(verbose, f"Bank: \"{bank}\"")
            if (bank == ""):
                conditional_print(verbose, f"  Omitting.")
                continue
            bank = int(bank)
            header = len(str(bank))
            joltage = 0
            for trailing in range(count-1 , 0-1, -1):
                target_bank = (bank // (10 ** trailing)) * (10 ** trailing)                         # delete trailing
                target_bank = target_bank - (target_bank // (10 ** (header))) * (10 ** (header))    # delete header
                header = find_max_battery_rindex(target_bank) 
                joltage_digit = int(str(bank)[len(str(bank)) - header-1])
                joltage = joltage * 10 + joltage_digit
            conditional_print(verbose, f"  Joltage: {joltage}.")
            suma += joltage 
    print(f"Sum of maximal joltages: {suma}")



if __name__ == "__main__":

    argument_parser = argparse.ArgumentParser(description="Solve the challenge of day 3 of Advent Of Code.")

    argument_parser.add_argument(
        "filename",
        type = str,
        help = "Path to the file holding the challenge input.")
    argument_parser.add_argument(
        "count",
        type = int,
        help = "Amount of batteries to be turned on per bank.")
    argument_parser.add_argument(
        "--verbose",
        action = "store_true",
        help = "Print diagnostic messages.")

    arguments = argument_parser.parse_args()
    main(arguments.filename, arguments.count ,arguments.verbose)
