$(document).ready(function() {
    $("#add_item").click(function() {
        var listItem = $("<li>").text("Item");
        $("ul.my_list").append(listItem);
    });
});
