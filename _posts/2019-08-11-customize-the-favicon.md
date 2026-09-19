---
title: 自定义站点图标
author: 于兆海
date: 2019-08-11 00:34:00 +0800
categories: [博客, 教程]
tags: [图标]
toc: false
---

在 [**Chirpy**](https://github.com/cotes2020/jekyll-theme-chirpy/) 中，[Favicons](https://www.favicon-generator.org/about/)（站点图标）的图片文件位于 `assets/img/favicons/` 目录。你可能需要用自己制作的图标替换它们。下面来看看如何自定义这些图标。

准备好一张方形图片（PNG、JPG 或 GIF），打开 [*Favicon & App Icon Generator*](https://www.favicon-generator.org/) 网站并上传你的原始图片。

![upload-image](/assets/img/sample/upload-image.png)

点击 <kbd>Create Favicon</kbd> 按钮，稍等片刻，网站会自动生成各种尺寸的图标。

![download-icons](/assets/img/sample/download-icons.png){: width="600"}

下载生成的压缩包，解压后从解压出的文件中删除以下两个文件：

- browserconfig.xml
- manifest.json

现在，将解压出的 `.zip` 文件中剩余的图片文件（`.PNG` 和 `.ICO`）复制到 `assets/img/favicons/` 文件夹中，覆盖原有文件。

下表帮助你了解图标文件的变更：

> ✓ 表示保留，✗ 表示删除。

| 文件                 | 来自 Favicon & App Icon Generator | 来自 Chirpy |
|---------------------|:---------------------------------:|:-----------:|
| `*.PNG`             | ✓                                 | ✗           |
| `*.ICO`             | ✓                                 | ✗           |
| `browserconfig.xml` | ✗                                 | ✓           |
| `manifest.json`     | ✗                                 | ✓           |

下次构建站点时，图标将替换为自定义版本。
