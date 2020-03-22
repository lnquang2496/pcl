from openpyxl import load_workbook

wb = 0

def pcl_load_workbook(filename:str):
    global wb
    wb = load_workbook(
        filename=filename,
        read_only=False,
        keep_vba=False,
        keep_links=False)

def pcl_free_workbook():
    global wb
    del wb

def pcl_get_worksheet(worksheetname):
    global wb
    return wb[worksheetname]
