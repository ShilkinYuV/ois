function myFunction(){
	var selectedValue = $(".org").val();
	$.ajax({
		type: 'GET', // GET или POST
		url: "change_choice/",
		data: {
			selectedValue,
		}, 
		dataType: "text",
		cache: false,

        success: function(json) {
            if (json) {
                for (var source in json) {
                   $(".clnt").prepend("<option value='"+json[source].id+"'>"+json[source].FIO+"</option>");
                }

            }
            },
		  // если ошибка, то
		error: function (response) {
		    // предупредим об ошибке
		    alert(response.responseJSON.errors);
		    console.log(response.responseJSON.errors)
	  }
});

}
