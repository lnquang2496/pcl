from copy import copy
from itertools import tee

g_ws = None
g_ws_rows = None
g_ws_merged_cells = None

class cell_info(object):
    __slots__=['column', 'row', 'value', 'bounds', 'match_case']
    def __init__(self, i_input=None, i_value=None, i_match_case=False):
        global g_ws

        if (i_value == None):
            if (len(i_input) == 2):
                self.column = i_input[0]
                self.row    = i_input[1]
                self.bounds = self.cell_get_boundary()
                del self.column
                del self.row
            elif (len(i_input) == 4):
                self.bounds = i_input

            self.value = g_ws.cell(self.bounds[1], self.bounds[0]).value

        else:
            self.value = i_value
            self.match_case = i_match_case
            self.bounds = self.cell_get_value()
            del self.match_case

    def cell_get_boundary(self):
        global g_ws_merged_cells

        # l_ws_merged_cells = copy(g_ws_merged_cells)
        g_ws_merged_cells, l_ws_merged_cells = tee(g_ws_merged_cells)
        for loop_merged_cell in l_ws_merged_cells:
            if ((self.column >= loop_merged_cell[0]) and 
                (self.column <= loop_merged_cell[2])):
                if ((self.row >= loop_merged_cell[1]) and
                    (self.row <= loop_merged_cell[3])):
                    return loop_merged_cell
        return (self.column, self.row, self.column, self.row)

    def cell_get_value(self):
        global g_ws_rows

        # l_ws_rows = copy(g_ws_rows)
        g_ws_rows, l_ws_rows = tee(g_ws_rows)
        for e_row, loop_rows in enumerate(l_ws_rows, start=1):
            for e_col, loop_cell in enumerate(loop_rows, start=1):
                if (loop_cell.value != None):
                    if ((loop_cell.value == self.value) if self.match_case else (loop_cell.value in self.value)):
                        self.column = e_col
                        self.row = e_row
                        l_bounds = self.cell_get_boundary()
                        del self.column
                        del self.row
                        return l_bounds

    def cell_shift_up(self):
        if ((self.bounds[1] - 1) > 0):
            global g_ws

            self.column = self.bounds[0]
            self.row = self.bounds[1] - 1
            self.bounds = self.cell_get_boundary()
            self.value = g_ws.cell(self.bounds[1], self.bounds[0]).value
            del self.column
            del self.row
        else:
            return

    def cell_shift_down(self):
        global g_ws

        self.column = self.bounds[0]
        self.row = self.bounds[3] + 1
        self.bounds = self.cell_get_boundary()
        self.value = g_ws.cell(self.bounds[1], self.bounds[0]).value
        del self.column
        del self.row

    def cell_shift_left(self):
        if ((self.bounds[0] - 1) > 0):
            global g_ws

            self.column = self.bounds[0] - 1
            self.row = self.bounds[1]
            self.bounds = self.cell_get_boundary()
            self.value = g_ws.cell(self.bounds[1], self.bounds[0]).value
            del self.column
            del self.row
        else:
            return

    def cell_shift_right(self):
        global g_ws

        self.column = self.bounds[2] + 1
        self.row = self.bounds[1]
        self.bounds = self.cell_get_boundary()
        self.value = g_ws.cell(self.bounds[1], self.bounds[0]).value
        del self.column
        del self.row

def g_ws_merged_cells_init(i_ws):
    l_merged_cells_temp = []
    l_merged_cells = i_ws.merged_cell_ranges
    for loop_merged_cells in l_merged_cells:
        l_merged_cells_temp.append(loop_merged_cells.bounds)
    return iter(l_merged_cells_temp)

def pcl_ws_init(ws):
    global g_ws
    global g_ws_rows
    global g_ws_merged_cells

    g_ws = ws
    g_ws_rows = ws.rows
    g_ws_merged_cells = g_ws_merged_cells_init(ws)

    l_temp = cell_info(i_value='Input element')
    print(l_temp.bounds, l_temp.value)
