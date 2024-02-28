import spacy
from spacy.language import Language

# 定义定制化组件
@Language.component("length_component")
def length_component_function(doc):
    # 获取doc的长度
    doc_length = ____
    print(f"This document is {doc_length} tokens long.")
    # 返回这个doc
    ____


# 读取小规模的中文流程
nlp = spacy.load("zh_core_web_sm")

# 将组件加入到流程的最前面，打印流程组件名
____.____(____, ____=____)
print(nlp.pipe_names)

# 处理一段文本
doc = ____
