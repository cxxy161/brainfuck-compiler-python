# brainfuck-compiler-python
基于py的一种从神秘自创语言转译到brainfuck的项目

# 使用方法
下面有ai写的api文档(:

提供了几个我自己写的示例

目前仍在持续更新

我写的这个bf解释器增加了两个关键字，

r是代表在当前单元格生成一个0-255的随机数

c是代表输出当前的内存等状态，调试用的

## 自定义语法表
by Gemini-2.5flash
| 命令 | 参数 | 解释 | 示例 |
| :--- | :--- | :--- | :--- |
| **`var`** | `name`, `number` | 声明变量 `name` 并初始化为 `number`（数字或rand）若为rand，则将变量初始化成一个0-255的随机数。 | `var count 10` |
| **`put`** | `name`, `number` | 设置已声明的变量 `name` 的值为 `number`。 | `put count 255` |
| **`copy`** | `where`, `to` | 复制变量 `where` 的值到变量 `to`。 | `copy var1 result` |
| **`cont`** | `to`, `v1`, `yun`, `v2` | 执行算术/赋值操作 $to = v1 \text{ } yun \text{ } v2$。`yun` 可为 `+`, `-`, `*`, `/`, `%`, `opp` (取负)。 | `cont total num1 + num2` |
| **`is`** | `to`, `v1`, `yun`, `v2` | 执行逻辑判断 $v1 \text{ } yun \text{ } v2$，结果（1 或 0）存入 `to`。`yun` 可为 `>`, `<`, `=`, `not`, `and`, `or`, `in`（in的v2必须为列表）。 | `is flag x = 10` |
| **`varlist`** | `name`, `long` | 声明名为 `name`、长度为 `long` 的列表。 | `varlist my_array 5` |
| **`putlist`** | `name`, `list` | 用逗号分隔的值初始化列表 `name` 的元素。 | `putlist my_array 1,2,3,4,5` |
| **`getlist`** | `sto`, `ln`, `sw` | 从列表 `ln` 的索引 `sw` 处取值，存入变量 `sto`。`sw` 可为数字或变量。| `getlist value my_array index_var` |
| **`setlist`** | `ln`, `sw`, `sv` | 将值 `sv` 存入列表 `ln` 的索引 `sw` 处。`sw` 和 `sv` 可为数字或变量。 | `setlist my_array 2 new_value` |
| **`printi`** | `var` | 以十进制形式打印变量 `var` 的值。 | `printi count` |
| **`prints`** | `str...` | 打印字符串。使用 `^` 代表换行符。 | `prints Result is: ^` |
| **`inputi`** | `varn` | 从用户接收一位的整数输入，存入 `varn`。 | `inputi input_char` |
| **`if`** | `var` 或 `: v1 yun v2` | 条件开始。如果 `var` 非零或条件 `: v1 yun v2` （该语法等同于is）成立，则执行块内代码。 | `if condition_var` / `if : x > 10` |
| **`else`** | *(无)* | `if` 条件不满足时执行的块。 | `else` |
| **`while`** | `var` | 循环开始。只要 `var` 非零就重复执行块内代码。 | `while loop_flag` |
| **`for`** | `item`, `list` | 循环开始。遍历列表 `list`，将每个元素赋值给 `item`。 （修改item不会改变原列表）| `for element my_array` |
| **`func`** | `name` | 函数定义开始。 | `func calculate` |
| **`run`** | `name` | 函数调用。 | `run calculate` |
| **`}`** | *(无)* | 结束最近的 `if`, `else`, `while`, `for`, 或 `func` 块。 | `}` |
| **`delvar`** | `name` | 删除变量 `name` 并释放其占用的单元格。 | `delvar temp_var` |
| **`#`** | *(任意)* | 注释行，编译器会跳过。 | `# This is a comment` |

# 编写限制
prints 因为brainfuck的限制不支持中文

else必须紧贴着上一行的}

由于brainfuck限制，目前所有var为8位整数，最大值为255，所以255+1=0

目前不支持任何缩进，否则会导致报错

不能在代码后面添加注释

inputi只能获取一位的用户输入，如需要多位输入，请通过多次的inputi来一位一位的获取

所有变量都必须先使用var进行初始化

