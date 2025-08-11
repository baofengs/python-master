## **Day 1 — 基础语法**

* 变量与类型（int、float、str、bool、None）
* 输入输出：`print()`、`input()`
* 基本运算：+ - \* / // % \*\*
* 练习：实现一个“温度转换器”（摄氏↔华氏）

## **JS → Python 对照表（Dify 插件开发常用）**

| 功能              | JavaScript                                                 | Python                                                                 |
| --------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------- |
| **变量声明**        | `let x = 10;`<br>`const y = "hi";`                         | `x = 10`<br>`y = "hi"`                                                 |
| **数据类型**        | `Number, String, Boolean, Object, Array, null, undefined`  | `int, float, str, bool, dict, list, tuple, None`                       |
| **字符串拼接**       | `` `Hello ${name}` ``                                      | `f"Hello {name}"`                                                      |
| **数组 / 列表**     | `arr = [1, 2, 3]`<br>`arr.push(4)`                         | `arr = [1, 2, 3]`<br>`arr.append(4)`                                   |
| **对象 / 字典**     | `obj = { a: 1, b: 2 }`<br>`obj.a` / `obj["a"]`             | `obj = { "a": 1, "b": 2 }`<br>`obj["a"]`                               |
| **循环**          | `for (let i=0; i<5; i++) {}`<br>`for (let item of arr) {}` | `for i in range(5):`<br>`for item in arr:`                             |
| **条件判断**        | `if (x > 0) {}`                                            | `if x > 0:`                                                            |
| **函数**          | `function add(a,b){return a+b}`                            | `def add(a, b): return a + b`                                          |
| **箭头函数 / 匿名函数** | `(a,b) => a+b`                                             | `lambda a, b: a + b`                                                   |
| **导入模块**        | `import fs from "fs"`                                      | `import os`<br>`from os import path`                                   |
| **异常处理**        | `try { ... } catch(e) {}`                                  | `try:\n    ...\nexcept Exception as e:\n    ...`                       |
| **JSON 解析**     | `JSON.parse(str)`<br>`JSON.stringify(obj)`                 | `json.loads(str)`<br>`json.dumps(obj)`                                 |
| **HTTP 请求**     | `fetch(url)`<br>`axios.get(url)`                           | `requests.get(url)`                                                    |
| **异步**          | `async function(){ await fetch() }`                        | `async def func():\n    await fetch()`（结合 `aiohttp` 或 `asyncio`）       |
| **类**           | `class User { constructor(name){ this.name = name } }`     | `class User:\n    def __init__(self, name):\n        self.name = name` |
| **模块导出**        | `export default func`                                      | （Python 直接调用）`if __name__ == "__main__": func()`                       |
| **常量**          | `const PI = 3.14`                                          | `PI = 3.14`（全大写表示常量习惯）                                                 |
| **空值**          | `null` / `undefined`                                       | `None`                                                                 |

---

## **特别注意（JS → Python 跨坑指南）**

1. **缩进很重要**

   * Python 没有 `{}`，用**缩进**（一般 4 空格）表示代码块。
   * 少一个空格都会语法错误。

2. **变量类型可变**

   * 不需要 `let` / `const`，赋值即定义。
   * 但习惯上全大写变量名表示常量。

3. **列表推导式**（JS 没有直接对应）

   ```python
   nums = [x*2 for x in range(5)]  # [0, 2, 4, 6, 8]
   ```

4. **函数参数**

   * 默认参数写在 `=` 后面
   * 可变参数：

     ```python
     def func(*args, **kwargs):
         print(args, kwargs)
     ```

5. **异步要配合框架**

   * Python 原生 `async` 不能直接跑，需要事件循环（`asyncio.run()` 或 FastAPI 自带的）。

---

## **建议用法**

我建议你在学的时候，把 JS 里的旧代码拿出来，**对照速查表改成 Python**，比如：

* 你之前写的记账插件里的数据处理逻辑，可以改成 Python 版本
* HTTP 请求逻辑换成 `requests` 或 `aiohttp`
* 数据存储换成 `pymysql` + Python 字典操作

这样两周下来，你的思维切换会非常快。

---

如果你愿意，我可以帮你**基于这个速查表做一个“Dify 插件开发常用 Python 模板包”**，
里面直接包含：

* HTTP 请求封装
* MySQL 读写
* 日志打印
* 配置管理
  这样你写插件时就不用从零写这些基础代码了。

你要我现在帮你做这个模板吗？这样你学的同时就能直接用到实际项目。
