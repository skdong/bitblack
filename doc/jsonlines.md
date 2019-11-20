写入

```python
import jsonlines
def parse(self, response):
    jsonresponse=json.loads(response.text)
    with jsonlines.open('output.jsonl',mode='a') as writer:
        writer.write(jsonresponse)
```

读取

```python
import jsonlines
with open("xxxx.jl", "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        print(item)
```