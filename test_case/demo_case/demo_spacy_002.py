import spacy
from spacy.matcher import Matcher

nlp = spacy.load("zh_core_web_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "升级iPhone X之后，我们并没有发现系统设计有很大的不同，远没有当年iOS 7发布时带来的"
    "焕然一新的感觉。大部分iOS 11的设计与iOS 10保持一致。但我们仔细试用后也发现了一些"
    "小的改进。"
)

# 写一个模板(两个属性)来匹配完整的iOS版本 ("iOS 7", "iOS 11", "iOS 10")
# 注意这里是匹配的两个
pattern1 = [{"TEXT": "iOS"}, {"IS_DIGIT": True}]
pattern2 = [{"LOWER": "iphone"}, {"LOWER": "x"}]

# 输出分词索引、文本、词性
for token in doc:
    print(token.i,token.text,token.pos_)

# 把模板加入到matcher中，将matcher应用到doc上面
matcher.add("IOS_VERSION_PATTERN", [pattern1,pattern2])
matches = matcher(doc)
print("Total matches found:", len(matches))

# 遍历所有的匹配，然后打印span的文本
for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)