from threading import Thread
# Define number of Thread
NUMOFTHREAD = 4

# Global hold worksheet information
g_ws_rows         = None
g_ws_merged_cells = None
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

# Thread function
def ws_thread_seek(i_ws_rows, i_string, i_index, i_matchcase=False):
    global g_thread_return

    for loop_rows in i_ws_rows:
        for loop_cell in loop_rows:
            if ((loop_cell.value == i_string) if i_matchcase else (loop_cell.value in i_string)):
                g_thread_return[i_index] = loop_cell.coordinate
                return

def pcl_worksheet_init(ws):
    global g_ws_rows
    global g_ws_merged_cells
    global g_target
    global g_thread_return

    g_ws_merged_cells = ws.merged_cells

    l_thread = [None] * NUMOFTHREAD
    for loop_i in range(NUMOFTHREAD):
        print(loop_i)
        l_thread[loop_i] = Thread(target=ws_thread_seek, args=(ws.rows, g_target[loop_i], loop_i, True))
        l_thread[loop_i].start()

    for loop_i in range(NUMOFTHREAD):
        l_thread[loop_i].join()

    print(g_thread_return)

    
