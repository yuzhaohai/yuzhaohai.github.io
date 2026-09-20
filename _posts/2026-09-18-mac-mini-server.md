---
title: M2丐中丐版Mac mini，搭建一台真正属于自己的服务器
author: 于兆海
date: 2026-09-18 11:33:00 +0800
categories: [博客, 教程]
tags: [Mac, Mac mini, 服务器, Docker]
---

# M2丐中丐版Mac mini，搭建一台真正属于自己的服务器

<u>**前言：我这里为了大家更方便食用本视频，我将Mac mini还原成刚买来的样子给大家做演示！**</u>

## 前期准备

- Mac mini一台
- 最好是有一个公网IP，否则就花钱买服务器，再不然就是只能搭建在本地

**电脑开机正常激活**

## 基本设置：

**服务器是7*24小时运行的，所以需要相关的一些设置**
- 设置-->节能-->显示器关闭时，防止制动进入睡眠（打开）-->唤醒已供网络访问（打开）-->断电后制动启动（打开）
- 设置-->锁定屏幕-->不活跃时启动屏幕保护程序（永不）-->不活跃时关闭显示器（永不）
- 设置-->用户与群组-->自动以此身份登陆（选择自己设置的账户）
- 设置-->通用-->共享-->文件共享（打开）-->远程管理（打开）-->远程登录（打开）-->远程应用程序脚本（打开）-->（其他按各人需求设置）

**自己使用时比较舒适的设置（看个人喜好设置）:**(我是用的是触控板)

- 设置-->桌面与程序坞-->程序坞大小：20%-->程序坞放大：60%-->置于屏幕上的位置（左侧）-->最小化窗口时使用（神奇效果）-->将窗口最小化至应用程序图标（打开）-->自动隐藏和显示程序坞（打开）-->弹跳打开应用程序（打开）-->点按强制以显示桌面（始终）-->台前调度（挺好用的，只是偶尔需要两个应用程序参照，就会关掉）
- 设置-->触控板-->静默点按（关闭）-->用力点按和触感反馈（打开）-->轻点来点按（打开）
- 设置-->辅助功能-->指针控制-->触控板选项-->使用触控板进行拖移（打开）-->拖移样式（三指拖移）
设置-->网络-->以太网-->详细信息-->TCP/IP-->配置IPv4（手动）-->ip地址最后一段按各人喜好填写，不要跟其他网络设备IP重复就好了！

## 网络设置：

### Surge配置：（当然也可以用其他类似的软件）

- 概览-->系统代理（打开）-->增强模式（打开）-->HTTP&SCOKS5代理（打开）
- 更多-->模块-->从URL安装模块-->`https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/config/Surge.sgmodule`-->安装完成后点应用
- 解密-->HTTPS解密（打开）-->生成新证书-->将证书安装到系统-->重启Surge
- 打开浏览器输入：`https://sub.store`-->右下角“+”-->单条订阅-->名称（随意尽量英文）-->链接（🐔场给的）-->添加一个操作（国旗操作、节点排序、正则过滤）-->正则过滤（过滤模式）-->保存
- 点生成的订阅-->Surge后面的复制图标-->重新打开一个浏览器粘贴到地址栏-->就会看到所有节点，看看有没有（剩余流量、剩余日期....之类的）如果有就直接复制（=trojan等于号前面一段）-->返回到订阅管理页面-->点钢笔图标打开刚刚生成的订阅-->把刚刚复制的粘贴到正则表达式里面，再点后面的定位图标-->添加一个操作（脚本操作）-->脚本操作的链接：`https://raw.githubusercontent.com/Keywos/rule/main/rename.js`-->保存
- 点生成的订阅-->Surge后面的复制图标-->重新打开一个浏览器粘贴到地址栏-->就会看到所有节点，如果没有剩余流量、剩余日期....之类的）就OK了

**替换配置文件：**

- 新建一个文本文件：abc.conf（abc可以替换成你想要的名字）-->打开这个文件
  - 或者打开终端：`cd /Users/mrdong/Documents`
  - 再次输入：`Touch abc.conf`


