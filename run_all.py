
import pytest, os

if __name__ == '__main__':
    pytest.main(['./test_case/','-m xijiao'])
    os.system('allure generate ./temp -o ./report --clean')

