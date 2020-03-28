var manufacturer = d3.select('#man').text().slice(14).toLowerCase()



console.log(manufacturer)

alert('hi4');

d3.json(`static/data/${manufacturer}.json`, function(data) {

    alert('hi5');

    var plot_data;


    if (data.length >= 100) {
        
        // get random items
        var ind;
        var tracker = [];

        while (tracker.length < 100) {
            ind = Math.floor(Math.random()*data.length)
            if (tracker.includes(ind) == false) {
                plot_data.push(data[ind])
                tracker.push(ind)
                console.log(ind)
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