```
# > Surge 范例托管配置文件，推荐搭配 Sub-Store 插件进行使用
 
# > 范例托管文件长久地址：https://v2rayssr.com/surge-sub.html
 
# > 若有使用问题，请配合上述网页中的视频演示，对配置文件进行修改，有问题，请到电报群进行讨论学习：https://t.me/bozaiweb
 
[General]
# > 日志级别
loglevel = notify
show-error-page-for-reject = true
# > Wi-Fi 访问
allow-wifi-access = false
# > All Hybrid 网络并发
all-hybrid = false
# > IPv6 支持（默认关闭）
ipv6 = false
# > 测试超时（秒）
test-timeout = 2
# > Internet 测试 URL
internet-test-url = http://www.baidu.com
# > 代理测速 URL
proxy-test-url = http://www.google.com/generate_204
# > GeoIP数据库
geoip-maxmind-url = https://github.com/Hackl0us/GeoIP2-CN/raw/release/Country.mmdb
# > 排除简单主机名
exclude-simple-hostnames = true
# > DNS 服务器
dns-server = 223.5.5.5, 119.29.29.29
hijack-dns = 8.8.8.8:53, 8.8.4.4:53
# > 从 /etc/hosts 读取 DNS 记录
read-etc-hosts = true
# > 远程控制器
http-api-web-dashboard = false
use-default-policy-if-wifi-not-primary = false
# > 跳过代理
skip-proxy = 127.0.0.1, 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, 100.64.0.0/10, 17.0.0.0/8, localhost, *.local, *.crashlytics.com, seed-sequoia.siri.apple.com, sequoia.apple.com
# > Always Real IP Hosts
always-real-ip = *.srv.nintendo.net, *.stun.playstation.net, xbox.*.microsoft.com, *.xboxlive.com*.srv.nintendo.net, *.stun.playstation.net, xbox.*.microsoft.com, *.xboxlive.com, *.battlenet.com.cn, *.battlenet.com, *.blzstatic.cn, *.battle.net
http-listen = 0.0.0.0
socks5-listen = 0.0.0.0
 
[Replica]
# > 隐藏 Apple 请求
hide-apple-request = false
# > 隐藏崩溃追踪器请求
hide-crash-reporter-request = true
# > 隐藏 UDP 会话
hide-udp = false
# > 关键词过滤器
keyword-filter-type = false
 
[Proxy Group]
🚀 节点选择 = select, ♻️ 自动选择, 🇭🇰 香港节点, 🇨🇳 台湾节点, 🇸🇬 狮城节点, 🇯🇵 日本节点, 🇺🇲 美国节点, 🇰🇷 韩国节点, 🚀 手动切换, DIRECT
🚀 手动切换 = select, policy-path=填上你Sub-Store的节点信息
♻️ 自动选择 = url-test, policy-path=填上你Sub-Store的节点信息, url=http://www.gstatic.com/generate_204, interval=300, tolerance=50
📲 电报消息 = select, 🚀 节点选择, ♻️ 自动选择, 🇸🇬 狮城节点, 🇭🇰 香港节点, 🇨🇳 台湾节点, 🇯🇵 日本节点, 🇺🇲 美国节点, 🇰🇷 韩国节点, 🚀 手动切换, DIRECT
💬 OpenAi = select, 🚀 节点选择, ♻️ 自动选择, 🇸🇬 狮城节点, 🇭🇰 香港节点, 🇨🇳 台湾节点, 🇯🇵 日本节点, 🇺🇲 美国节点, 🇰🇷 韩国节点, 🚀 手动切换, DIRECT
📹 油管视频 = select, 🚀 节点选择, ♻️ 自动选择, 🇸🇬 狮城节点, 🇭🇰 香港节点, 🇨🇳 台湾节点, 🇯🇵 日本节点, 🇺🇲 美国节点, 🇰🇷 韩国节点, 🚀 手动切换, DIRECT
🎥 奈飞视频 = select, 🎥 奈飞节点, 🚀 节点选择
📺 巴哈姆特 = select, 🇨🇳 台湾节点, 🚀 节点选择, 🚀 手动切换, DIRECT
📺 哔哩哔哩 = select, 🎯 全球直连, 🇨🇳 台湾节点, 🇭🇰 香港节点
🌍 国外媒体 = select, 🚀 节点选择, ♻️ 自动选择, 🇭🇰 香港节点, 🇨🇳 台湾节点, 🇸🇬 狮城节点, 🇯🇵 日本节点, 🇺🇲 美国节点, 🇰🇷 韩国节点, 🚀 手动切换, DIRECT
🌏 国内媒体 = select, DIRECT, 🇭🇰 香港节点, 🇨🇳 台湾节点, 🇸🇬 狮城节点, 🇯🇵 日本节点, 🚀 手动切换
📢 谷歌FCM = select, DIRECT, 🚀 节点选择, 🇺🇲 美国节点, 🇭🇰 香港节点, 🇨🇳 台湾节点, 🇸🇬 狮城节点, 🇯🇵 日本节点, 🇰🇷 韩国节点, 🚀 手动切换
Ⓜ️ 微软云盘 = select, DIRECT, 🚀 节点选择, 🇺🇲 美国节点, 🇭🇰 香港节点, 🇨🇳 台湾节点, 🇸🇬 狮城节点, 🇯🇵 日本节点, 🇰🇷 韩国节点, 🚀 手动切换
Ⓜ️ 微软服务 = select, DIRECT, 🚀 节点选择, 🇺🇲 美国节点, 🇭🇰 香港节点, 🇨🇳 台湾节点, 🇸🇬 狮城节点, 🇯🇵 日本节点, 🇰🇷 韩国节点, 🚀 手动切换
🍎 苹果服务 = select, DIRECT, 🚀 节点选择, 🇺🇲 美国节点, 🇭🇰 香港节点, 🇨🇳 台湾节点, 🇸🇬 狮城节点, 🇯🇵 日本节点, 🇰🇷 韩国节点, 🚀 手动切换
🎮 游戏平台 = select, DIRECT, 🚀 节点选择, 🇺🇲 美国节点, 🇭🇰 香港节点, 🇨🇳 台湾节点, 🇸🇬 狮城节点, 🇯🇵 日本节点, 🇰🇷 韩国节点, 🚀 手动切换
🎶 网易音乐 = select, DIRECT, 🚀 节点选择, ♻️ 自动选择
🎯 全球直连 = select, DIRECT, 🚀 节点选择, ♻️ 自动选择
🛑 广告拦截 = select, REJECT, DIRECT
🍃 应用净化 = select, REJECT, DIRECT
🐟 漏网之鱼 = select, 🚀 节点选择, ♻️ 自动选择, DIRECT, 🇭🇰 香港节点, 🇨🇳 台湾节点, 🇸🇬 狮城节点, 🇯🇵 日本节点, 🇺🇲 美国节点, 🇰🇷 韩国节点, 🚀 手动切换
# > 外部节点自动匹配
# > 匹配到关键字，自动收纳为节点组
🇭🇰 香港节点 = url-test, policy-path=填上你Sub-Store的节点信息, policy-regex-filter=(🇭🇰)|(港)|(Hong)|(HK), url=http://www.gstatic.com/generate_204, interval=300, tolerance=150
🇨🇳 台湾节点 = url-test, policy-path=填上你Sub-Store的节点信息, policy-regex-filter=(🇨🇳)|(台)|(Tai)|(TW), url=http://www.gstatic.com/generate_204, interval=300, tolerance=150
🇺🇲 美国节点 = url-test, policy-path=填上你Sub-Store的节点信息, policy-regex-filter=(🇺🇸)|(美)|(States)|(US), url=http://www.gstatic.com/generate_204, interval=300, tolerance=150
🇯🇵 日本节点 = url-test, policy-path=填上你Sub-Store的节点信息, policy-regex-filter=(🇯🇵)|(日)|(Japan)|(JP), url=http://www.gstatic.com/generate_204, interval=300, tolerance=150
🇸🇬 狮城节点 = url-test, policy-path=填上你Sub-Store的节点信息, policy-regex-filter=(🇸🇬)|(新)|(Singapore)|(SG), url=http://www.gstatic.com/generate_204, interval=300, tolerance=150
🇰🇷 韩国节点 = url-test, policy-path=填上你Sub-Store的节点信息, policy-regex-filter=(🇰🇷)|(韩)|(Korea)|(KR), url=http://www.gstatic.com/generate_204, interval=300, tolerance=150
🎥 奈飞节点 = select, policy-path=填上你Sub-Store的节点信息, policy-regex-filter=(NF)|(奈飞)|(Netflix)|(video)|(Video)|(nf), url=http://www.gstatic.com/generate_204, interval=300, tolerance=150
 
[Rule]
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/LocalAreaNetwork.list,🎯 全球直连,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/UnBan.list,🎯 全球直连,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list,🛑 广告拦截,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanProgramAD.list,🍃 应用净化,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/GoogleFCM.list,📢 谷歌FCM,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/GoogleCN.list,🎯 全球直连,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/SteamCN.list,🎯 全球直连,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/OneDrive.list,Ⓜ️ 微软云盘,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Microsoft.list,Ⓜ️ 微软服务,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Apple.list,🍎 苹果服务,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Telegram.list,📲 电报消息,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/OpenAi.list,💬 OpenAi,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/NetEaseMusic.list,🎶 网易音乐,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Epic.list,🎮 游戏平台,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Origin.list,🎮 游戏平台,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Sony.list,🎮 游戏平台,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Steam.list,🎮 游戏平台,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Nintendo.list,🎮 游戏平台,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/YouTube.list,📹 油管视频,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Netflix.list,🎥 奈飞视频,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Bahamut.list,📺 巴哈姆特,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/BilibiliHMT.list,📺 哔哩哔哩,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Bilibili.list,📺 哔哩哔哩,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaMedia.list,🌏 国内媒体,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ProxyMedia.list,🌍 国外媒体,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ProxyGFWlist.list,🚀 节点选择,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaDomain.list,🎯 全球直连,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaCompanyIp.list,🎯 全球直连,update-interval=86400
RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Download.list,🎯 全球直连,update-interval=86400
GEOIP,CN,🎯 全球直连
FINAL,🐟 漏网之鱼
```

