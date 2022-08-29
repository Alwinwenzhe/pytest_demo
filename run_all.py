
import pytest, os
if __name__ == '__main__':
    pytest.main(['./test_case/','-m xijiao','-x'])
    os.system('allure generate ./temp -o ./report --clean')

