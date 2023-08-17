<script setup>
import {ref} from 'vue'

let isLight = ref(false)

let yuqueHomeHref = "https://www.yuque.com/xlu103";

function changeLight() {
  isLight = !isLight;
  console.log(isLight)
}

function toYuque() {
  window.location.href = yuqueHomeHref;
}

let picPrefix = "/src/assets/images/"
let blogList = [{
  pic: "互联网资源合集.png",
  title: "互联网资源合集",
  href: "https://www.yuque.com/xlu103/re",
  detail: "这里汇聚了互联网上许多高质量的内容和工具,包括:\n" +
      "● 📚 优质电子书资源\n" +
      "● 🌟 个人成长类学习资料\n" +
      "● 💡 创业和职场相关内容\n" +
      "● 🧰 实用工具和生产力软件\n" +
      "● 🎨 设计和创意灵感来源\n" +
      "● 🔎 学术和技术资料\n" +
      "这些资源原本散落在互联网的不同角落,我花时间搜集和整理,舍弃劣质内容,保留精华。\n" +
      "就像海滩上的贝壳,我希望把它们收集起来,免得这些宝贝被大海冲走。我会不断更新和完善这个合集,欢迎你经常来逛逛,挖掘有用的资源宝石。"
}]

function getBlogList() {
  blogList.forEach(item => {
    // item.detail = item.detail.replace("\n", "<br/>")
  })
  console.log(blogList)
  return blogList;
}
</script>

<template>
  <div v-bind:class="{'light-theme':isLight,'dark-theme':!isLight}">
    <header>
      <div class="container">
        <nav class="navbar">
          <a href="#">
            <img src="./assets/images/logo-light.svg"
                 v-if="isLight"
                 alt="X Blog 的 Logo"
                 width="150"
                 height="40"
                 class="logo-light">
            <img src="./assets/images/logo-dark.svg"
                 v-else
                 alt="X Blog 的 Logo"
                 width="150"
                 height="40"
                 class="logo-dark">
          </a>

          <div class="btn-group">
            <button class="theme-btn theme-btn-mobile light">
              <ion-icon name="moon"
                        class="moon"></ion-icon>
              <ion-icon name="sunny"
                        class="sun"></ion-icon>
            </button>

            <button class="nav-menu-btn">
              <ion-icon name="menu-outline"></ion-icon>
            </button>

          </div>

          <div class="flex-wrapper">

            <ul class="desktop-nav">

              <li>
                <a href="#"
                   class="nav-link">主页</a>
              </li>
              <li>
                <a href="#"
                   class="nav-link">关于我</a>
              </li>
              <li>
                <a href="#"
                   class="nav-link">联系我</a>
              </li>
            </ul>

            <button class="theme-btn theme-btn-desktop "
                    :class="{'light':isLight,'dark':!isLight}"
                    @click="changeLight">
              <ion-icon name="moon"
                        class="moon"></ion-icon>
              <ion-icon name="sunny"
                        class="sun"></ion-icon>
            </button>

          </div>

          <div class="mobile-nav">
            <button class="nav-close-btn">
              <ion-icon name="close-outline"></ion-icon>
            </button>

            <div class="wrapper">

              <p class="h3 nav-title">主菜单</p>

              <ul>
                <li class="nav-item">
                  <a href="#"
                     class="nav-link">主页</a>
                </li>

                <li class="nav-item">
                  <a href="#"
                     class="nav-link">关于我</a>
                </li>

                <li class="nav-item">
                  <a href="#"
                     class="nav-link">联系我</a>
                </li>
              </ul>

            </div>

          </div>

        </nav>

      </div>

    </header>
    <main>
      <div class="hero">

        <div class="container">

          <div class="left">

            <h1 class="h1">
              Hi, I'm <b>Xlu&nbsp;Stout</b>.
              <br>28线 程序员
            </h1>

            <p class="h3">
              会一点 <abbr title="Accessibility"> 编程 </abbr>
            </p>
            <div class="btn-group">
              <a href="#"
                 class="btn btn-primary">联系我</a>
              <a :href="yuqueHomeHref"
                 class="btn btn-secondary">关于我</a>
            </div>
          </div>
          <div class="right">
            <div class="pattern-bg"></div>
            <div class="img-box">
              <img src="./assets/images/avatar.png"
                   alt="Xlu Stout"
                   class="hero-img">
              <div class="shape shape-1"></div>
              <div class="shape shape-2"></div>
            </div>

          </div>

        </div>

      </div>


      <div class="main">

        <div class="container">

          <!--
        - BLOG SECTION
      -->
          <div class="blog">
            <h2 class="h2">我的一些知识库</h2>
            <div class="blog-card-group">
              <div class="blog-card"
                   v-for=" item in getBlogList()">
                <div class="blog-card-banner">
                  <img :src="picPrefix+item.pic"
                       alt="Building microservices with Dropwizard, MongoDB & Docker"
                       width="250"
                       class="blog-banner-img">
                </div>
                <div class="blog-content-wrapper">
                  <!--<button class="blog-topic text-tiny">直链</button>-->
                  <h3>
                    <a :href="item.href"
                       class="h3">
                      {{ item.title }}
                    </a>
                  </h3>
                  <span class="blog-text">

                    {{ item.detail }}
                  </span>
                </div>
              </div>
            </div>


            <button class="btn load-more"
                    @click="toYuque">查看更多
            </button>

          </div>


          <div class="aside">


            <div class="contact">

              <h2 class="h2">找到我</h2>

              <div class="wrapper">

                <p>
                  欢迎尬聊（如果你想的话）
                </p>

                <ul class="social-link">

                  <li>
                    <a href="#"
                       class="icon-box discord">
                      <ion-icon name="logo-discord"></ion-icon>
                    </a>
                  </li>

                  <li>
                    <a href="#"
                       class="icon-box twitter">
                      <ion-icon name="logo-twitter"></ion-icon>
                    </a>
                  </li>

                  <li>
                    <a href="#"
                       class="icon-box facebook">
                      <ion-icon name="logo-facebook"></ion-icon>
                    </a>
                  </li>

                </ul>

              </div>

            </div>
          </div>
        </div>
      </div>
    </main>

    <footer>
      <div class="container">
        <div class="wrapper">
          <a href="#"
             class="footer-logo">
            <img src="./assets/images/logo-light.svg"
                 alt="DevBlog's Logo"
                 width="150"
                 height="40"
                 class="logo-light">
            <img src="./assets/images/logo-dark.svg"
                 alt="DevBlog's Logo"
                 width="150"
                 height="40"
                 class="logo-dark">
          </a>

          <p class="footer-text">
            😒 及 时 行 乐 是 一 场 瘟 疫
          </p>

        </div>

        <div class="wrapper">

          <p class="footer-title"> 直 链 </p>
          <ul>

            <li>
              <a :href="yuqueHomeHref"
                 class="footer-link">关于我</a>
            </li>
            <li>
              <a href="#"
                 class="footer-link">联系我</a>
            </li>

          </ul>

        </div>

        <div class="wrapper">

          <p class="footer-title">Legal Stuff</p>

          <ul>

            <li>
              <a href="#"
                 class="footer-link">Privacy Notice</a>
            </li>

            <li>
              <a href="#"
                 class="footer-link">Cookie Policy</a>
            </li>

            <li>
              <a href="#"
                 class="footer-link">Terms Of Use</a>
            </li>

          </ul>

        </div>

      </div>

      <p class="copyright">
        &copy; Copyright 2023 <a href="#">xlu stout</a>
      </p>

    </footer>

  </div>
</template>

<style scoped>


</style>