- 把以上代码复制粘贴到：abc.conf文件中，再把Sub-store的surge订阅链接替换掉以上代码的`填上你Sub-Store的节点信息`这一串文字，完成之后（cmmmand+S保存）退出
- 打开Surge-->更多-->配置-->导入...-->选择刚刚修改的abc.conf文件打开-->解密-->HTTPS解密（打开）-->生成新证书-->将证书安装到系统-->下面三个选项全部打勾-->重启surge-->完成

## 安装应用程序

### Clean MyMac X：

<u>这是一款Mac 系统优化工具，帮助用户清理、优化和保护他们的 Mac 设备，以提高系统性能并释放磁盘空间。</u>

安装包以保存文件夹！

### Homebrew：（必要）

<u>这是一款使用命令行下载安装软件管理软件的应用</u>

#### 安装设置：

- 打开终端-->输入一键安装命令：`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`回车
- 当出现`Press RETURN/ENTER to continue or any other key to abort:`这一串话时说明安装好了，按回车

**接下来修改环境变量：**（这里切换成英文输入法）

- 打开终端-->输入命令：`vim ~/.bash_profile`进入编辑模式
- （按“i”才可以编辑）复制粘贴以下两行代码：
- export PATH=$PATH:/Users/klee/library/Android/sdk/platform-tools
- export PATH=$PATH:/opt/homebrew/bin
- 按“ESC”再输入：wq再回车（这就是保存退出了）

