function test(){
alert("Hello");

}

function get_summary(){

    var title = document.getElementById("title_id").value.trim();
    var input = document.getElementById("input_id").value.trim();
    
    $.blockUI();

    $.ajax({
	url: 'get_summary.php',
	data: { "title" : title, "input" : input},
	dataType: 'json',
	method: 'POST',
	success: function(data){
	    document.getElementById("output_id").value = data.result;
	}
    });
    
}

function add_ui_elements(div){
    
    var table = document.createElement("table");
    table.align = "center";
    table.style.height = "100px";

    var title = document.createElement("textarea");
    title.type = "text";
    title.id = "title_id";
    title.cols = 100;
    title.style.height = "50px";
    
    var title_label = document.createElement("label");
    title_label.innerHTML = "Title";

    var input = document.createElement("textarea");
    input.type = "text";
    input.id = "input_id";
    input.cols = 100;
    input.style.height = "500px";

    
    var input_label = document.createElement("label");
    input_label.innerHTML = "Paste your document here ...";

    var output = document.createElement("textarea");
    output.type = "text";
    output.id = "output_id";
    output.cols = 100;
    output.style.height = "500px";
    
    var output_label = document.createElement("label");
    output_label.innerHTML = "Summary of the document ...";

    var button = document.createElement("button");
    button.innerHTML = "Summarize";
    button.class = "button";
    button.style.width = "500px";
    button.style.height = "70px";
    button.onclick = get_summary;
   
    var tr = table.insertRow(-1);
    var td = tr.insertCell(-1);
    
    td.appendChild(title_label);

    tr = table.insertRow(-1);
    td = tr.insertCell(-1);
    td.appendChild(title);

    tr = table.insertRow(-1);
    td = tr.insertCell(-1);
    td.appendChild(input_label);
    
    tr = table.insertRow(-1);
    td = tr.insertCell(-1);
    td.appendChild(input);
    
    tr = table.insertRow(-1);
    td = tr.insertCell(-1);
    td.appendChild(button);

    tr = table.insertRow(-1);
    td = tr.insertCell(-1);
    td.appendChild(output_label);

    tr = table.insertRow(-1);
    td = tr.insertCell(-1);
    td.appendChild(output);

    div.appendChild(table);
}
