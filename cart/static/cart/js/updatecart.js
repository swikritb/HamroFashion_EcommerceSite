var updateBtn = document.getElementById("updateCart");

updateBtn.addEventListener("click", function () {
  var req = new Request(updateCartUrl, {
    headers: {
      "X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken")[0].value,
    },
  });
  var data = createJson();
  fetch(req, { method: "post", body: JSON.stringify(data) })
    .then((resp) => resp.json())
    .then((data) => {
      console.log(data);
      window.location.reload();
    });
});

function createJson() {
  var dataTags = document.getElementsByClassName("data__tag");
  var quantityTags = document.getElementsByClassName("quantity");
  var data = [];
  for (let i = 0; i < dataTags.length; i++) {
    try {
      data.push({ [dataTags[i].dataset.cid]: quantityTags[i].innerText });
    } catch (e) {}
  }
  return data;
}
