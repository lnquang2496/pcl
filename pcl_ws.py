from copy import copy

g_ws = None
g_g_ws_merged_cells = None

class cell_info(object):
    __slots__=['column', 'row', 'value', 'bounds']
    def __init__(self, i_input, i_value=None):
        self.value = i_value
        if (len(i_input) == 2):
            self.column = i_input[0]
            self.row    = i_input[1]
            self.bounds = self.cell_get_boundary()
            del self.column
            del self.row
        elif (len(i_input) == 4):
            self.bounds = i_input
        else:
            # Error process, not implement yet
            pass

    def cell_get_boundary(self):
        global g_ws_merged_cells

        for loop_merged_cell in g_ws_merged_cells:
            if ((self.column >= loop_merged_cell[0]) and 
                (self.column <= loop_merged_cell[2])):
                if ((self.row >= loop_merged_cell[1]) and
                    (self.row <= loop_merged_cell[3])):
                    return loop_merged_cell
        return (self.column, self.row, self.column, self.row)

def ws_find(i_rows, i_target, i_match_case=False):
    for loop_rows in i_rows:
        for loop_cell in loop_rows:
            if (isinstance(i_target, str)):
                pass
            elif (isinstance(i_target, tuple)):
                pass

def g_ws_merged_cells_init(i_ws):
    global g_ws
    global g_ws_merged_cells

    g_ws = copy(i_ws)
    print(i_ws)
    print(g_ws)

    l_merged_cells_temp = []
    l_merged_cells = i_ws.merged_cell_ranges
    for loop_merged_cells in l_merged_cells:
        l_merged_cells_temp.append(loop_merged_cells.bounds)
    g_ws_merged_cells = tuple(l_merged_cells_temp)

def pcl_ws_init(ws):
    global g_ws_merged_cells

    g_ws_merged_cells_init(ws)
    l_temp = cell_info([2,2])
