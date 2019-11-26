#!/usr/bin/env python

import csv
import sys


def create_csv_reader(file):
    fieldnames = ["transaction_date", "settlement_date", "sender", "receiver", "details", "amount", "ccy",
                  "amount_regional", "ccy_regional", "sender_account_number", "receiver_account_number"]
    return csv.DictReader(file, fieldnames=fieldnames, delimiter=";")


def create_csv_writer(file):
    fieldnames = ["date", "payment", "info", "payee", "memo", "amount", "category", "tags"]
    return csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")


def main():
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    with open(input_file_name, mode="r", encoding="windows-1250") as input_csv_file, \
            open(output_file_name, mode="w", encoding="UTF-8") as output_csv_file:
        csv_reader = create_csv_reader(input_csv_file)
        csv_writer = create_csv_writer(output_csv_file)

        next(csv_reader, None)
        next(csv_reader, None)
        csv_writer.writeheader()
        for row in csv_reader:
            csv_writer.writerow({
                "date": row["transaction_date"],
                "info": row["details"],
                "amount": row["amount_regional"]
            })


if __name__ == '__main__':
    main()