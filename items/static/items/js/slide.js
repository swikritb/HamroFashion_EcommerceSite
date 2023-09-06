const slides = document.querySelector(".slides").children;
const prev = document.querySelector(".prev");
const next = document.querySelector(".next");
const indicators = document.querySelector(".indicators");
let index = 0;

prev.addEventListener("click", () => {
  prevSlide();
});

next.addEventListener("click", () => {
  nextSlide();
});

function nextSlide() {
  if (index === slides.length - 1) {
    index = 0;
  } else {
    index++;
  }
  changeSlide();
}

function createCircle() {
  for (let i = 0; i < slides.length; i++) {
    const div = document.createElement("div");
    div.addEventListener("click", () => {
      index = i;
      changeSlide();
      clearInterval(changer);

      changer = setInterval(nextSlide, 5000);
    });
    if (i == index) {
      div.classList.add("active");
    }
    indicators.appendChild(div);
  }
}

createCircle();

function prevSlide() {
  if (index === 0) {
    index = slides.length - 1;
  } else {
    index--;
  }
  changeSlide();
}

function changeSlide() {
  for (let i = 0; i < slides.length; i++) {
    slides[i].classList.remove("active");
    indicators.children[i].classList.remove("active");
  }
  indicators.children[index].classList.add("active");
  slides[index].classList.add("active");
}

let changer = setInterval(nextSlide, 5000);
