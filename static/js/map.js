//code from freakyjolly.com & Rosie Resume 
var map;
var InforObj = [];
var niagaraFalls = {
    lat: 43.077664999999996,
    lng: -79.07924700000001
};
var markersOnMap = [{
        placeName: "Stay N Play Cottage Lodge 6395 Garner Rd, Niagara Falls, ON L2E 6S4, Canada",
        LatLng: [{
            lat: 43.080887,
            lng: -79.1516717
        }]
    },
    {
        placeName: "Pine Tree House, 4339 Bampfield Street, Niagara Falls, ON L2E 1G7, Canada",
        LatLng: [{
            lat: 43.10196697731903,
            lng: -79.06416070332675
        }]
    },
    {
        placeName: "Craig House, 5057 River Road, Niagara Falls, ON L2E 3G7, Canada",
        LatLng: [{
            lat: 43.100796,
            lng: -79.063494
        }]
    } 
];

window.onload = function() {
    initMap();
};

var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

function addMarker() {
    for (var i = 0; i < markersOnMap.length; i++) {
        var contentString = markersOnMap[i].placeName;

        const marker = new google.maps.Marker({
            position: markersOnMap[i].LatLng[0],
            label: labels[i % labels.length],
            map: map
        });

        const infowindow = new google.maps.InfoWindow({
            content: contentString,
            maxWidth: 110
        });

        marker.addListener('click', function() {
            closeOtherInfo();
            infowindow.open(marker.get('map'), marker);
            InforObj[0] = infowindow;
        });

    }
}

function closeOtherInfo() {
    if (InforObj.length > 0) {
        /* detach the info-window from the marker */
        InforObj[0].set("marker", null);
        /* and close it */
        InforObj[0].close();
        /* blank the array */
        InforObj.length = 0;
    }
}

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: niagaraFalls
    });
    addMarker();
}

