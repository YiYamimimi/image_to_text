Python Django+HTML+css+JavaScript 图片转文字

安装Django：在命令行中运行 pip install django

使用Tesseract OCR库进行图片转文字 pip install pytesseract

### 后端
1.创建Django项目：
在命令行中运行 django-admin startproject image_to_text 创建一个名为image_to_text的Django项目。

2.进入项目目录：cd image_to_text。

3.创建Django应用：
在命令行中运行 python manage.py startapp image_converter 创建一个名为image_converter的Django应用。

4.在image_converter/views.py中编写视图函数

5.在image_to_text/urls.py中配置URL路由

### 前端：
在image_converter目录下创建templates文件夹，并在其下创建index.html和result.html两个模板文件。

### 运行：
返回项目根目录，在命令行中运行 python manage.py runserver 启动Django服务器。
在浏览器中访问 http://localhost:8000/ 即可使用图片转文字功能。

### 效果：
![效果图](https://img1.imgtp.com/2023/07/04/8Gcus40a.png)
