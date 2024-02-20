import pytest, os
if __name__ == '__main__':

    # pytest.main(['./test_case/app_case/sina/test_add_article.py'])
    pytest.main(['./test_case/jnt_inter_case/','-m jnt_app','-x',"--alluredir=temp"])
    os.system('allure generate ./temp -o ./report --clean')


