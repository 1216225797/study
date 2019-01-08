# 1. OOP-Python面向对象

# 2. 面向对象概述(ObjectOriented,OO)
- OOP思想
    - 接到任何一个任务，首先想到是任务这个世界的构成，是有模型构成的
- 几个名词
    - OO:面向对象
    - OOA:面向对象的分析
    - OOD:面向对象的设计
    - OOI:面向对象的实现
    - OOP:面向对象的编程
    - OOA -> OOD -> OOI：面向对象的实现过程
- 类和对象的概念
    - 类：抽象名词，代表一个集合，共性的事物
    - 对象：具象的事物，单个的个体
    - 类和对象的关系
        - 一个具象，代表某一类事物的某一个个体
        - 一个抽象，代表的是一大类事物
- 类的内容，具有两个内容
    - 表明事物的特征，叫做属性(变量)
    - 表明事物的功能或动作，称为成员方法(函数)
# 3. 类的基本实现
- 类的命名
    - 遵守变量名的规范
    - 大驼峰
    - 尽量避开跟系统命名相似的命名
- 如何声明一个类
    - 必须用class关键字
    - 类由属性和方法构成，其他不允许出现
    - 成员属性定义可以直接使用变量赋值，如果没有值，则使用None
    - 案例 01.py
- 实例化类
    变量 = 类名() # 实例化了一个对象
- 访问对象成员
    - 使用点操作符
            
            obj.成员属性名称
            obj.成员方法