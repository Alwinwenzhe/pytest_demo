import pytest, os

if __name__ == '__main__':
    pytest.main(['./test_case/jnt_inter_case/','-m jnt_app','-x',"--clean-alluredir"])
    os.system('allure generate ./temp -o ./report')



