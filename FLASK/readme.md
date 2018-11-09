# 配置文件
- 使用'config.py'文件
- 使用'app.config.from_object(config)'加载配置参数


## 1.数据库安装
- Mac 本地启动mysql

  ```bash
  # 启动
  mysql -uroot -p 
  # 输入密码
  ```

- 安装mysql-python

  ```bash
  sudo pip install mysql-python
  ```

- 安装flask-sqlalchemy

  使用flask与数据库之间进行关系映射，对数据库进行增删改查等操作。可以想在Python中操作类一样对数据库进行操作，数据库中的表抽象成了类，数据库中的每条数据对应类中的一个对象。

  ```bash
  # pip 安装
  pip install flask-sqlalchemy
  # conda 安装
  conda install -c conda-forge flask-sqlalchemy 
  ```

- sqlalchemy连接数据库