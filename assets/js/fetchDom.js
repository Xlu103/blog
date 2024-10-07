function generateArticleCards() {
  let articleCardGroup = document.querySelector("#article-card-group");
  // 遍历articleList并生成HTML卡片
  for (let article of articleList) {
    let articleCard = document.createElement("div");
    articleCard.className = "blog-card";

    let banner = document.createElement("div");
    banner.className = "blog-card-banner";
    let bannerImg = document.createElement("img");
    bannerImg.src = article.image;
    bannerImg.alt = article.title;
    bannerImg.width = "250";
    bannerImg.className = "blog-banner-img";
    banner.appendChild(bannerImg);
    articleCard.appendChild(banner);

    let contentWrapper = document.createElement("div");
    contentWrapper.className = "blog-content-wrapper";

    let titleLink = document.createElement("a");
    titleLink.href = article.url;
    titleLink.className = "h3";
    titleLink.textContent = article.title;
    let title = document.createElement("h3");
    title.appendChild(titleLink);
    contentWrapper.appendChild(title);

    let description = document.createElement("p");
    description.className = "blog-text";
    description.textContent = article.description;
    contentWrapper.appendChild(description);

    let wrapperFlex = document.createElement("div");
    wrapperFlex.className = "wrapper-flex";
    let wrapper = document.createElement("div");
    wrapper.className = "wrapper";
    let timeInfo = document.createElement("p");
    timeInfo.className = "text-sm";
    timeInfo.innerHTML = `
        <time datetime="${article.create_time}">创建时间: ${article.create_time}</time>
        <span class="separator"></span>
        <time datetime="${article.update_time}">更新时间: ${article.update_time}</time>
    `;
    wrapper.appendChild(timeInfo);
    wrapperFlex.appendChild(wrapper);
    contentWrapper.appendChild(wrapperFlex);

    articleCard.appendChild(contentWrapper);
    articleCardGroup.appendChild(articleCard);
  }
}

generateArticleCards();
 