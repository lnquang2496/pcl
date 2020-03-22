import pcl_load_workbook
from memory_profiler import memory_usage
from time import time

def main():
    t1 = time()
    m1 = memory_usage()
    pcl_load_workbook.pcl_load_workbook('test.xlsx')
    ws = pcl_load_workbook.pcl_get_worksheet('Sheet1')
    pcl_load_workbook.pcl_free_workbook()
    t2 = time()
    m2 = memory_usage()
    print(t2 - t1, m2[0] - m1[0])

if __name__ == '__main__':
    main()
