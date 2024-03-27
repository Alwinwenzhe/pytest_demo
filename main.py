import pytest, os

if __name__ == '__main__':
    pytest.main(
        ['-m chat', '--alluredir', './tmp'])
    os.system('allure generate ./tmp -o ./report -c')
