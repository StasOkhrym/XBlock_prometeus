function SimpleXBlock(runtime, element) {
  function updateCount(result) {
    $(".count", element).text(result.count);
  }

  var handlerUrl = runtime.handlerUrl(element, "increment_count");

  $("p", element).click(function (eventObject) {
    $.ajax({
      type: "POST",
      url: handlerUrl,
      data: JSON.stringify({ hello: "world" }),
      success: updateCount,
    });
  });

  $(function ($) {
    var coll = document.getElementsByClassName("simplexblock_block");
    var i;

    for (i = 0; i < coll.length; i++) {
      coll[i].addEventListener("click", function () {
        this.classList.toggle("active");

        var content = this.nextElementSibling;

        if (content.style.display === "block") {
          content.style.display = "none";
        } else {
          content.style.display = "block";
        }
      });
    }
  });
}
