// from data.js
var tableData = data;

// YOUR CODE HERE!
var headers = ['datetime', 'city', 'state', 'country', 'shape', 'durationMinutes', 'comments'];

var table = d3.select("table");
var tbody = d3.select("tbody");
var row = tbody.append("tr");

for (var i = 0; i < tableData.length; i++) {
    row = tbody.append("tr");
    for (var j = 0; j < headers.length; j++) {
        row.append("td").text(tableData[i][headers[j]]);
    }
}

var button = d3.select("#filter-btn");

button.on("click", function() {
    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#datetime");
    // Get the value property of the input element
    var inputValue = inputElement.property("value");

    console.log(inputValue);

    var filteredData = tableData.filter(sighting => sighting.datetime === inputValue);

    tbody.html('');

    if (inputValue != '') {

        for (var i = 0; i < filteredData.length; i++) {
            row = tbody.append("tr");
            for (var j = 0; j < headers.length; j++) {
                row.append("td").text(filteredData[i][headers[j]]);
            }
        }
    } else {

        for (var i = 0; i < tableData.length; i++) {
            row = tbody.append("tr");
            for (var j = 0; j < headers.length; j++) {
                row.append("td").text(tableData[i][headers[j]]);
            }
        }
    }
});