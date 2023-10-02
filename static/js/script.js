const bookmarkIconImg = document.getElementById("bookmark_icon");

bookmarkIconImg.addEventListener("click", function() {
  if (bookmarkIconImg.src.endsWith("bookmark.png")) {
    bookmarkIconImg.src = "/static/img/bookmark-clicked.png";
  } else {
    bookmarkIconImg.src = "/static/img/bookmark.png";
  }
});