# 1. 安装依赖

> [Python 用pip批量安装包 requirements.txt（python查看安装的第三方扩展包）| 利用requirements.txt离线安装依赖包](https://blog.csdn.net/inthat/article/details/117026589)


```shell
C:\Users\admin\AppData\Local\Programs\Python\Python37\Scripts\pip3.exe install ddddocr -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
C:\Users\admin\AppData\Local\Programs\Python\Python37\Scripts\pip3.exe install flask -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
C:\Users\admin\AppData\Local\Programs\Python\Python37\Scripts\pip3.exe install gevent -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```



## pip 更新

```shell
pip install --upgrade pip
```

或者

```shell
[notice] A new release of pip available: 22.3.1 -> 23.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip
```


## 制作`requirements.txt`文件

```shell
C:\Users\admin\AppData\Local\Programs\Python\Python37\Scripts\pip3.exe install pipreqs -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

pipreqs.exe ./ --encoding=utf8

# 根据文件进行包安装
C:\Users\admin\AppData\Local\Programs\Python\Python37\Scripts\pip3.exe install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```



## 利用requirements.txt离线安装依赖包

### 下载离线的包到指定目录

###### 将requirements.txt中导入的包离线下载到 package_tmp_dir 文件夹

```shell
pip wheel -w package_tmp_dir -r requirements.txt
pip download -d package_tmp_dir -r requirements.txt
```

### 安装离线的包

```shell
pip install --no-index --find-links=package_tmp_dir  -r requirements.txt
```