const API_KEY = "";


var mymap = L.map('map').setView([37.0902, -95.7129], 3.5);


L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: API_KEY
}).addTo(mymap);


var manufacturer = d3.select('#man').text().slice(14).toLowerCase()




d3.json(`static/data/${manufacturer}.json`, function(data) {


    var plot_data = [];


    if (data.length >= 100) {
        
        // get random listings to plot
        var ind;
        var tracker = [];

        while (tracker.length < 100) {
            ind = Math.floor(Math.random()*data.length)
            if (tracker.includes(ind) == false) {
                plot_data.push(data[ind])
                tracker.push(ind)
            };
        };

    } else {
        plot_data = data
    };

    plot_data.forEach(function(veh) {

        var year = veh.year
        var model = veh.model;
        var price = veh.price
        var lat = veh.lat
        var long = veh.long
        var odo = veh.odometer
        var condition = veh.condition

        L.marker([lat, long]).addTo(mymap).bindPopup(`<b>${year} ${manufacturer} ${model}</b><br>Price: \$${price}<br>Mileage: ${odo}<br>Condition: ${condition}`).openPopup();

    });

});
  
