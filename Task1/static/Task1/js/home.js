


$(".user").on("click",(event)=>{

    $("#User-dropdown").slideToggle(500).toggleClass('show');
  

});

$(".s1").on("click",(event)=>{

    $("#sidemenu1").slideToggle(500).toggleClass('show');
  

});
$(".s2").on("click",(event)=>{

    $("#sidemenu2").slideToggle(500).toggleClass('show');
  

});
$(".s3").on("click",(event)=>{

    $("#sidemenu3").slideToggle(500).toggleClass('show');
  

});

    // Close the dropdown menu if the user clicks outside of it
 $(document).on("click", function(event) {
        if (!$(event.target).closest('.dropdown').length) {
          $(".dropdown-content").slideUp(500).removeClass('show');
        }
      });
 
$(".sidebar-button").on("click",(event)=>{

    $("#menu").slideToggle(500).toggleClass('show');

});
$(document).on("click", function(event) {
    if (!$(event.target).closest('.side-drop').length) {
      $(".sidedrop").slideUp(500).removeClass('show');
    }
  });



/*control side bar  */
$(document).ready(()=>{
    $(window).resize((event)=>{
        if ($(window).width() >= 500) {
            $("#menu").css("display", "block");
            $(".sidebar-button").hide();
        } else {
            $("#menu").css("display", "none");
            $(".sidebar-button").show();
        }
    });
});









// Handle delete functionality
// $(document).on('click', '.delete', function (e) {
//     e.preventDefault();
//     if (confirm('Are you sure you want to delete this row?')) {
//         var $row = $(this).closest('tr');

//         var rowId = $row.attr('row_id');
        

//         $row.remove();


//         userData.splice(rowId, 1);


//         console.log('Row deleted:', rowId);
//         console.log('Updated userData:', userData);
//     }
// });

