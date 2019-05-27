import allure


class Test_002(object):
    def test_add_png(self):
        with open("./Snipaste_2019-03-26_19-23-59.png", "rb")as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)
