14-15周
======

**数据库任务**

.. class:: prettyprint lang-sql

:: 

    create table foo (  
        bar serial  
    );

jianxiaoqi  
----------

1. 将井字棋 *pull request* 到此
2. 学习 tornado_ 框架，输入 https://localhost:8000/helloworld 输出 ``hello, world`` (参照 helloworld.py_ )
3. 不使用数据库和 ``session`` ，参照 demo_ 完成简单登录功能
4. 在 *psql* 下进行基本的 ``select`` ``insert`` ``update`` ``delete`` 操作
5. 使用数据库完成 **任务3**
6. \*使用数据库和 ``session`` 完成 **任务3**
  
weishuwen
---------
1. 将黑白棋 *pull request* 到此
2. 其余同 `jianxiaoqi`_
  
lilinfeng
---------

* 同 `weishuwen`_
  
zhangshiyi
----------

1. fork `jianxiaoqi`_ 井字棋，读懂代码
2. 用python实现井字棋
3. 阅读 `pro git <http://git-scm.com/book/zh>`_ 到2.5
4. \*将井字棋 *pull request* 到此

lichaopeng
----------

1. 完成扫雷
2. 将扫雷 *pull request* 到此
3. 在 *psql* 下进行基本的 ``select`` ``insert`` ``update`` ``delete`` 操作
4. 学习 tornado_ 框架，输入 https://localhost:8000/helloworld 输出 ``hello, world`` (参照 helloworld.py_ )
5. 给 *扫雷* 添加一个 *保存按钮* , 玩家点击 *保存* 时将当前游戏状态存到服务器(提示:不要用数据库,假设玩家只有一个).即玩家关闭浏览器再打开时自动加载上次保存的游戏
6. \*用 ``session`` 实现 **任务5** (假设玩家有多个)
7. \*用数据库实现 **任务5**

.. _demo: https://github.com/loggerhead/tornado-memcached-sessions/blob/master/demo/main.py
.. _helloworld.py: https://github.com/facebook/tornado/blob/master/demos/helloworld/helloworld.py
.. _tornado: https://github.com/facebook/tornado
