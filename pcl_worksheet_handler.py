from threading import Thread
# Define number of Thread
NUMOFTHREAD = 4

# Global hold search worksheet Item
# Length of Target must be equal with NUMOFTHREAD
g_target = [
    '#'              , # Seek for NumOfTestCase
    'Input element'  , # Seek for Input
    'Output element' , # Seek for Output
    'Judgment'         # Seek for Optional
]
# Gloabl hold the return value of Thread
g_thread_return = [None] * NUMOFTHREAD
g_test_case_id = []

# Thread function
def ws_thread_seek(i_ws_rows, i_ws_merged_cell, i_target, i_index, i_matchcase=False):
    global g_thread_return

    if (i_target)
    for loop_rows in i_ws_rows:
        for loop_cell in loop_rows:
            if ((loop_cell.value == i_target) if i_matchcase else (loop_cell.value in i_target)):
                print(i_target, loop_cell.coordinate)
                for each_merged_cells in i_ws_merged_cell:
                    if (loop_cell.coordinate in each_merged_cells):
                        g_thread_return[i_index] = each_merged_cells.bounds
                        return
                g_thread_return[i_index] = (loop_cell.column, loop_cell.row, loop_cell.column, loop_cell.row)

def pcl_shift_left(i_ws_rows):
    pass

def pcl_worksheet_init(ws):
    global g_target
    global g_thread_return

    l_thread = [None] * NUMOFTHREAD
    for loop_i in range(NUMOFTHREAD):
        l_thread[loop_i] = Thread(target=ws_thread_seek, args=(ws.rows, ws.merged_cells, g_target[loop_i], loop_i, True))
        l_thread[loop_i].start()

    for loop_i in range(NUMOFTHREAD):
        l_thread[loop_i].join()

    print(g_thread_return)


