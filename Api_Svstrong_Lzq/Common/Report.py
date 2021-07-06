import unittest
from BeautifulReport import BeautifulReport


class Report:
    def report(self):
        # 收集用例
        cases_dir = '/Users/vita/Desktop/svs/Api_Svstrong_Lzq/Case'
        reports_dir = '/Users/vita/Desktop/svs/Api_Svstrong_Lzq/Report'
        case = unittest.defaultTestLoader.discover(cases_dir, pattern='Test*.py')

        # 生成报告
        br = BeautifulReport(case)
        br.report("互动课堂Api自动化", "互动课堂_api.html", reports_dir)
if __name__ == '__main__':
    Report.report('')