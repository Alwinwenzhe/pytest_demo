import pytest, os

if __name__ == '__main__':
    pytest.main(['./test_case/jnt_inter_case/','-m debug','-x','--alluredir','./tmp'])
    os.system('allure generate ./tmp -o ./report -c')