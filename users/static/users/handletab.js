let tabs = document.getElementsByClassName("selector");

[...tabs].forEach((tab) => {
  tab.addEventListener("click", function (event) {
    event.stopPropagation();
    //removing the active class if it has
    [...document.getElementsByClassName("active")].forEach(function (element) {
      element.classList.remove("active");
    });

    //adding the tactive class in targer and the clicked button

    document
      .getElementsByClassName(this.dataset.target)[0]
      .classList.add("active");
    this.classList.add("active");
  });
});
