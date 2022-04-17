from csv import writer
from csv import reader


def drop_column(input_file, output_file, transform_row):
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


# Remove unnecessary columns
drop_column('input.csv', 'drop_column.csv', lambda row, line_num: row.remove(row[0]))
