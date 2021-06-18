# _*_ coding:utf-8 _*_
# @Time:2020/12/2 16:53
# @Author:Cadman
# @File auto_print.py

import win32com
import win32api
import win32print
import win32com.client


class AutoPrint:
    GHOSTSCRIPT_PATH = r"D:\Python\python3.7\Framework\FastAPI\atools\apps\lib\GHOSTSCRIPT\bin\gswin32.exe"
    GSPRINT_PATH = r"D:\Python\python3.7\Framework\FastAPI\atools\apps\lib\GSPRINT\gsprint.exe"

    def __init__(self):
        self.__printer = win32print.GetDefaultPrinter()

    def print_usual(self, filename):
        """
        打印常规文件,例如txt,word 文档文本类型
        :return:
        """
        open(filename, "r")
        win32api.ShellExecute(
            0,
            "print",
            filename,
            '/d:"%s"' % self.__printer,
            ".",
            0
        )

    def print_pdf(self, filename):
        '''
        根据默认打印机打印pdf文件
        :return:
        '''
        self.__command = f'''-ghostscript "{self.GHOSTSCRIPT_PATH}" -printer "{self.__printer}" "{filename}" '''

        # self.a = '-ghostscript \
        #             "' + self.GHOSTSCRIPT_PATH + '" \
        #                     -printer \
        #                     "' + self.__printer + '" \
        #                     "' + filename + '" '

        win32api.ShellExecute(
            0,
            'open',
            self.GSPRINT_PATH,
            self.__command,
            '.',
            0
        )

    def print_execl(self, execl_file_path):
        """
        打印execl 文件
        :param execl_file_path:
        :return:
        """
        xlApp = win32com.client.Dispatch('Excel.Application')  # 打开 EXCEL
        xlApp.Visible = 0  # 不在后台运行
        xlApp.EnableEvents = False
        xlApp.DisplayAlerts = False  # 显示弹窗
        xlBook = xlApp.Workbooks.Open(execl_file_path)
        xlApp.ActiveWorkbook.Sheets(1).PageSetup.Zoom = False
        xlApp.ActiveWorkbook.Sheets(1).PageSetup.FitToPagesWide = 1
        xlApp.ActiveWorkbook.Sheets(1).PageSetup.FitToPagesTall = 1  # 保存
        ename = xlApp.ActiveWorkbook.name  # 获取打开工作表名称

        xlBook.PrintOut()  # 打印页数1到1
        xlApp.quit()  # 退出


'''
# [自动打印文件]
# 分别对word,execl,pdf文档进行测试打印!
path = "C:\\Users\\Administrator\\esktop\\tmp\\我说的是多.docx"
path2 = "C:\\Users\\Administrator\\Desktop\\drive_long.xlsx"
path3 = "C:\\Users\\Administrator\\Desktop\\tmp\\通过串口外部控制NION实例介绍.pdf"

ap = AutoPrint()
ap.print_usual(path)
ap.print_execl(path2)
ap.print_pdf(path3)
'''
