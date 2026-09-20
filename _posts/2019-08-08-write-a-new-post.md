---
title: 如何撰写新文章
author: 于兆海
date: 2019-08-08 14:10:00 +0800
categories: [博客, 教程]
tags: [写作]
---

## 命名与路径

创建一个名为 `YYYY-MM-DD-标题.扩展名` 的新文件，并将其放在根目录的 `_posts/` 中。请注意，`扩展名` 必须是 `md` 和 `markdown` 之一。

## Front Matter（文章信息）

通常，你需要在文章顶部填写如下 [Front Matter](https://jekyllrb.com/docs/front-matter/)：

```yaml
---
title: 标题
date: YYYY-MM-DD HH:MM:SS +/-TTTT
categories: [顶级分类, 子分类]
tags: [标签]     # 标签名称应始终使用小写
---
```

> **注意**：文章的 ***layout*** 已默认设置为 `post`，因此无需在 Front Matter 中添加 ***layout*** 变量。

### 日期时区

为了准确记录文章的发布日期，你不仅需要设置 `_config.yml` 中的 `timezone`，还需要在 Front Matter 的 `date` 字段中提供文章的时区。格式：`+/-TTTT`，例如 `+0800`。

### 分类与标签

每篇文章的 `categories` 最多包含两个元素，`tags` 中的元素数量可以是零到任意多个。例如：

```yaml
categories: [Animal, Insect]
tags: [bee]
```

## 目录

默认情况下，文章的右侧面板会显示**目录**（TOC）。如果你想全局关闭它，请进入 `_config.yml` 并将变量 `toc` 的值设置为 `false`。如果你想关闭特定文章的目录，请在文章的 [Front Matter](https://jekyllrb.com/docs/front-matter/) 中添加以下内容：

```yaml
---
toc: false
---
```

## 评论

与目录类似，[Disqus](https://disqus.com/) 评论默认在每个文章中加载，全局开关由 `_config.yml` 文件中的变量 `comments` 定义。如果你想关闭某篇文章的评论，请在文章的 **Front Matter** 中添加以下内容：

```yaml
---
comments: false
---
```

## 数学公式

出于网站性能的考虑，数学公式功能默认不会加载。但可以通过以下方式启用：

```yaml
---
math: true
---
```

## Mermaid

[**Mermaid**](https://github.com/mermaid-js/mermaid) 是一个很棒的图表生成工具。要在你的文章中启用它，请在 YAML 块中添加以下内容：

```yml
---
mermaid: true
---
```

然后你就可以像其他 Markdown 语法一样使用它：用 <code class="highlighter-rouge">```mermaid</code> 包围图表代码。

## 图片

### 预览图

如果你想在文章内容顶部添加一张图片，请通过以下方式指定图片的 url：

```yaml
---
image: /path/to/image-file
---
```

### 图片说明文字

在图片的下一行添加斜体文本，它将成为图片说明，显示在图片底部：

```markdown
![图片描述](/path/to/image)
_图片说明_
```

### 图片尺寸

你可以使用 `width` 指定图片的宽度（和高度）：

```markdown
![Desktop View](/assets/img/sample/mockup.png){: width="400"}
```

### 图片位置

默认情况下图片居中，但你可以使用 `normal`、`left` 和 `right` 之一来指定位置。例如：

- **正常位置**

  图片将在下方示例中左对齐：

  ```markdown
  ![Desktop View](/assets/img/sample/mockup.png){: width="350" .normal}
  ```

- **左浮动**

  ```markdown
  ![Desktop View](/assets/img/sample/mockup.png){: width="240" .left}
  ```

- **右浮动**

  ```markdown
  ![Desktop View](/assets/img/sample/mockup.png){: width="240" .right}
  ```

> **限制**：一旦指定了图片的位置，就不能再添加图片说明文字。

## 置顶文章

你可以将一篇或多篇文章置顶到首页顶部，置顶的文章按照发布日期的倒序排列。通过以下方式启用：

```yaml
---
pin: true
---
```

## 代码块

Markdown 符号 <code class="highlighter-rouge">```</code> 可以轻松创建代码块，如下例所示。

```
This is a common code snippet, without syntax highlight and line number.
```

## 指定语言

使用 <code class="highlighter-rouge">```language</code> 可以获得带行号和语法高亮的代码片段。

> **注意**：本主题不允许使用 Jekyll 风格的 `{% raw %}{%{% endraw %} highlight LANGUAGE {% raw %}%}{% endraw %}` 或 `{% raw %}{%{% endraw %} highlight LANGUAGE linenos {% raw %}%}{% endraw %}`！

```yaml
# Yaml code snippet
items:
    - part_no:   A4786
      descrip:   Water Bucket (Filled)
      price:     1.47
      quantity:  4
```

### Liquid 代码

如果你想显示 **Liquid** 代码片段，请用 `{% raw %}{%{% endraw %} raw {%raw%}%}{%endraw%}` 和 `{% raw %}{%{% endraw %} endraw {%raw%}%}{%endraw%}` 包围 Liquid 代码。

{% raw %}
```liquid
{% if product.title contains 'Pack' %}
  This product's title contains the word Pack.
{% endif %}
```
{% endraw %}

## 了解更多

有关 Jekyll 文章的更多知识，请访问 [Jekyll Docs: Posts](https://jekyllrb.com/docs/posts/)。
