from common import operate_json

oper_j = operate_json.OperateJson()


def process_url(url):
    symbol_data = url.split('j::')
    data = symbol_data[0]

    for i in range(1, len(symbol_data)):
        key_value_pairs = symbol_data[i].split('&')

        key = key_value_pairs[0].split('=')[-1]  # 获取标识符后的键名
        value = oper_j.get_json_value(key)  # 获取对应键的值
        data += str(value)

        if len(key_value_pairs) > 1:
            data += '&' + '&'.join(key_value_pairs[1:])  # 保留剩余的参数部分

    return data


url = 'https://v1.2.tunnelprj.com/api/app/construction/log/statistics/time/consuming?tunnelId=j::tunnelId&taskId=j::taskId'
processed_url = process_url(url)
print(processed_url)
