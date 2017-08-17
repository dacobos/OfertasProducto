################################  MODULE  INFO  ################################
# Author: David  Cobos
# Cisco Systems Solutions Integrations Architect
# Mail: cdcobos1999@gmail.com  / dacobos@cisco.com
################################  MODULE  INFO  ################################

# Read a xls file and return a dictionary with all the values

# from openpyxl import Workbook
# from openpyxl import load_workbook

import xlrd


def readxls(filename):
    book = xlrd.open_workbook(filename)
    # get the first worksheet
    xl_sheet = book.sheet_by_index(0)
    num_rows = xl_sheet.nrows
    data = []
    for i in range(0, num_rows):
        data.append(xl_sheet.row_values(i))
    return data
