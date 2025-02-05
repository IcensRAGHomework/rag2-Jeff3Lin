
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter, RecursiveCharacterTextSplitter)
import re 
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
    """
    使用 PyPDFLoader 讀取 PDF 文本內容，
    將所有頁面內容合併，然後進行 Chunk 分割。
    """
    # 使用 PyPDFLoader 讀取 PDF 文本內容
    loader = PyPDFLoader(q2_pdf)
    documents = loader.load()

    # 1. 將所有頁面內容合併到一個字符串中
    full_text = ""
    for document in documents:
        full_text += document.page_content + "\n"

    chunks = []
    current_chunk = ""
    lines = full_text.splitlines()

    for line in lines:
        line = line.strip()  # 移除行首尾的空白字符
        if not line:  # 忽略空行
            continue

        # 判斷是否是章節或條款標題 (使用更嚴格的判斷)
        if re.match(r"^第\s*[一二三四五六七八九十]+\s*章\s*.*$", line) or re.match(r"^第\s*(100|[1-9][0-9]|[1-9])(\s*[-－]\s*\d+)?\s*條$", line):
            # 如果是章節或條款標題，則開始一個新的 chunk
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = line
        else:
            # 否則，將該行添加到當前 chunk 中
            current_chunk += "\n" + line

    # 處理最後一個 chunk
    if current_chunk:
        chunks.append(current_chunk.strip())

    # 合併第一章以前的內容
    first_chapter_index = -1
    for i, chunk in enumerate(chunks):
        if re.match(r"^第\s*一\s*章", chunk):
            first_chapter_index = i
            break

    if first_chapter_index > 0:
        first_part = "\n".join(chunks[:first_chapter_index])
        chunks = [first_part] + chunks[first_chapter_index:]

    # 打印分割結果 (或進行後續處理)
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}: {chunk}\n")

    return len(chunks)


# 測試 hw02_1 方法
last_chunk = hw02_1(q1_pdf)
print(last_chunk)

# 測試 hw02_2 方法
chunks_count = hw02_2(q2_pdf)
print(f"Total number of chunks: {chunks_count}")