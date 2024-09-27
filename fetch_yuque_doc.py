import requests
from bs4 import BeautifulSoup
import json
import os
import re


def fetch_yuque_doc():
    url = 'https://www.yuque.com/xlu103/re/qkxru83yf80cyhez?singleDoc'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # 从 GitHub Actions 的 secrets 获取 cookie
        cookie = os.environ.get('YUQUE_COOKIE')
        if not cookie:
            print("错误:未能从 GitHub Actions 的 secrets 中获取 YUQUE_COOKIE")
            return
        
        headers['Cookie'] = cookie
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # 查找特定格式的链接
        link_pattern = r'https%3A%2F%2Fwww\.yuque\.com%2Fxlu103%2Frvt9mr%2F([a-zA-Z0-9]+)%22%2C%22'
        matches = soup.find_all(string=lambda text: text and re.search(link_pattern, text))
        
        文章列表 = []
        if matches:
            for match in matches:
                link_ids = re.findall(link_pattern, match)
                for link_id in link_ids:
                    完整链接 = f"https://www.yuque.com/xlu103/rvt9mr/{link_id}"
                    print(f"完整链接: {完整链接}")
                    文章列表.append(完整链接)
        else:
            print("未找到符合格式的链接")
        
        # 将文章列表存储到 JSON 文件中
        with open('yuque_doc.json', 'w', encoding='utf-8') as f:
            json.dump(文章列表, f, ensure_ascii=False, indent=2)
        print("文章列表已保存到 yuque_doc.json 文件中")
         
    
    except requests.RequestException as e:
        print(f"获取文档时出错: {e}")

if __name__ == "__main__":
    fetch_yuque_doc()