#coding:utf-8
import unittest
from Common import HTMLTestRunner


def all_case():
    case_dir="C:\\Users\\yangsha\\PycharmProjects\\ystestselenium\\Case"

    testcase=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(case_dir,
                                             pattern="test*.py",
                                             top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testcase.addTests(test_case)
    print(testcase)
    return testcase

if __name__=="__main__":
    runner=unittest.TextTestRunner()

    fq=open("C:\Users\Administrator\PycharmProjects\test\EnventXtra\Report"+"result.html","wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fq,
                                         title="Envent自动化测试报告",
                                         description="用例执行情况")
    runner.run(all_case())
    fq.close()
