var removeButtons = document.getElementsByClassName("fa-remove");

for (let i = 0; i < removeButtons.length; i++) {
  var currButton = removeButtons[i];
  currButton.addEventListener("click", function () {
    var csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    var id = this.dataset.cid;
    var req = new Request(removeFromCartUrl, {
      headers: {
        "X-CSRFToken": csrfToken,
      },
    });
    fetch(req, {
      method: "post",
      body: JSON.stringify({ cart_item_id: id }),
    }).then((resp) => {
      window.location.reload();
    });
  });
}
