options = ['firstOption','secondOption','thirdOption'];
var response = [];

for(var i=0;i<options.length;i++){
response += "<option>"+options[i]+"</option>"
document.getElementById('customOptions').innerHTML = response;
}




