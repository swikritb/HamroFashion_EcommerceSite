const imgs = document.getElementsByClassName("img-small");

for (let i = 0; i < imgs.length; i++) {
  currImg = imgs[i];
  currImg.addEventListener("click", function () {
    document.getElementById("dp").src = this.src;
    for (let j = 0; j < imgs.length; j++) {
      currImg = imgs[j];
      currImg.style.border = "0";
    }
    this.style.border = "1px solid orange";
  });
}
