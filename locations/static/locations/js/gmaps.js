const startLocation = {lat: -23.533773, lng: -46.625290};
const validAddressTypes = ["route", "street_address", "intersection", "point_of_interest ", "park"];
var map;

function initMap() {    
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: startLocation
    });

    var layer = new google.maps.FusionTablesLayer({
        query: {
          select: '\'Location\'',
          from: '1hIFxlOCg1zPTwrc9Mgo0-q5__PnmLdcVnDnGLYRW'
        }
    });
    layer.setMap(map);
    
    map.addListener('click', onMapClick);
}

function onMapClick(location) {
    getAddressFromLatLng(location.latLng)
        .then((result) => handleReceivedLocation(result, location))
        .catch(handleError);
}

function getAddressFromLatLng(latlng) {
    return new Promise((resolve, reject) => {
        var geocoder = new google.maps.Geocoder;
        geocoder.geocode({ location: latlng }, function(results, status) {
            if (status === 'OK') {
                if (results[0]) {
                    resolve(results[0]);
                } 
                
                reject('ZERO_RESULTS');
            }
            
            reject(status);
        });
    });
}

function handleReceivedLocation(result, location) {
    if (isAddressValid(result)) {
        var marker = new google.maps.Marker({
            position: location.latLng, 
            map: map
        });        

        var infowindow = new google.maps.InfoWindow({
            content: result.formatted_address
        });
        infowindow.open(map, marker);
        
        toSave = formatLocationToSave(result.formatted_address, location.latLng);
        saveLocation(toSave);
    }
    else {
        console.error('invalid');
    }
}

function handleError(err) {
    alert("You can't mark this location. We got an error: " + err);
}

function isAddressValid(result) {
    const anyValidType = (element) => validAddressTypes.includes(element);
    const isValid = result.types.some(anyValidType);

    return isValid;
}