import pcl_load_workbook
import pcl_worksheet_handler
from memory_profiler import memory_usage
from time import time

def main():
    t1 = time()
    m1 = memory_usage()
    # Load workbook and Load worksheet
    pcl_load_workbook.pcl_load_workbook('test.xlsx')
    ws = pcl_load_workbook.pcl_get_worksheet('Sheet1')
    # Analyze the worksheet
    pcl_worksheet_handler.pcl_worksheet_init(ws)

    pcl_load_workbook.pcl_free_workbook()
    t2 = time()
    m2 = memory_usage()
    print((t2 - t1)*1000, 'ms, ', (m2[0] - m1[0]), 'Mb')

if __name__ == '__main__':
    main()
