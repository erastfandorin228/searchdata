$(function () {

    // плавное перемещение страницы к нужному блоку
    $("a.go, a.menu__link").click(function (e) {
        e.preventDefault();
        elementClick = $(this).attr("href");
        destination = $(elementClick).offset().top;
        $("body,html").animate({scrollTop: destination }, 800);
    });
    
});
