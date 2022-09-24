
import pytest, os
if __name__ == '__main__':
    pytest.main(['./test_case/','-k xijiao','-x'])
    # pytest.main(['./test_case/app_case/sina/test_add_article.py'])
    os.system('allure generate ./temp -o ./report --clean')

