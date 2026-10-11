---
# 语言 （可选）
lang: zh-cn
# 网页关键词和描述
keywords: 于兆海,简历
description: 男，已婚已育；13年入行iOS开发，有丰富的独立开发&上架经验；热爱开发，甚于游戏.....
# 简历标题
resume_title: 于兆海的简历
# 应聘者姓名
name: 于兆海
avatar: /avatar.png
# 联系方式
contact:
  - icon: fas fa-globe-asia
    text: yuzhaohai.github.io
    url: https://yuzhaohai.github.io
  # 邮箱
  - icon: fas fa-envelope
    text: yuzhaohai@126.com
    url: mailto:yuzhaohai@126.com
  # 电话号码
  - icon: fas fa-phone-alt
    text: 15253913919
    url: tel:15253913919
---

{% raw %}
<center>
<a href='/en/'>English</a> | <a href='/'>简体中文</a>
</center>
{% endraw %}



## <i class="fas fa-user-graduate"></i> 教育背景

**09.09-13.07  临沂大学  信息学院    网络工程专业**
**12.07-12.11  青软实训  Java开发**
**12.11-13.09  青软实训  iOS开发**


## <i class="fas fa-user-tie"></i> 工作经验


2024年 ~ 至今：自由职业
2021年 ~ 2024年：临沂敏捷软件有限公司
2019年 ~ 2021年：山东来客网络科技有限公司
2018年 ~ 2019年：山东青迈智能科技有限公司
2017年 ~ 2018年：山东影响力智能科技有限公司
2016年 ~ 2017年：临沂冠科软件有限公司
2013年 ~ 2016年：上海三知数码科技有限公司
2012年 ~ 2013年：上海虎扑体育


## <i class="fas fa-award"></i> 精选项目


2013年入行，项目经验近百，涵盖社交、音视频、健身、工具、电商等多种类型；但时间久远，有些项目已经下架、有些项目并未上架......下面是尚在线中比较典型的，敬请查看。

{% raw %}
<btns rounded>
<a href='https://apps.apple.com/cn/app/id6777906127'>
  <img src='https://pic1.imgdb.cn/i/034deQ8UzFTcW4ONwlArD5.jpg'>
  意练
</a>
<a href='https://apps.apple.com/cn/app/id1593385233'>
  <img src='https://pic1.imgdb.cn/i/034deUH5FiDD4PSQeLCVQq.png'>
  WeListen
</a>
<a href='https://apps.apple.com/cn/app/id1568224803'>
  <img src='https://pic1.imgdb.cn/i/034denDeq8OGf2dfccarwB.png'>
  趣海钓
</a>
<a href='https://apps.apple.com/cn/app/id1448000712'>
  <img src='https://pic1.imgdb.cn/i/034des5ldiHOO4bv4928uA.png'>
  中付掌柜
</a>
<a href='https://apps.apple.com/cn/app/id1438587731'>
  <img src='https://pic1.imgdb.cn/i/034df6lplDmdWWSYAXwsaN.jpg'>
  安居公社
</a>
<a href='https://apps.apple.com/cn/app/id1242756510'>
  <img src='https://pic1.imgdb.cn/i/034df6lvPXM49YKV61eCTZ.jpg'>
  百货商家端
</a>
<a href='https://apps.apple.com/cn/app/id906632439'>
  <img src='https://pic1.imgdb.cn/i/034df6ljQH5LUzWxxfcchw.jpg'>
  虎扑
</a>
</btns><br>
{% endraw %}

## <i class="fas fa-code"></i> 代码技能

| 技能  | 熟练度  |
| :------------ | :------------ |
| Objective-C  |  精通 |
| Swift  | 熟练  |
|React Native|掌握|
|Flutter|掌握|
|Java|掌握|
|Python|掌握|
|Go|掌握|
|Vue|熟悉|
|React|熟悉|

## <i class="fas fa-phone-alt"></i> 与我联系

目前状态为：自由职业。

{% raw %}
<style>
.contact-link{cursor:pointer;color:#2196f3;}
.contact-link:hover{text-decoration:underline;}
#contact-modal-mask{display:none;position:fixed;z-index:9999;inset:0;background:rgba(0,0,0,.45);}
#contact-modal{position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);background:#fff;border-radius:12px;padding:20px 24px;min-width:260px;box-shadow:0 8px 30px rgba(0,0,0,.2);text-align:center;}
#contact-modal .cm-value{font-size:16px;font-weight:600;margin-bottom:16px;word-break:break-all;color:#333;}
#contact-modal .cm-btns{display:flex;gap:10px;justify-content:center;}
#contact-modal .cm-btns a,#contact-modal .cm-btns button{flex:1;padding:8px 0;border-radius:8px;border:1px solid #ddd;background:#f5f5f5;color:#333;font-size:14px;cursor:pointer;text-decoration:none;line-height:1.5;}
#contact-modal .cm-btns a:hover{text-decoration:none;}
#contact-modal .cm-btns .cm-primary{background:#2196f3;border-color:#2196f3;color:#fff;}
</style>
<span class="contact-link" onclick="openContactModal('yuzhaohai@126.com','mailto:yuzhaohai@126.com','写信')"><i class="fas fa-envelope fa-fw"></i> yuzhaohai@126.com</span><br><br>
<span class="contact-link" onclick="openContactModal('15253913919','tel:15253913919','拨号')"><i class="fas fa-phone-alt fa-fw"></i> 15253913919</span>
<div id="contact-modal-mask" onclick="if(event.target===this)closeContactModal()">
  <div id="contact-modal">
    <div class="cm-value" id="cm-value"></div>
    <div class="cm-btns">
      <button onclick="copyContactValue()">复制</button>
      <a id="cm-action" class="cm-primary" href="javascript:void(0)"></a>
      <button onclick="closeContactModal()">取消</button>
    </div>
  </div>
</div>
<script>
var cmCurrentValue='';
function openContactModal(value,url,actionText){
  cmCurrentValue=value;
  document.getElementById('cm-value').textContent=value;
  var a=document.getElementById('cm-action');
  a.textContent=actionText;a.href=url;
  document.getElementById('contact-modal-mask').style.display='block';
}
function closeContactModal(){document.getElementById('contact-modal-mask').style.display='none';}
function copyContactValue(){
  if(navigator.clipboard&&navigator.clipboard.writeText){
    navigator.clipboard.writeText(cmCurrentValue).then(cmCopied,cmFallbackCopy);
  }else{cmFallbackCopy();}
}
function cmFallbackCopy(){
  var ta=document.createElement('textarea');ta.value=cmCurrentValue;document.body.appendChild(ta);ta.select();
  try{document.execCommand('copy');cmCopied();}catch(e){}
  document.body.removeChild(ta);
}
function cmCopied(){
  var btn=document.querySelector('#contact-modal .cm-btns button');
  btn.textContent='已复制';setTimeout(function(){btn.textContent='复制';closeContactModal();},800);
}
</script>
{% endraw %}


## <i class="fas fa-flag"></i> 个人探索

[个人博客](https://yuzhaohai.github.io/blog/)<br>
[JSON 树视图](https://yuzhaohai.github.io/html/awsome/json-tree.html)<br>
