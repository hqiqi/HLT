$(document).ready(function(){

   // jQuery methods go here...


var currency = ["USD", "AUD", "CHF", "JPY", "GBP", "EUR"];

var currencyratio = 1; 
var currencies = '';
for (var i=0;i<currency.length;i++){
	currencies += '<option value="'+ currency[i] + '">' + currency[i] + '</option>';
}
$('#currencies').append(currencies);
$( "#currencies" ).change(function() {
	$('#currencypair').empty();
var currencypair = '';
for (var i=0;i<currency.length;i++){
	if(currency[i]!=$('#currencies').val()){
	currencypair += '<option value="'+ currency[i] + $('#currencies').val()+'">' + currency[i] + $('#currencies').val() + '</option>';
	}
}
$('#currencypair').append(currencypair);
});

$( "#calculate" ).click(function() {
	
	//every time calculate button click this will execute
	var amount = (Number($("#asize").val()) * Number($('#rratio').val()))/100;
	
	//write formula and tag it into a variable
	 $("#amount").text(amount);
	 //tag the result of the calculation to a html tag
	 //$("#rratio").val()+$("#sloss").val();
	});

});


$(".colorMe td").each(function() {
    var val = parseInt(this.innerHTML, 10);
    if (val < 3000) {
        this.style.backgroundColor = "#F00000";
    }
});


