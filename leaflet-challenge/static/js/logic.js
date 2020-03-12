// Query all earthquakes in the last week
var url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson';


// Creating map object
var myMap = L.map("map", {
    center: [34.0522, -118.2437],
    zoom: 4
  });


// Add base layer
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    accessToken: token
}).addTo(myMap);

// Pulling Data and running Marker Builder
d3.json(url, function(data) {
    buildMarkers(data.features);
});

// Applying Marker Builder
function buildMarkers(earthquakes) {

    //onEachFeature: build;

    earthquakes.forEach(build);

}

// Marker Builder
function build(earthquake) {

    var mag = earthquake.properties.mag;
    var col;
    var opa = mag / 8;

    if (mag > 5) {
        col = '#ff4000'
    }
    else if (mag > 4) {
        col = '#ff8000'
    }
    else if (mag > 3) {
        col = '#ffbf00'
    }
    else if (mag > 2) {
        col = '#ffff00'
    }
    else if (mag > 1) {
        col = '#bfff00'
    }
    else if (mag > 0) {
        col = '#80ff00'
    }
    else {
        col = 'white'
        opa = 0
    }

    var geojsonMarkerOptions = {
        radius: mag*5,
        fillColor: col,
        color: col,
        weight: 1,
        opacity: opa,
        fillOpacity: opa
    };

    L.geoJSON(earthquake, {
        pointToLayer: function (feature, latlng) {
            return L.circleMarker(latlng, geojsonMarkerOptions)
                    .bindPopup('<h3>' + `${earthquake.properties.place}` + '</h3>'
                        + '<h5>' + `Magnitude: ${earthquake.properties.mag}` + '</h5>'
                        + '<h5>' + `Time: ${new Date(earthquake.properties.time)}` + '</h5>');
        }
    }).addTo(myMap);

}

// Building Legend
var legend = L.control({position: 'bottomright'});

legend.onAdd = function (myMap) {

    var div = L.DomUtil.create('div', 'info-legend'),
        mags = ['0-1', '1-2', '2-3', '3-4', '4-5', '5+']
        colors = ['#80ff00', '#bfff00', '#ffff00', '#ffbf00', '#ff8000', '#ff4000']
        labels = []

    // Add min & max
    var legendInfo = "<h4>Earthquake Magnitude</h4>"

    div.innerHTML = legendInfo;

    mags.forEach(function(mag, index) {
        labels.push("<li style=\"background-color: " + colors[mags.length - index - 1] + "\">" + mags[mags.length - index - 1] + "</li>")
    });

    div.innerHTML += "<ul>" + labels.join("") + "</ul>";
    return div;

};

legend.addTo(myMap);
