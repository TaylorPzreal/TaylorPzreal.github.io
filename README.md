# Github Pages Blog

## Development

Base <https://getpelican.com/>

```sh
conda create -n py_pelican_12 python=3.12
conda activate py_pilican_12
pip install "pelican[markdown]"

# 本地开发
pelican -r -l
# http://localhost:8000/ 

# Build
pelican content

pelican --listen
```

导出依赖

```sh
pip freeze > requirements.txt
```


## Create an article

文章模板示例

```md
Title: My super title
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Authors: Alexis Metaireau, Conan Doyle
Summary: Short version for index and feeds
lang: zh-cn/en
status: draft/hidden/skip/published

This is the content of my super blog post.
```

