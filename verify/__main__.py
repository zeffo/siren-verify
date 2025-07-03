import sys
from openpyxl import load_workbook
from openpyxl.utils.exceptions import InvalidFileException

workbook = load_workbook(sys.argv[1])
sheets = workbook.worksheets

primary = sheets[0]
secondary = sheets[1]


for row_p, row_s in zip(primary.rows, secondary.rows):
    for cell_p, cell_s in zip(row_p, row_s):
        if cell_p.value != cell_s.value:
            print(f"{cell_p.coordinate}: {cell_p.value} | {cell_s.value}")
