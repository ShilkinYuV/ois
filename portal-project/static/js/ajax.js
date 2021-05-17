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
            		 $('.clnt').find('option').remove();
            	 var data = json;
 				 var dataObject = JSON.parse(data);
                for (var source in dataObject) {
                   $(".clnt").prepend("<option value='"+dataObject[source].id+"'>"+dataObject[source].FIO+"</option>");
                   console.log(json[source].FIO);
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
