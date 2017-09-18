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

    getAddressFromLatLng(location.latLng)
        .then(addr => alert(addr))
        .catch(err => alert('failed due ' + err));
}

function getAddressFromLatLng(latlng) {
    return new Promise((resolve, reject) => {
        var geocoder = new google.maps.Geocoder;
        geocoder.geocode({'location': latlng}, function(results, status) {
            if (status === 'OK') {
                if (results[0]) {
                    console.log(results);
                    resolve(results[0].formatted_address);
                } 
                
                reject('ZERO_RESULTS');
            }
            
            reject(status);
        });
    });
}