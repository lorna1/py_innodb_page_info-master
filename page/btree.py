import include
from include import *


class btree():
    def parseBtree(page):
        # 解析页头信息
        btree.parsePageHeader(page)
        # 解析record信息
        btree.parseInfimumAndSupreMumRecord(page)
        return

    def parsePageHeader(page):
        # 页 header
        page_headers = array_split(page, FIL_PAGE_DATA, FIL_PAGE_HEADER)
        # 0~2 页目录 page directory slot槽个数
        page_directory_solts = mach_read_convert_int(page_headers, 0, 2)
        # 2~4 堆中第一个记录的指针
        page_heap_top = mach_read_from_n(page_headers, 2, 2)
        # 4~6 堆中的记录个数
        page_record_num = mach_read_convert_int(page_headers, 4, 2)
        # 6~8 指向可重用记录指针
        page_free = mach_read_from_n(page_headers, 6, 2)
        # 8~10 已删除的记录的字节数（delete flag=1的记录大小总数）
        page_grabage = mach_read_convert_int(page_headers, 8, 2)
        # 10-12 最后插入记录的位置
        page_last_insert = mach_read_from_n(page_headers, 10, 2)
        # 12-14 最后插入记录的方向
        page_direction = mach_read_from_n(page_headers, 12, 2)
        # 14-16 一个方向连续插入记录的数量
        page_n_direction = mach_read_convert_int(page_headers, 14, 2)
        # 16-18 该页中记录的数量
        page_n_recs = mach_read_convert_int(page_headers, 16, 2)
        # 18-26 当前页最大事务ID
        page_max_trx_id = mach_read_from_n(page_headers, 18, 8)
        # 26~28 页level
        page_level = mach_read_convert_int(page_headers, 26, 2)
        # 28~36 索引ID
        page_index_id = mach_read_from_n(page_headers, 28, 8)
        # 36~46 b+树非叶节点所在段的segment header
        page_btr_seg_leaf = mach_read_from_n(page_headers, 46, 10)
        # 46~56 b+树，叶节点所在段的segment header
        page_btr_seg_top = mach_read_from_n(page_headers, 46, 10)

        print("     ==== PAGE HEADER ==== ")
        print("     [  0-2  ]页目录(稀疏索引) slots个数:<%s>" % page_directory_solts)
        print("     [  2-4  ]第一个记录的指针:<%s>" % (page_heap_top))
        print("     [  4-6  ]堆中的记录个数:<%s>" % (page_record_num))
        print("     [  6-8  ]指向可重用记录指针:<%s>" % (page_free))
        print("     [  8-10 ]已删除的记录的字节数:<%s>" % (page_grabage))
        print("     [ 10-12 ]最后插入记录的位置:<%s>" % (page_last_insert))
        print("     [ 12-14 ]最后插入记录的方向:<%s>" % (page_direction))
        print("     [ 14-16 ]一个方向连续插入记录的数量:<%s>" % (page_n_direction))
        print("     [ 16-18 ]该页中记录的数量:<%s>" % (page_n_recs))
        print("     [ 18-26 ]当前页最大事务ID:<%s>" % (page_max_trx_id))
        print("     [ 26-28 ]页level:<%s>" % (page_level))
        print("     [ 28-36 ]索引ID(当前页属于哪个索引):<%s>" % (page_index_id))
        print("     [ 36-46 ]b+树非叶节点所在段的segment header:<%s>" %
              (page_btr_seg_leaf))
        print("     [ 46-56 ]b+树，叶节点所在段的segment header:<%s>" %
              (page_btr_seg_top))
        return

    def parseInfimumAndSupreMumRecord(page):
        # 页 header
        user_records = array_split(
            page, FIL_PAGE_DATA + FIL_PAGE_HEADER, len(page))

        # 69 6e 66 69 6d 75 6d 00 = infimum
        page_infimum = array_split(user_records, 0, 13)
        # 73 75 70 72 65 6d 75 6d = supremum
        page_supremum = array_split(user_records, 0, 13)
        print("     ==== INF SUPRE ==== ")
        for c in range(page_infimum):
            b = bin(int(c, 16))[2:]
            print(b + " ")

        print("     [  0-13  ]:<%s>" % page_infimum)
        # print("     [  13-13  ]:<%s>" % page_supremum)
        return
