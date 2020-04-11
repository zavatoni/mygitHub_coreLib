#!/usr/bin/python3
from pandas import ExcelWriter
from pandas import DataFrame
from numpy import random
from publicModule.errorWar_modu import errors_run_log
from publicModule.errorWar_modu import result_debug_type
import unittest
from os import listdir

df_pub = DataFrame(
    {
        'v1': random.rand(100),
        'v2': random.rand(100),
        'v3': random.rand(100)
    }
)


def date_lst_range(str_date):
    try:
        from pandas import date_range
        lst_date = []
        v_dates = date_range(str_date, periods=6)
        for v_itrs in v_dates:
            lst_itrs = str(v_itrs).split(' ')
            lst_date.append(lst_itrs[0])
        return lst_date
    except:
        return result_debug_type(), errors_run_log()


def xlrd_sheetNumber_count(v_file):
    try:
        import xlrd
        lst_xlrd = []
        with xlrd.open_workbook(v_file) as tCase:
            count = len(tCase.sheets())
            for v_sheet in tCase.sheets():
                lst_xlrd.append(v_sheet.name)
            return count, lst_xlrd
    except:
        return errors_run_log(),result_debug_type()


# from pandas import read_excel
class TestExcelWriter_case(unittest.TestCase):
    def test_excelWriter_base(self):
        try:
            with ExcelWriter('tempCase_table.xlsx') as tc:
                df_pub.to_excel(tc)
            lst_direct = listdir('./')
            if len(lst_direct) > 2:
                for itr_xlsx in lst_direct:
                    if itr_xlsx.endswith('xlsx'):
                        self.assertIn('tempCase_table.xlsx', itr_xlsx)
                        with open('ExcelWriter_result.log', 'a') as ew:
                            ew.write('\ntest_excelWriter_base\n:{}'.format(df_pub))
        except:
            return errors_run_log(),result_debug_type()

    def test_excel_writer_sheetName(self):
        '''
        with ExcelWriter('path_to_file.xlsx') as writer:
            df1.to_excel(writer, sheet_name='Sheet1')
            df2.to_excel(writer, sheet_name='Sheet2')
        :return:
        '''
        try:
            with ExcelWriter('testXlsx_sheet.xlsx') as txs:
                df_pub.to_excel(txs, sheet_name='dFrame_demo')
                df_pub.to_excel(txs, sheet_name='dFrame_exam')
            vCount, lst_sheet = xlrd_sheetNumber_count(v_file='testXlsx_sheet.xlsx')
            if len(lst_sheet) == 2:
                self.assertEqual(vCount, 2)
                for itr_str in lst_sheet:
                    self.assertIn('dFrame', itr_str)
                with open('ExcelWriter_result.log', 'a') as ewr:
                    ewr.write('\ntest_excel_writer_sheetName:{}\n'.format(lst_sheet))
                    ewr.write('test_excel_writer_sheetName:lenght==>{}\n'.format(vCount))
        except:
            errors_run_log()
            return result_debug_type()

    def test_excel_writer_date(self):
        '''
        with ExcelWriter('path_to_file.xlsx',
                      date_format='YYYY-MM-DD',
                      datetime_format='YYYY-MM-DD HH:MM:SS') as writer:
            df.to_excel(writer)
        '''
        try:
            with ExcelWriter(
                    path='test_excel_dates.xlsx',
                    date_format='YYYY-MM-DD',
                    datetime_format='YYYY-MM-DD HH:MM:SS'
            ) as we:
                df_pub.to_excel(we)
            lst_directs = listdir('./')
            for index in lst_directs:
                if index.startswith('test_excel') and index.endswith('xlsx'):
                    print(index)
        except:
            return errors_run_log(), result_debug_type()

    def test_excel_writerMode_a(self):
        '''
        with ExcelWriter('path_to_file.xlsx', mode='a') as writer:
            df.to_excel(writer, sheet_name='Sheet3')
        :return:
        '''
        try:
            with ExcelWriter('testXlsx_sheet.xlsx', mode='a') as ted:
                df_pub.to_excel(ted, sheet_name='Sheet3')
            vCount, lst_sheets = xlrd_sheetNumber_count(v_file='testXlsx_sheet.xlsx')
            if vCount == len(lst_sheets):
                self.assertEqual(vCount, len(lst_sheets))
                with open('test_excel_writerMode_a.log', 'a') as inp_tew:
                    inp_tew.write('test_excel_writerMode_a:vCount==>{}\n'.format(vCount))
                    inp_tew.write('test_excel_writerMode_a:lst_sheets==>{}\n'.format(lst_sheets))
        except:
            return result_debug_type(), errors_run_log()

    def test_series_basic(self):
        try:
            # Creating a Series by passing a list of values, letting pandas create a default integer index:
            from pandas import Series
            import numpy as np
            s = Series([1, 3, 5, np.nan, 6, 8])
            for itrs in s:
                if 'float' in str(type(itrs)):
                    self.assertIn('float', str(type(itrs)))
                    with open('test_series_basic.log', 'a') as tsBasic:
                        tsBasic.write('test_series_basic:Type==>{}\n'.format(type(itrs)))
        except:
            return result_debug_type(), errors_run_log()

    def test_date_range_basic(self):
        '''
        Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:
        :return:该测试用例可以作为配套的应用函数
        '''
        try:
            from pandas import date_range
            v_dates = date_range('20200505', periods=6)
            lst_date = []
            for v_itr in v_dates:
                lst_itrs = str(v_itr).split(' ')
                self.assertEqual(len(lst_itrs), 2)
                lst_date.append(lst_itrs[0])
            self.assertEqual(len(lst_date), 6)
            with open('pandas_date_range.log', 'a') as pdr:
                pdr.write('test_date_range_basic:lst_date==>{}\n'.format(lst_date))
        except:
            return result_debug_type(), errors_run_log()

    def test_dateRange_dataFrame_group(self):
        '''
        Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:
        :return:
        '''
        try:
            from pandas import DataFrame
            from numpy import random
            v_dates = date_lst_range(str_date='20130101')
            df_rand = DataFrame(random.randn(6, 4), index=v_dates, columns=list('ABCD'))
            with open('dateRange_dataFrame_group.log', 'a') as var_dr:
                var_dr.write('test_dateRange_dataFrame_group:df_rand==>\n{}\n'.format(df_rand))
        except:
            return result_debug_type(), errors_run_log()


if __name__ == '__main__':
    unittest.main()
