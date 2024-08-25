
# 导入整个模块 这样使用，使用   模块名.函数名
import printing_functions
printing_functions.printing_functions('A4', 'white', 'blue')

# 从模块导入某个函数名， 直接使用函数名调用
from printing_functions import printing_functions
printing_functions('A4', 'white', 'blue')

# 导入模块名，将模块命名为别名，这样用
import printing_functions as pf
pf.printing_functions('A3', 'black')

# 导入模块中的函数，把函数命名别名
from printing_functions import printing_functions as pf
pf('A4', 'blue', 'red')

# 导入所有
from printing_functions import *
printing_functions('a4','green')