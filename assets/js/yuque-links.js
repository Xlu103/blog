const yuqueLinks = {
  about: 'https://www.yuque.com/xlu103',
  contact: 'https://www.yuque.com/xlu103/rvt9mr/gqv7lqfh7kae0gnr?singleDoc',
  homepage: 'https://www.yuque.com/xlu103'
};

// 更新页面中的语雀链接
function updateYuqueLinks() {
  const elements = document.querySelectorAll('[data-yuque-link]');
  elements.forEach(element => {
    const linkType = element.getAttribute('data-yuque-link');
    if (yuqueLinks[linkType]) {
      element.href = yuqueLinks[linkType];
    }
  });
}

// 当DOM加载完成后执行更新
document.addEventListener('DOMContentLoaded', updateYuqueLinks);