**修改第二个环境变量：**

- 输入命令：`vim ~/.zshrc`进入编辑模式
- （按“i”才可以编辑）复制粘贴以下两行代码：
- source ~/.bash_profile
- 按“ESC”再输入：wq再回车（这就是保存退出了）

#### 命令行使用方法：

- 查看Homebrew版本号：```brew --version```
- 安装软件：```brew install 软件名称```
- 搜索相关软件名称：```brew search 关键词```
- 查看安装了哪些软件：```brew list```
- 查看所有有更新版本的软件：```brew outdated```
- 更新所有软件：```brew upgrade```
- 更新指定当个软件：```brew upgeade 软件名```
- 卸载指定软件：```brew uninstall 软件名```
- 查看指定某个软件详细信息：```brew info 软件名```
- 清理系统所有软件的历史版本遗留：```brew cleanup```
- 清理指定软件的历史版本遗留：```brew cleanup 软件名```

### Final cat pro：推荐（非必要）

<u>这是一款Apple官方出品的剪辑软件</u>

***无法通过HomgBrew下载安装***

- [官网90天试用下载地址：](https://www.apple.com.cn/final-cut-pro/trial/)

**白嫖命令：**

- ```mv -v ~/Library/Application\ Support/.ffuserdata ~/.Trash```

**命令使用方法**：

- 到期的时候会提醒“购买”还是“退出”
- 直接点退出
- 打开终端输入**白嫖命令**，回车
- 再次打开Final cat pro，会提示试用版将于90天后到期

### Typora：推荐（非必要）

<u>这是一款可以自动保存进度的markdown写作软件</u>

***可通过HomgBrew下载安装***

- 一键安装命令：```brew install typora```

**白嫖激活方法**

- 安装好后打开访达→应用程序→找到Typora→右键显示包内容→Contents→Resources→TypeMark→page-dist→static→js→把LicenseIndex.180dd4c7.e861f46f.chunk.js文件复制到桌面→打开桌面LicenseIndex.180dd4c7.e861f46f.chunk.js文件→把 hasActivated="true"==e.hasActivated替换成hasActivated="true"=="true"→保存→把改完的文件跟原文件替换掉→完成

### bilibili：推荐（非必要）

<u>这就不用介绍了</u>

***可通过HomgBrew下载安装***

- 一键安装命令：`brew install bilibili`

### infuse：推荐（非必要）

<u>这是一款可以自动生成海报墙的视频播放软件</u>

***无法通过HomgBrew下载安装***

- 前往AppStore手动下载安装

### Stay：推荐（非必要）

<u>这是一款Safari浏览器的插件</u>

***无法通过HomgBrew下载安装***

- 前往AppStore手动下载安装
- [插件网站：](https://greasyfork.org/zh-CN)

### FinalShell：推荐（接近必要）

<u>这是一款SSH远程终端工具</u>

***可通过HomgBrew下载安装***

- 一键安装命令：`brew install finalshell`
- 设置方式-->打开Finalshell-->点击上方文件夹图标-->添加SSH链接-->名称：（随意）-->主机：(本机电脑的IP地址）-->用户名/密码：(本机电脑的账号密码)-->确定

- 

---

### MacZip：推荐（非必要）

<u>这是一款解压缩软件</u>

***可通过HomgBrew下载安装***

- 一键安装命令：`brew install maczip`

### Rectangle：推荐（非必要）

<u>这是一款桌面窗口管理软件</u>

***可通过HomgBrew下载安装***

- 一键安装命令：`brew install rectangle`



### PlayCover：推荐（非必要）

<u>这是一款可以在mac上面玩ipad游戏的模拟器</u>

***无法通过HomgBrew下载安装***

- [手动前往GitHub下载](https://github.com/PlayCover/PlayCover/releases/tag/3.0.0-beta.2)

### Google Chrome

<u>这是谷歌浏览器</u>

***可通过HomgBrew下载安装***

- 一键安装命令：`brew install google-chrome`

### Speedtest：推荐（非必要）

<u>这是一款测速软件</u>

***无法通过HomgBrew下载安装***

- 前往AppStore手动下载安装

### 剪映：推荐（非必要）

<u>这是一款剪辑软件，通常用来帮Final cut pro导字幕</u>

***无法通过HomgBrew下载安装***

- 前往AppStore手动下载安装

### Parsec远程桌面：推荐（必要）

<u>这是一款非常丝滑的远程桌面操控软件</u>

***可通过HomgBrew下载安装***

- 一键安装命令：`brew install parsec`

### OrbStack：推荐（必要）

<u>这是一款平替Docker的软件，相应速度快，占用资源小</u>

***可通过HomgBrew下载安装***

- 一键安装命令：`brew install orbstack`

#### 小雅：

***要用root权限安装***

sudo -i

***一键安装命令:***
`bash -c "$(curl http://docker.xiaoya.pro/update_new.sh)"`

输入command+shift+句号，要一起按，就会出来隐藏文件夹

***mytoken.txt***
获取32位阿里云盘token方式：[点击进入](https://aliyuntoken.vercel.app/)

***myopentoken.txt***
获取280位open token方式：[点击进入](https://alist.nn.ci/zh/guide/drivers/aliyundrive_open.html)

***temp_transfer_folder_id.txt***
阿里云盘小雅转存目录

***guestlogin.txt***
在/xiaoya目录下`touch guestlogin.tx`

- 这个是设置小雅的强制登陆，空文件就可以
- 强制登陆账号：dav

***guestpass.txt***
在/xiaoya目录下`vi guestpass.txt`

- 这个是设置小雅的强制登陆密码

***iptv.m3u***
在/xiaoya目录下`vi iptv.m3u`编辑电视频道直播源
[iptv.m3u](joplin://528db4953bf14b548ebde83c1d5069b8)

***docker_address.txt***
在/xiaoya目录下`vi docker_address.txt`编辑小雅IP地址

- 这个是把小雅绑定到TVBox上
- 编辑格式是http://<小雅IP地址>:5678

***tv.txt***
在/xiaoya目录下`vi tv.txt`编辑小雅自定义直播源
[tv.txt](joplin://c712f0dc70884c97af2c697c6e4f7cc5)

***alist_auth_token.txt***
在/xiaoya目录下`touch alist_auth_token.txt`

- 这个是自动生成Alist挂载小雅的令牌的,空文件就可以

***alist_list.txt***
在/xiaoya目录下`vi alist_list.txt`编辑套娃多个Alist资源库
 [alist_list.txt](alist_list.txt) 

***alishare_list.txt***
在/xiaoya目录下`vi alishare_list.txt`挂载别人分享的网盘
[alishare_list.txt](joplin://0ebb45282ef849ad80c2cb9879f93936)

***pikpakshare_list.txt***
在/xiaoya目录下`vi pikpakshare_list.txt`挂载自己一个或多个 pikpak分享
[pikpakshare_list.txt](joplin://4c050189edd943f8b3c6646c51643088)

***注：全部设置好后需要重启小雅Docker容器！***

**登陆方式**

- 登陆地址
  - <自己电脑IP地址>:5678
- 默认登陆账号密码
  - 账号：guest
  - 密码：guest_Api789
- 强制登陆账号密码
  - 账号：dav
  - 密码：***自己设置的密码***

#### Alist：

**一键部署命令：**

- ```shell
  docker run -d --restart=always -v /etc/alist:/opt/alist/data -p 5244:5244 -e PUID=0 -e PGID=0 -e UMASK=022 --name="alist" xhofe/alist:latest
  ```

- 修改密码命令：`docker exec -it alist ./alist admin set NEW_PASSWORD`（把NEW_PASSWORD改成你自己想要的密码）

- 输入：http://<自己电脑IP地址>:5244进入Alist登陆界面

- 默认账号：admin

- 密码：上面刚设置的

#### 小雅全自动清理机器人：

**一键部署命令：**

- ```
  bash -c "$(curl -s https://xiaoyahelper.zengge99.eu.org/aliyun_clear.sh | tail -n +2)" -s 5
  ```

#### DDNS-GO：

<u>这是一款动态域名解析服务提供商，专门为用户提供动态 IP 地址下的域名解析服务。</u>

**一键部署命令：**

- ````
  docker run -d --name ddns-go --restart=always --net=host -v /opt/ddns-go:/root jeessy/ddns-go
  ````

**ddns-go配置**

- 输入：http://<自己电脑IP地址>:9876进入到ddns配置页面

- 服务商选择：Cloudflare
- token选择：打开Cloudflare官网-->右上角我的个人资料-->{}API个人令牌-->如果现实无API令牌就点创建令牌-->编辑区域DNS(使用模版)-->区域资源最后一个选择（自己想要绑定的域名）-->拉到最下面选择（继续以显示摘要）-->创建令牌-->Copy前面那一串就是令牌了-->点Copy-->粘贴到ddns-go配置界面的token就可以了
- IPv4下面的Domains：输入刚刚创建令牌时候选择的那个域名
- 保存

#### Sun-Panel

<u>这是一款方便管理链接的导航栏。</u>

**一键部署命令：**

- ```
  docker run -d --restart=always -p 3002:3002 \
  -v /private/etc/sun-panel/conf:/app/conf \
  -v /private/etc/sun-panel/uploads:/app/uploads \
  -v /private/etc/sun-panel/database:/app/database \
  --name sun-panel \
  hslr/sun-panel
  
  ```
  
- 输入：http://<自己电脑IP地址>:3002进入到登陆页面

  默认密码： 

  账号：admin@sun.cc

  密码：12345678

#### HomeAssistant部署：

***创建homeassistant的安装目录:***

```
mkdir -p /private/etc/homeassistant
```

***一键安装命令:***

```
docker run -d --name=home-assistant -v /private/etc/homeassistant:/config -e TZ=Asia/Shanghai --net=host homeassistant/home-assistant

```

***`/private/etc/homeassistant`一键安装命令里面这一串就是安装在刚创建的文件夹里面】***

http://<自己电脑IP地址>:8123

- [下载HACS](https://github.com/hacs/integration/releases/tag/1.34.0)
- **安装HA需要魔法，如果没有魔法就看看就好！
- 在浏览器中打开 HACS GitHub 页面-->HACS GitHub Release在页面中找到最新版本的 HACS并下载-->下载完成后解压会出现HACS文件夹（里面还有一些文件）-->这个时候创建一个叫“custom_components”的文件夹，然后把刚刚解压出来的HACS文件夹放进custom_components的文件夹里面，以及再创建一个www名字的空文件夹，把“custom_components”和“www”两个文件夹放到/private/etc/homeassistant文件夹下
- 完成之后重启homeassistant容器
- 打开http://<自己电脑IP地址>:8123
- 右下角头像-->往下拉打开高级模式-->配置-->设备与服务-->添加集成-->输入HACS-->点HACS-->把所有选项打勾-->会弹出GitHub登陆界面-->还有验证码-->复制验证码-->登陆上去-->把验证码粘贴上去-->这样HACS就安装完成了-->重启homeassistant
- 登陆homeassistant-->点HACS-->输入xiaomi-->选择xiaomi Miot Auto-->Download-->Download
- 配置-->添加集成-->输入xiaomi Miot Auto-->账号即成-->输入账号密码提交-->包含-->选择自己的智能设备-->
- 

***桥接homekit***

- 配置-->设备与服务-->添加集成-->输入apple-->点apple-->选择homekit Bridge

- command+空格-->输入/private/etc/homeassistant进入到homeassistant文件夹

- 打开 configuration.yaml文件-->在最下面一行添加`homekit: !include homekit.yaml`

- 创建一个homekit.yaml-->打开这个文件，把下面的命令复制粘贴进去

- ```
  homekit:
    - filter:
        include_domains:
          - alarm_control_panel
          - light
          - media_player
        include_entity_globs:
          - binary_sensor.*_occupancy
        include_entities:
          - binary_sensor.living_room_motion
          - 这里输入你的实体ID
          - 这里输入你的实体ID
          - 这里输入你的实体ID
          - 这里输入你的实体ID
      entity_config:
        alarm_control_panel.home:
          code: 1234
        binary_sensor.living_room_motion:
          linked_battery_sensor: sensor.living_room_motion_battery
          low_battery_threshold: 31
        light.kitchen_table:
          name: Kitchen Table Light
        lock.front_door:
          code: 1234
        media_player.living_room:
          feature_list:
            - feature: on_off
            - feature: play_pause
            - feature: play_stop
            - feature: toggle_mute
        switch.bedroom_outlet:
          type: outlet
        camera.back_porch:
          support_audio: True
    - name: HASS Bridge 2
      port: 21065
      filter:
        include_domains:
          - light
  
  ```

- 把“这里输入你的实体ID”换成你homeassistant的实体ID保存-->重启homeassistant-->这个时候右下角就有了一个通知是一个二维码-->拿出你的iphone-->打开家庭-->添加设备-->扫码就ok了

- 目前我添加不了，但是我能确定不是操作的原因，应该是我家里网络的原因，所以各位可以自己试试！

### MAMP可通过HomgBrew下载安装

- 一键安装命令：`brew install mamp`

### WordPress只能通过官网手动下载

- [官方手动下载](https://wordpress.org/download/)

#### 使用方法：

- 打开MAMP软件（MAMP PRO是收费的，不用管它）-->Preferences-->Start servers(这个是开机自启动)打勾-->Server-->Open in Finder-->会打开MAMP的htdocs文件夹，把WordPress解压出来的文件夹拖进去，关掉窗口-->OK
- 打开MAMP服务：MAMP主界面右上角的“Start”是开启服务
- 开浏览器输入：http://localhost:8888/MAMP/
- 右上角Tools-->phpMyAdmin-->（上面导航栏）数据库-->数据库名：wordpress-->创建
- 打开浏览器输入：http://localhost:8888/wordpress/
- 现在就开始！-->数据库名：wordpress-->用户名-->root-->密码：root-->数据库主机：localhost或者127.0.0.1-->表前缀：wp_-->提交
- 现在安装-->站点标题:（随意）-->用户名:（自己设置）-->密码:（自己设置）-->电子邮箱:（随意）-->安装wordpress-->登录-->用户名密码（都是刚刚设置的）-->登录-->完成
- **注册登录界面**开浏览器输入：http://localhost:8888/wordpress/wp-admin/
- http://<自己电脑IP地址>:8888/wordpress

**当作个人网盘使用技巧：**

把自己的文件上传上去当作自己的无限大网盘使用：

- 在htdocs目录下创建一个作为网盘的文件夹(名字看各人喜好，我起个简单的名字：wenjian)：`mkdir -p /Applications/MAMP/htdocs/wenjian`

- 这个时候就可以往这个文件夹里面放自己的文件了

- 打开浏览器输入：`http://<自己电脑IP地址>:8888/wenjian/`就可以看到刚刚放进去的文件了，点文件就可以自动下载了

- 加密这个文件夹，自己的私人网盘不能让谁都可以访问：

- 进入到要加密的文件夹中：`cd /Applications/MAMP/htdocs/wenjian`

- 创建一个.htaccess的文件：`touch .htaccess`

- 编辑这个文件：`vi .htaccess`

- 复制粘贴一下内容：

- ```
  AuthType Basic
  AuthName "Restricted Area"
  AuthUserFile "/Applications/MAMP/conf/.htpasswd"
  Require valid-user
  ```

- 按ESC+:wq保存

  创建账号密码：`sudo htpasswd -c /Applications/MAMP/conf/.htpasswd username`把username改成自己的用户名(看个人喜好)

  输入好后会提示输入两遍密码（这就是个人网盘的密码）

  第一个密码是你登陆你mac的密码，后面两个才是文件夹的密码，后面两个要一致！

- 重启Apache 服务器：`sudo /Applications/MAMP/bin/apache2/bin/apachectl restart`

- 好的，恭喜你，你的个人网盘已经创建好了(建议不要将重要文件存在里面，还有就是把账号密码设置复杂些)

- http://<自己电脑IP地址>:8888/wenjian

### CloudDrive2（把网盘挂在到本地）：推荐（非必要）

<u>这是一款把网盘映射到本地的工具</u>

**安装fuse**

- [macFUSE](https://osxfuse.github.io/)

- **注意：**安装的时候需要设置-->隐私与安全性-->有一个什么扩展要打开（打开需要关机-->长按开机键-->选项-->。。。。设置完重启，就可以出现了）

  

**clouddrive2**

- 根据架构选择软件， [clouddrive2](http://www.clouddrive2.com/download.html)

- 安装目录：/opt/homebrew/Cellar/CloudDrive2/clouddrive

  - 后台启动命令：nohup /opt/homebrew/Cellar/CloudDrive2/clouddrive &
  - 列出了所有包含 "clouddrive" 字符串的进程：`ps aux | grep clouddrive`
  - 关闭clouddrive：`kill 14389`（14389是clouddrive的进程id，根据各人情况）
- 
- 输入：http://<自己电脑IP地址>:19798进入到CloudDrive配置页面
- 登陆界面：
  - Email：自己注册
  - 密码：自己注册

- 登陆进去之后开始挂在网盘-->点电脑图标-->挂载点（选择）-->Users-->mydong-->选中-->挂载

