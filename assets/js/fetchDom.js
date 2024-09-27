// 使用 fetch API 获取网页内容
async function fetchYuqueDoc() {
  const url = 'https://www.yuque.com/xlu103/re/qkxru83yf80cyhez?singleDoc';
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP 错误! 状态: ${response.status}`);
    }
    const html = await response.text();
    console.log('获取到的网页内容:', html);
  } catch (error) {
    console.error('获取文档时出错:', error);
  }
}

// 调用函数
fetchYuqueDoc();