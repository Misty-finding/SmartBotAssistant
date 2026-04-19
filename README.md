## 一、项目总体概述

![image-20260419201128938](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419201128938.png)

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

![image-20260419201833062](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419201833062.png)



1.绝对路径工具  返回绝对路径

2.日志工具  logger-handler







## 三、配置工具  文件工具  提示词加载工具

![image-20260419211022962](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419211022962.png)![image-20260419211036514](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419211036514.png)





### 配置工具：  从yml文件中读取   提供配置文件的路径

![image-20260419211622732](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419211622732.png)

### 文件工具：   上传一个文件路径  返回一个文件的哈希值

#### 获取文件md5  （哈希)   

![image-20260419212550734](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419212550734.png)

#### 获取允许文件列表：   上传一个文件夹（路径）  和允许的文件类型（元组）  返回文件夹中允许的文件（列表）

![image-20260419212620037](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419212620037.png)



#### pdf txt加载工具  -- 使用langchain自带   返回列表[Documents]

![image-20260419212825635](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419212825635.png)

![image-20260419212751093](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419212751093.png)

### 提示词工具-- prompt_loader-- 返回提示词（字符串）

![image-20260419214109508](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419214109508.png)

![image-20260419214218566](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419214218566.png)



## 四、RAG向量存储服务开发

![image-20260419215349746](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419215349746.png)

实现四个   两个成员变量：vector_store,spliter    两个成员方法  load_document,get_retriever



### 对于使用的大模型  采用工厂模式  

![image-20260419222337798](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419222337798.png)

### vector_store,spliter

![image-20260419222726082](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419222726082.png)

### get_retriever

![image-20260419222827443](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419222827443.png)

### load_document  ：读取知识库文件夹中的文件，切分后转成向量，存入向量库

#### 		两个字符串md5功能函数   防止重复加载知识文件

![image-20260419223054715](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419223054715.png)

####   文档读取函数  返回langchain的Document（列表）

![image-20260419223250503](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419223250503.png)

#### 获取所有符合格式的文件（*路径*）

![image-20260419223414140](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419223414140.png)

#### 遍历处理每一个文件存入向量库（上面得到的）

获取md5检查是否处理过-->检查是否有有效文本-->分片（使用成员变量spilter）-->检查是否有效分片-->存入向量库



## 五、RAG总结服务开发--rag检索到相关资料之后-->让模型总结一下 再返回

![image-20260419224533348](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419224533348.png)



![image-20260419225819177](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419225819177.png)

![image-20260419225842993](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419225842993.png)



测试：
![image-20260419225852943](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419225852943.png)

结果：
![image-20260419225926207](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419225926207.png)

![image-20260419225933820](C:\Users\23148\AppData\Roaming\Typora\typora-user-images\image-20260419225933820.png)

返回的类型实际上是langchain的message   也就是说模型回答了问题



