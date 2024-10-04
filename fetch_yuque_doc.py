import requests
from bs4 import BeautifulSoup
import json
import os
import re
def fetch_yuque_doc():
    import random
    random_number = random.randint(1, 1000000)
    url = f'https://www.yuque.com/xlu103/re/qkxru83yf80cyhez?singleDoc&random={random_number}'
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
        print(soup)
        # 查找特定格式的链接
        link_pattern = r'https%3A%2F%2Fwww\.yuque\.com%2Fxlu103%2Frvt9mr%2F([a-zA-Z0-9]+)%22%2C%22'
        matches = soup.find_all(string=lambda text: text and re.search(link_pattern, text))
        
        article_list = []
        if matches:

            for match in matches:
            
                link_ids = re.findall(link_pattern, match)
                for link_id in link_ids:
                    full_link = f"https://www.yuque.com/xlu103/rvt9mr/{link_id}"
                    try:
                        # 访问完整链接,获取到 dom 中 id 为 article-title 的内容
                        response = requests.get(full_link, headers=headers)
                        response.raise_for_status()
                        
                        soup = BeautifulSoup(response.text, 'html.parser')
                        
                        # 获取文章标题
                        article_title = soup.find('meta', property='og:title')
                        if article_title:
                            article_title = article_title['content']
                        else:
                            raise ValueError("未找到文章标题")
                        
                        # 获取文章描述
                        article_description = soup.find('meta', property='og:description')
                        article_description = article_description['content'] if article_description else "无描述"
                        
                        # 获取文章URL
                        article_url = soup.find('meta', property='og:url')
                        article_url = article_url['content'] if article_url else full_link
                        
                        # 获取文章图片
                        article_image = soup.find('meta', property='og:image')
                        article_image = article_image['content'] if article_image else "无图片"
                        
                        # 获取文章创建时间
                        article_create_time = soup.find('meta', attrs={'name': 'weibo:article:create_at'})
                        article_create_time = article_create_time['content'] if article_create_time else "未知"
                        
                        # 获取文章更新时间
                        article_update_time = soup.find('meta', attrs={'name': 'weibo:article:update_at'})
                        article_update_time = article_update_time['content'] if article_update_time else "未知"
                        
                        article_data = {
                            "title": article_title,
                            "description": article_description,
                            "url": article_url,
                            "image": article_image,
                            "create_time": article_create_time,
                            "update_time": article_update_time,
                            "link": full_link
                        }
                        article_list.append(article_data)
                        print(f"已添加文章: {article_title}")
                    except requests.RequestException as e:
                        print(f"获取文章 {full_link} 时出错: {e}")
                    except ValueError as e:
                        print(f"处理文章 {full_link} 数据时出错: {e}")
                    except Exception as e:
                        print(f"处理文章 {full_link} 时发生未知错误: {e}")
        else:
            print("未找到符合格式的链接")
        
        # 将article_list存储到 JS 文件中
        with open('yuque_doc.js', 'w', encoding='utf-8') as f:
            f.write(f"const articleList = {json.dumps(article_list, ensure_ascii=False, indent=2)};")
        print("article_list已保存到 yuque_doc.js 文件中")
         
    
    except requests.RequestException as e:
        print(f"获取文档时出错: {e}")

if __name__ == "__main__":
    fetch_yuque_doc()