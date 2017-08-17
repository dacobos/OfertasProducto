################################  MODULE  INFO  ################################
# Author: David  Cobos
# Cisco Systems Solutions Integrations Architect
# Mail: cdcobos1999@gmail.com  / dacobos@cisco.com
################################  MODULE  INFO  ################################

# Write a xlsx file with the values passed in a dictionary

from openpyxl import Workbook
from openpyxl.styles import Font

def writexlsx(bom, filename):
    newfilename = filename.split('.')[0]+'_codigos_sap.xlsx'
    wb = Workbook()
    ws = wb.active
    for i in range(len(bom)):
        ws.append(bom[i])


    red_font = Font(color='00FF0000', italic=True)
    for cell in ws["2:2"]:
        cell.font = red_font
    wb.save(newfilename)
    return newfilename
