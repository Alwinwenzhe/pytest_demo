import pytest, os

if __name__ == '__main__':
    pytest.main(['./test_case/jnt_inter_case/','-m jnt_app','-x','--alluredir','./tmp'])
    os.system('allure generate ./tmp -o ./report --clean')