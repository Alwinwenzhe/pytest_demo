import pytest

brand = ['hauwei','realme','oppo']
memory = ['4g','8g','12g']
story = ['128g','256g']

@pytest.mark.parametrize('brand',brand)
@pytest.mark.parametrize('memory',memory)
@pytest.mark.parametrize('story',story)
def test_print_info(brand,memory,story):
    print('组合打印所有信息：')
    print(brand,' ',memory,' ',story)

if __name__ == '__main__':
    pytest.main()       # 这样就会将所有的手机信息组合18种，都打印出来