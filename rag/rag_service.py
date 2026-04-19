
"""
总结服务类：用户提问，搜索参考资料，将提问和参考资料提交给模型，让模型总结回复
"""
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from rag.vector_store import VectorStoreService
from utils.prompt_loader import load_rag_prompts
from langchain_core.prompts import PromptTemplate
from model.factory import chat_model


def print_prompt(prompt):
    print("="*20)
    print(prompt.to_string())
    print("="*20)
    return prompt


class RagSummarizeService(object):
    def __init__(self):
        self.vector_store = VectorStoreService() #vector_store类中的向量数据库
        self.retriever = self.vector_store.get_retriever() #向量库对象中，生成一个“检索器”
        self.prompt_text = load_rag_prompts()   #获得rag提示词
        self.prompt_template = PromptTemplate.from_template(self.prompt_text) #根据提示词创建提示词模板
        self.model = chat_model #获得模型 工厂模式
        self.chain = self._init_chain()  #获得链

    def _init_chain(self):  #返回构建的链
        chain = self.prompt_template | print_prompt | self.model | StrOutputParser()
        return chain

    def retriever_docs(self, query: str) -> list[Document]:  #先检索文档 获取document（langchain内置）
        return self.retriever.invoke(query)

    def rag_summarize(self, query: str) -> str:   #rag总结

        context_docs = self.retriever_docs(query) #先获取参考文档

        context = ""
        counter = 0
        for doc in context_docs:  #将参考资料拼接成字符串
            counter += 1
            context += f"【参考资料{counter}】: 参考资料：{doc.page_content} | 参考元数据：{doc.metadata}\n"

        return self.chain.invoke(   #把用户输入input，参考资料context给大模型  让模型总结后
            {
                "input": query,
                "context": context,
            }
        )


if __name__ == '__main__':
    rag = RagSummarizeService()
    res = rag.rag_summarize("小户型适合哪些扫地机器人")
    print(type(res))
    print(res)
