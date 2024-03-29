import json
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span, DocBin

with open(r"../../exercises/zh/iphone.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

nlp = spacy.load("zh_core_web_sm")
# # 修改成空白中文库后，matcheer匹配不上
# nlp = spacy.blank("zh")
matcher = Matcher(nlp.vocab)
# 将pattern加入mattcher中
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]
matcher.add("GADGET", [pattern1, pattern2])
docs = []
for doc in nlp.pipe(TEXTS):
    matches = matcher(doc)
    spans = [Span(doc, start, end, label=match_id) for match_id, start, end in matches]
    print(spans)
    doc.ents = spans
    docs.append(doc)

doc_bin = DocBin(docs=docs)
# 将DocBin存储到当前目录一个名为train.spacy中
doc_bin.to_disk('./train.spacy')