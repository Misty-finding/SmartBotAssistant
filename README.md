## 一、项目总体概述

![](typora_images/image-20260419201128938.png)

1、Rag工具  作为Agent的一个工具（rag_service)
rag检索到相关资料之后-->让模型总结一下 再返回  rag_summarize

rag作为agent的工具  agent可以选择不使用

2.中间件：

监控工具

模型之前日志记录

report_prompt_switch  ：动态切换提示词

3.工具 六个def

4.前端streamlit

5.第三方工具  utils



## 二、日志和路径工具开发  --基础工具

![](typora_images/image-20260419201833062.png)



1.绝对路径工具  返回绝对路径

2.日志工具  logger-handler



## 三、配置工具  文件工具  提示词加载工具

![](typora_images/image-20260419211022962.png)![image-20260419211036514](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419211036514.png)





### 配置工具：  从yml文件中读取   提供配置文件的路径

![](typora_images/image-20260419211622732.png)

### 文件工具：   上传一个文件路径  返回一个文件的哈希值

#### 获取文件md5  （哈希)   

![](typora_images/image-20260419212550734.png)

#### 获取允许文件列表：   上传一个文件夹（路径）  和允许的文件类型（元组）  返回文件夹中允许的文件（列表）

![](typora_images/image-20260419212620037.png)



#### pdf txt加载工具  -- 使用langchain自带   返回列表[Documents]

![](typora_images/image-20260419212825635.png)

![](typora_images/image-20260419212751093.png)

### 提示词工具-- prompt_loader-- 返回提示词（字符串）

![](typora_images/image-20260419214109508.png)

![](typora_images/image-20260419214218566.png)



## 四、RAG向量存储服务开发

![](typora_images/image-20260419215349746.png)

实现四个   两个成员变量：vector_store,spliter    两个成员方法  load_document,get_retriever



### 对于使用的大模型  采用工厂模式  

![](typora_images/image-20260419222337798.png)

### vector_store,spliter

![](typora_images/image-20260419222726082.png)

### get_retriever

![](typora_images/image-20260419222827443.png)

### load_document  ：读取知识库文件夹中的文件，切分后转成向量，存入向量库

#### 		两个字符串md5功能函数   防止重复加载知识文件

![](typora_images/image-20260419223054715.png)

####   文档读取函数  返回langchain的Document（列表）

![](typora_images/image-20260419223250503.png)

#### 获取所有符合格式的文件（*路径*）

![](typora_images/image-20260419223414140.png)

#### 遍历处理每一个文件存入向量库（上面得到的）

获取md5检查是否处理过-->检查是否有有效文本-->分片（使用成员变量spilter）-->检查是否有效分片-->存入向量库



## 五、RAG总结服务开发--rag检索到相关资料之后-->让模型总结一下 再返回

![](typora_images/image-20260419224533348.png)



![](typora_images/image-20260419225819177.png)

![](typora_images/image-20260419225842993.png)



测试：
![](typora_images/image-20260419225852943.png)

结果：
![](typora_images/image-20260419225926207.png)

![](typora_images/image-20260419225933820.png)

返回的类型实际上是langchain的message   也就是说模型回答了问题

## 六、tools工具开发

![](typora_images/image-20260420110624295.png)



引入rag服务  注册为工具 @tool

![](typora_images/image-20260420113809750.png)



获取时间天气等等  都注册为工具

![](typora_images/image-20260420113828207.png)





## 七、中间件和智能体Agent构建

### 中间件开发：

![](typora_images/image-20260420124740927.png)

类似java的AOP

```
@wrap_tool_call
@before_model
@dynamic_prompt
```

#### 监视工具： 每次调用tool工具都会被监控到

![](typora_images/image-20260420121654900.png)

![](typora_images/image-20260420122754787.png)

#### 动态提示词工具  ：可以根据监控时 是否注入report  来选择提示词模板

![](typora_images/image-20260420121722547.png)

#### 调用模型之前 写点日志

![](typora_images/image-20260420121711508.png)



### agent构建： react_agent开发

定义ReacrAgent类

装载上模型  系统提示词   工具  中间件

![](typora_images/image-20260420124535421.png)

定义执行函数（流式输出）
![](typora_images/image-20260420124602677.png)

![](typora_images/image-20260420124908243.png)

![](typora_images/image-20260420124924353.png)



agent如何实现的react的  就是如何思考  调用工具  再思考 ？

![](typora_images/image-20260420130522800.png)