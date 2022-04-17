import csv
import re
import numpy as np
import datatable as dt

def parse_number(string):
  try:
    try:
      n = float(string)
    except:
      numlike = re.findall(r'\d+', string)
      n = float(numlike[0])
    finally:
      return n
  except:
    return None

def load_data(file_name):
    """
    This function will load file return as numpy array for numerical values.
    """
    # arr = []
    # with open(file_name, mode="r") as f:
    #     lines = csv.reader(f)
    #     for l in lines:
    #         lst = l[0].split()

    #         lst = [parse_number(el) for el in lst]
    #         arr.append(lst)

    # arr = np.array(arr, dtype=np.float32)

    DT = dt.fread(file_name, fill = True, skip_blank_lines = True)
    return DT

