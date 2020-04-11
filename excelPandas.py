#!/usr/bin/python3
import pandas, numpy
from publicModule.errorWar_modu import errors_run_log
from publicModule.errorWar_modu import result_debug_type
from publicModule.errorWar_modu import print_debug_info
from traceback import print_exc
from xlwt import Workbook
from string import ascii_lowercase


def stringChars():
    v_chars = ""
    for itSer in ascii_lowercase:
        v_chars += itSer
        if len(v_chars)==3:
            v_chars=v_chars+"{},".format(v_chars)
    print(v_chars)


def workBook_sheet1Obj():
    try:
        v_book = Workbook(encoding='utf-8')
        v_sheet1 = v_book.add_sheet(u'Sheet2', cell_overwrite_ok=True)
        for itr in range(10):
            if itr < 3:
                v_sheet1.write(0, itr, '{}{}{}'.format(itr, itr, itr))
            else:
                v_sheet1.write(0, itr, '{}{}{}{}{}{}'.format(itr, itr, itr, itr, itr, itr))
            v_sheet1.write(1, itr, '{}{}{}{}{}{}'.format(itr, itr, itr, itr, itr, itr))
            v_sheet1.write(2, itr, '{}{}{}{}{}{}'.format(itr, itr, itr, itr, itr, itr))
            v_sheet1.write(3, itr, '{}{}{}{}{}{}'.format(itr, itr, itr, itr, itr, itr))
            v_sheet1.write(4, itr, '{}{}{}{}{}{}'.format(itr, itr, itr, itr, itr, itr))
            v_sheet1.write(5, itr, '{}{}{}{}{}{}'.format(itr, itr, itr, itr, itr, itr))
            # v_sheet1.write(2, itr, '{}{}{}{}{}{}'.format(itr, itr, itr, itr, itr, itr))
            # v_sheet1.write(itr, 0, 'erwerw')
            # v_sheet1.write(itr, 1, 'erwerw')
            # v_sheet1.write(itr, 2, 'erwerw')
        v_sheet2 = v_book.add_sheet(u'Sheet1', cell_overwrite_ok=True)
        v_str = ""
        # for itrs in range(5):

        v_book.save('workBook.xlsx')
    except:
        errors_run_log()
        print_exc()
        return result_debug_type()


def frameTo_excel():
    try:
        df1 = pandas.DataFrame(
            {
                'v1': numpy.random.rand(100),
                'v2': numpy.random.rand(100),
                'v3': numpy.random.rand(100)
            }
        )
        with pandas.ExcelWriter('../tempCache/path_to_fileTemp.xlsx') as tmp:
            df1.to_excel(tmp)
        df_tmp = pandas.DataFrame(
            [
                numpy.random.rand(10),
                numpy.random.rand(10),
                numpy.random.rand(10)
            ]
        )
        with pandas.ExcelWriter('../tempCache/path_to_fileTemp.xlsx') as wri_tmp:
            df_tmp.to_excel(wri_tmp)
        # v_df=pand
        # print(df_tmp)
    except:
        errors_run_log()
        return result_debug_type()


def main():
    stringChars()
    # workBook_sheet2Obj()
    # frameTo_excel()


if __name__ == '__main__':
    main()
