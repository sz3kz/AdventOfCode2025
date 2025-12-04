#!/usr/bin/env python3
import argparse

RANGE_SEPARATOR = "-"
READ_ONLY = "r"
RANGES_SEPARATOR = ","
TRAILING_NEWLINE = "\n"
RANGE_EMPTY = ""
INCLUDE_LAST_ID = 1

def calculate_divisors(number):
    divisors = []
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors

def conditional_print(condition, *args, **kwargs):
    if condition:
        print(*args,**kwargs)

def main(filename, multiple, verbose):
    sum = 0
    with open(filename, READ_ONLY) as file:
        ranges = file.read()                        # blob of ranges
        ranges = ranges.strip(TRAILING_NEWLINE)     # delete potential (does not need to be there) newline
        ranges = ranges.split(RANGES_SEPARATOR)     # create list of individual ranges of "<min>-<max>" format
        for current_range in ranges:
            conditional_print(verbose, f"------------\nCurrent range: \"{current_range}\"")
            if (current_range == RANGE_EMPTY):
                conditional_print(verbose,f"Range: \"{current_range}\" is empty, ommiting.")
                continue
            first_id, last_id = current_range.split(RANGE_SEPARATOR)
            first_id = int(first_id)
            last_id = int(last_id)
            conditional_print(verbose, f"First ID: {first_id}")
            conditional_print(verbose, f"Last ID: {last_id}")
            for product_id in range(first_id, last_id + INCLUDE_LAST_ID):
                conditional_print(verbose,f"  Product_ID: {product_id}")
                if multiple:
                    sequence_lengths = calculate_divisors(len(str(product_id)))
                    sequence_lengths.pop()
                else:
                    if (len(str(product_id)) % 2 == 0):
                        sequence_lengths = [len(str(product_id)) // 2]
                    else:
                        conditional_print(verbose, f"    Can't repeat twice({len(str(product_id))} % 2 != 0).")
                        continue
                conditional_print(verbose, f"  Potential repeating sequence lengths: {sequence_lengths}")
                for sequence_length in sequence_lengths:
                    sequence_mask = 10 ** sequence_length
                    sequence = product_id % sequence_mask
                    temporary_product_id = product_id // sequence_mask
                    repeating = True
                    conditional_print(verbose, f"    Sequence length: {sequence_length}")
                    conditional_print(verbose, f"      Sequence Mask: {sequence_mask}")
                    conditional_print(verbose, f"      Sequence: {sequence}")
                    while (temporary_product_id != 0):
                        temporary_sequence = temporary_product_id % sequence_mask
                        temporary_product_id //= sequence_mask
                        conditional_print(verbose, f"      Temporary product id: {temporary_product_id}")
                        conditional_print(verbose, f"      Temporary sequence: {temporary_sequence}")
                        conditional_print(verbose, f"      ? {temporary_sequence} != {sequence}:")
                        if (temporary_sequence != sequence):
                            repeating = False
                            break
                    if repeating:
                        conditional_print(verbose, f"      Product ID: {product_id} deemed INVALID")
                        sum += product_id
                        break
    print(f"Sum of invalid product ID's: {sum}")



if __name__ == "__main__":

    argument_parser = argparse.ArgumentParser(description="Solve the challenge of day 2 of Advent Of Code.")

    argument_parser.add_argument(
        "filename",
        type = str,
        help = "Path to the file holding the challenge input.")
    argument_parser.add_argument(
        "--multiple",
        action = "store_true",
        help = "Check if product ID is a multiple-repeating sequence, twice or more")
    argument_parser.add_argument(
        "--verbose",
        action = "store_true",
        help = "Print diagnostic messages.")

    arguments = argument_parser.parse_args()
    main(arguments.filename, arguments.multiple, arguments.verbose)
