import pytest, os

if __name__ == '__main__':
    pytest.main(
        ['./test_case/jnt_inter_case/', '-m jnt_app', '--maxfail=10', '--alluredir', './tmp'])
    os.system('allure generate ./tmp -o ./report -c')
