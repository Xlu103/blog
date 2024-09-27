function loadBlogCard() {
    const hero = document.getElementById('hero');
    const blogCardGroup = document.getElementById('blog-card-group');

    if (hero.getBoundingClientRect().top < window.innerHeight) {
        // 模拟加载新内容的延迟
        setTimeout(() => {
            blogCardGroup.classList.add('show');
            blogCardGroup.style.marginTop = "0";
            blogCardGroup.style.marginLeft = "0";
        }, 10);
    } else {
        setTimeout(() => {
            blogCardGroup.classList.remove('show');
            blogCardGroup.style.marginTop = "5vw";
            blogCardGroup.style.marginLeft = "5vw";
        }, 10);
    }
}

// 监听页面滚动事件
window.addEventListener('scroll', () => {
    loadBlogCard();
});
window.addEventListener('load', () => {
    loadBlogCard();
});


const hero = document.getElementById('img-box');
let isRotating = false;
let rotationX = 0;
let rotationY = 0;

hero.addEventListener('mouseenter', () => {
    isRotating = true;
    rotateHero();
});

hero.addEventListener('mouseleave', () => {
    isRotating = false;
    resetRotation();
});

hero.addEventListener('mousemove', (e) => {
    if (isRotating) {
        const rect = hero.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;
        rotationY = ((e.clientX - centerX) / rect.width) * 20;
        rotationX = ((e.clientY - centerY) / rect.height) * 20;
    }
});

function rotateHero() {
    if (isRotating) {
        hero.style.transform = `perspective(1000px) rotateX(${rotationX}deg) rotateY(${rotationY}deg)`;
        requestAnimationFrame(rotateHero);
    }
}

function resetRotation() {
    hero.style.transition = 'transform 0.5s ease-out';
    hero.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg)';
    setTimeout(() => {
        hero.style.transition = '';
    }, 500);
}



function typeWriter(text, element, speed) {
    let currentIndex = 0;
    const timer = setInterval(() => {
        element.textContent = text.slice(0, currentIndex) + "_";
        currentIndex++;
        if (currentIndex >= text.length) {
            clearInterval(timer);
            element.textContent = text;
        }
    }, speed);
}

const myNameElement = document.getElementById("my-name");
const myNameTest = "👋 Hi, I'm Xlu Stout 🫎"

// 只执行一次打字机效果
typeWriter(myNameTest, myNameElement, 100);


