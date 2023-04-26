$(document).ready(function () {
    $("#stars li")
      .on("mouseover", function () {
        var onStar = parseInt($(this).data("value"), 10);

        $(this)
          .parent()
          .children("li.star")
          .each(function (e) {
            if (e < onStar) {
              $(this).addClass("hover");
            } else {
              $(this).removeClass("hover");
            }
          });
      })
      .on("mouseout", function () {
        $(this)
          .parent()
          .children("li.star")
          .each(function (e) {
            $(this).removeClass("hover");
          });
      });

    $("#stars li").on("click", function () {
      var onStar = parseInt($(this).data("value"), 10);
      var stars = $(this).parent().children("li.star");

      for (i = 0; i < stars.length; i++) {
        $(stars[i]).removeClass("selected");
        $(stars[i]).removeClass("selected-all");
      }

      if (onStar == $("#stars li").length) {
        for (i = 0; i < onStar; i++) {
          $(stars[i]).addClass("selected-all");
        }
      } else {
        for (i = 0; i < onStar; i++) {
          $(stars[i]).addClass("selected");
        }
      }

      if (onStar == 1) {
        $(stars[0]).addClass("first");
      } else {
        $(stars[0]).removeClass("first");
      }
    });
  });

  $("li").click(function () {
    var a = $(this).attr("value");
    $("#star").val(a);
  });