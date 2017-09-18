var startLocation = {lat: -23.533773, lng: -46.625290};
var map;

function initMap() {    
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: startLocation
    });    
    
    map.addListener('click', onMapClick);
}

function onMapClick(location) {
    var marker = new google.maps.Marker({
        position: location.latLng, 
        map: map
    });

    var addr = getAddressFromLatLng(location.latLng);
    alert(addr);
}

function getAddressFromLatLng(latlng) {
    var geocoder = new google.maps.Geocoder;
    geocoder.geocode({'location': latlng}, function(results, status) {
        if (status === 'OK') {
            if (results[0]) {
                // console.log(results);
                // return results[0].formatted_address;
                alert(results[0].formatted_address);
            } 
            
            // return 'No results found';
            alert('No results found');
            return;
        } 
            
        // return 'Geocoder failed due to: ' + status;
        alert('Geocoder failed due to: ' + status);
    });
}