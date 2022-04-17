from csv import writer
from csv import reader
import re
import click

@click.command()
@click.option("--output_file", required = True)
@click.argument("input_file")
def remove_special_chars(input_file, output_file):
    transform_row = lambda row, line_num: row.append(re.sub('[^A-Za-z0-9]+', '', row[4]))
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        csv_reader = reader(read_obj)
        csv_writer = writer(write_obj)
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)


# Add a column to csv file by duplicating column x but without special chars
# remove_special_chars('input.csv', 'remove_special.csv', lambda row, line_num: row.append(re.sub('[^A-Za-z0-9]+', '', row[4])))
