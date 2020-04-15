class cell_info(object):
    __slots__=['column', 'row', 'value']
    def __init__(i_column, i_row, i_value, i_):
        self.column = i_column
        self.row = i_row
        self.value = value

ws_row = None
ws_merged_cells = None

def ws_find(i_rows, i_target, i_match_case=False):
    for loop_rows in i_rows:
        for loop_cell in loop_rows:
        if (isinstance(i_ws, str)):
            if ()
        elif (isinstance(i_ws, tuple)):
            pass

def ws_merged_cells_init(i_ws):
    global ws_merged_cells

    l_merged_cells_temp = []
    l_merged_cells = i_ws.merged_cell_ranges
    for loop_merged_cells in l_merged_cells:
        l_merged_cells_temp.append(loop_merged_cells.bounds)
    ws_merged_cells = tuple(l_merged_cells_temp)

def pcl_ws_init(ws):
    global ws_merged_cells

    ws_merged_cells_init(ws)
    print(ws_merged_cells)
