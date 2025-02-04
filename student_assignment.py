from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    # 使用 PyPDFLoader 讀取 PDF 文本內容
    loader = PyPDFLoader(q1_pdf)
    documents = loader.load()
    
    # 使用 CharacterTextSplitter 將文本以頁為單位分割為多個 chunks
    text_splitter = CharacterTextSplitter(chunk_overlap=0)
    chunks = text_splitter.split_documents(documents)
   
    # 回傳最後一個 chunk 物件
    return chunks[-1]

def hw02_2(q2_pdf):
    # 使用 PyPDFLoader 讀取 PDF 文本內容
    loader = PyPDFLoader(q2_pdf)
    documents = loader.load()
    
    # 使用 CharacterTextSplitter 將文本以頁為單位分割為多個 chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0, separators=["\n\n", "\n"])
    chunks = text_splitter.split_documents(documents)
    
    # 回傳最後一個 chunk 物件
    return chunks[-1]

def hw02_2(q2_pdf):
    # 使用 PyPDFLoader 讀取 PDF 文本內容
    loader = PyPDFLoader(q2_pdf)
    documents = loader.load()
    
    # 使用 RecursiveCharacterTextSplitter 將文本分割為多個 chunks
    # 使用適當的分隔符號來將每一章和每一條分割成單獨的 chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0, separators=["章", "條","\n\n"])
    chunks = text_splitter.split_documents(documents)
    
    # 打印所有 chunks 的數量和每個 chunk 的簡要內容
    print(f"Total chunks: {len(chunks)}")
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}: {chunk.page_content[:100]}...")  # 打印前100個字符
    
    # 回傳得到的 chunks 數量
    return len(chunks)



# 測試 hw02_1 方法
last_chunk = hw02_1(q1_pdf)
print(last_chunk)

# 測試 hw02_2 方法
#chunks_count = hw02_2(q2_pdf)
#print(f"Total number of chunks: {chunks_count}")
