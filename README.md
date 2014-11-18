# 介绍

一些用于从[努努书坊][]下载小说并用 [pandoc][] 制作电子书的脚本

# 脚本

- down.py - 从[努努书坊][]下载小说并保存为 json 格式
- tomd.py - 把 xxx.json 转换为Markdown格式文件 xxx.md

# 依赖

- Python 2.7
- 安装 requests 和 lxml
    * `pip install requsts`
    * `pip install lxml`
    * Windows推荐直接下载[安装包][pythonlibs]
- [pandoc][]

  [pandoc]: http://johnmacfarlane.net/pandoc/ "Pandoc"
  [努努书坊]: http://book.kanunu.org/ "小说在线阅读"
  [pythonlibs]: http://www.lfd.uci.edu/~gohlke/pythonlibs/ "Unofficial Windows Binaries for Python Extension Packages"
