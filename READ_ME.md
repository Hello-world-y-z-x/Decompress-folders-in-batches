使用的库(两个均为内置库, 无需安装)

> os
>
> zipfile

walk_file 遍历当前文件中的所有文件及文件夹中文件

unzip 解压压缩包

如果**文件夹名字是英文**, 可以直接将un_zip文件放在当前文件夹中直接操作



如果**文件夹名字是中文** 请接着往下看, 编码问题的报错会十分头疼

需要修改原码zipfile.py中的两处(因为zipfile只支持utf-8和cp437两种编码)

> encode -> 解码, decode -> 编码

![image-20211231192032972](C:\Users\刘在源\AppData\Roaming\Typora\typora-user-images\image-20211231192032972.png)

![image-20211231192259380](C:\Users\刘在源\AppData\Roaming\Typora\typora-user-images\image-20211231192259380.png)

参考内容如下:

>文件夹遍历: https://www.cnblogs.com/wt7018/p/11610286.html
>zipfile的使用: https://www.cnblogs.com/thomson-fred/p/10328662.html
>解压文件名乱码: https://www.cnblogs.com/limengjie0104/archive/2018/06/17/9192449.html

