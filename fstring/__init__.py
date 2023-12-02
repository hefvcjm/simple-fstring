# -*- coding=utf-8 -*-
import re
import inspect

__all__ = ["f", "F", "Template"]


class Template(object):

    def __init__(self, delim="$"):
        self.__delim = delim
        self.__pattern = re.compile(r"""
        %(delim)s(?:   # 起始标识
            (?P<escaped>%(delim)s) |  # 连续两个标识转义为一个
            {(?P<expr>.*?)(?<!\\)}  # 求值表达式，\}转义结束括号
        )
        """ % {"delim": re.escape(delim)}, re.VERBOSE | re.UNICODE | re.MULTILINE)

    @staticmethod
    def __get_caller_ns():
        # 获取调用处的globals和locals
        frames = inspect.getouterframes(inspect.currentframe())
        f = frames[2][0]
        return f.f_globals, f.f_locals

    def __call__(self, s, safe=True, globals_ns=None, locals_ns=None):
        if None in (globals_ns, locals_ns):
            f_globals, f_locals = self.__get_caller_ns()
            if globals_ns is None:
                globals_ns = f_globals
            if locals_ns is None:
                locals_ns = f_locals

        def rplc(m):
            if m.group("escaped") is not None:
                return self.__delim
            expr = m.group("expr")
            if not expr:
                return ""
            try:
                expr = expr.replace("\\}", "}")  # 转义结束括号恢复
                result = eval(expr, globals_ns, locals_ns)  # 求值
                return "%s" % result
            except:
                if safe:
                    return expr
                raise

        return self.__pattern.sub(rplc, s)


f = F = Template()

if __name__ == '__main__':
    a = 1
    b = 2
    c = u"哈哈"
    d = "哈哈"
    print F("${a + b}")  # 3
    print F(u"我是c${c}")  # 我是c哈哈
    print F("我是d${d}")  # 我是d哈哈
    print F("我是d${c}c")  # 鎴戞槸d哈哈c
    print F(u"我是c${d}d")  # 我是c鍝堝搱d
    print F("$${}")  # ${}
    print F("${{'a':'dict test'\}.get('a')}")  # dict test
    print F("${{'a':'dict test'}.get('a')}")  # {'a':'dict test'.get('a')}
    print f("${a + b}", globals_ns={"a": 10, "b": 20}, locals_ns={"a": 1})  # 21
