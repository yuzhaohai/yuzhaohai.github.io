---
title: 快速开始
author: 于兆海
date: 2019-08-09 20:55:00 +0800
categories: [博客, 教程]
tags: [入门]
pin: true
---


## 安装

在 GitHub 上 [**Fork Chirpy**](https://github.com/cotes2020/jekyll-theme-chirpy/fork)，将仓库重命名为 `USERNAME.github.io`（其中 `USERNAME` 是你的 GitHub 用户名），然后在终端中克隆该分支到本地：

```terminal
$ git clone https://github.com/USERNAME/USERNAME.github.io.git -b master --single-branch
```

### 搭建本地环境

如果你想在本地机器上运行或构建项目，请参考 [Jekyll 文档](https://jekyllrb.com/docs/installation/) 完成 `Ruby`、`RubyGems`、`Jekyll` 和 `Bundler` 的安装。

在首次运行或构建之前，请先安装 Jekyll 插件。进入项目根目录并运行：

```terminal
$ bundle install
```

`bundle` 会自动安装 `Gemfile` 中指定的所有依赖。

### 使用 Docker 环境（可选）

如果你是 [**Docker**](https://www.docker.com/) 的忠实爱好者，或者只是懒得安装上面提到的软件包，请确保 **Docker Engine** 已安装并运行，然后通过以下命令从 Docker Hub 获取 `jekyll/jekyll` 镜像：

```console
$ docker pull jekyll/jekyll
```

## 使用方法

### 初始化

进入项目根目录并开始初始化：

```console
$ bash tools/init.sh
```

> **注意**：如果你不打算部署到 GitHub Pages，请在以上命令末尾添加参数选项 `--no-gh`。

它所做的事情如下：

1. 从你的仓库中删除一些文件或目录：

    - `.travis.yml`
    - `_posts` 下的文件
    - `docs` 文件夹

2. 如果你使用了 `--no-gh` 选项，`.github` 目录将被删除。否则，将通过移除 `.github/workflows/pages-deploy.yml.hook` 的扩展名 `.hook` 来设置 GitHub Action 工作流，然后删除 `.github` 文件夹中的其他文件和目录。

3. 自动创建一次提交以保存更改。

### 配置

通常，进入 `_config.yml` 并按需配置其中的变量。其中一些典型选项如下：

- `url`
- `avatar`
- `timezone`
- `theme_mode`

### 本地运行

你可能希望在发布前预览站点内容，只需运行：

```terminal
$ bundle exec jekyll s
```

然后在浏览器中访问 <http://localhost:4000>。

### 使用 Docker 运行

使用以下命令在 Docker 上运行站点：

```terminal
$ docker run --rm -it \
    --volume="$PWD:/srv/jekyll" \
    -p 4000:4000 jekyll/jekyll \
    jekyll serve
```


### 部署

部署开始前，请检查 `_config.yml` 文件，确保 `url` 配置正确。此外，如果你更喜欢 [_项目站点_](https://help.github.com/en/github/working-with-github-pages/about-github-pages#types-of-github-pages-sites) 且不使用自定义域名，或者你希望在其他不是 **GitHub Pages** 的 Web 服务器上通过 baseurl 访问你的网站，请记得将 `baseurl` 改为以斜杠开头的项目名称，例如 `/project`。

假设你已经完成了[初始化](#初始化)，现在可以选择以下任一方法来部署你的网站。

#### 部署到 GitHub Pages

出于安全原因，GitHub Pages 构建运行在 `safe` 模式下，这限制了使用插件生成额外页面文件。因此，我们可以使用 **GitHub Actions** 构建站点，将构建好的站点文件存储在新分支上，并使用该分支作为 Pages 服务的来源。

1. 推送任意提交到 `origin/master` 以触发 GitHub Actions 工作流。一旦构建完成并成功，会出现一个名为 `gh-pages` 的新远程分支，用于存储构建好的站点文件。

2. 浏览到仓库主页，在 _Settings_ → _Options_ → _GitHub Pages_ 中选择 `gh-pages` 分支作为[发布来源](https://docs.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)：
    ![gh-pages-sources](/assets/img/sample/gh-pages-sources.png){: width="650" class="normal"}

3. 访问 GitHub 指示的网站地址。

#### 部署到其他平台

在除 GitHub 之外的平台上，我们无法享受 **GitHub Actions** 的便利。因此，我们应该在本地（或其他第三方 CI 平台）构建站点，然后将站点文件放到服务器上。

进入源项目根目录，通过以下命令构建站点：

```console
$ JEKYLL_ENV=production bundle exec jekyll b
```

或者使用 Docker 构建：

```terminal
$ docker run -it --rm \
    --env JEKYLL_ENV=production \
    --volume="$PWD:/srv/jekyll" \
    jekyll/jekyll \
    jekyll build
```

除非你指定了输出路径，否则生成的站点文件将放在项目根目录的 `_site` 文件夹中。现在你应该将这些文件上传到你的 Web 服务器。
