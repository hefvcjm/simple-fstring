# simple-fstring

A simple basic f-string like behavior in Python 2

### Installation
```
$ pip install simple-fstring
```

### Usage
```
from fstring import f
a = 1
b = 2
c = u"哈哈"
d = "哈哈"
print f("${a + b}")  # 3
print f(u"我是c${c}")  # 我是c哈哈
print f("我是d${d}")  # 我是d哈哈
print f("我是d${c}c")  # 鎴戞槸d哈哈c
print f(u"我是c${d}d")  # 我是c鍝堝搱d
print f("$${}")  # ${}
print f("${{'a':'dict test'\}.get('a')}")  # dict test
print f("${{'a':'dict test'}.get('a')}")  # {'a':'dict test'.get('a')}
# specify expr namespace
print f("${a + b}", globals_ns={"a": 10, "b": 20}, locals_ns={"a": 1})  # 21
```


### License

[MIT](https://github.com/hefvcjm/simple-fstring/blob/master/LICENSE)