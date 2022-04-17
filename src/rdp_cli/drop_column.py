from csv import writer
from csv import reader
import click

@click.command()
@click.option("--output_file", required = True)
@click.argument("input_file")
@click.option("--col")
def drop_column(input_file, output_file, col):
    transform_row = lambda row, line_num: row.remove(row[int(col)])
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        csv_reader = reader(read_obj)
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)
