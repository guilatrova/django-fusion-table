const BASE_URL = 'http://localhost:8000/api/locations/';
var locations = [];

$(function() {
    retrieveLocations();
});

function updateLocationsList() {
    $('#markers-added tbody').html(
        locations.map(location => `<tr><td>${location.address}</td>
            <td>${location.lat}</td> 
            <td>${location.lon}</td></tr>`)
    );
}

function formatLocationToSave(address, location) {
    return {
        address: address,
        lat: location.lat(),
        lon: location.lng()
    }
}

function saveLocation(location) {
    $.post(BASE_URL, location)
        .done((data) => {
            locations.push(data);
            updateLocationsList();
            refreshFusionTableLayer();
        })
        .fail((err) => {            
            alert("Sorry. We couldn't save this because: " + errToStr(err.responseJSON));
        });
}

function errToStr(err) {
    if (err['address'])
        return err['address'];

    if (err['detail'])
        return err['detail'];
}

function retrieveLocations() {
    $.get(BASE_URL, (data) => {
        locations = data;
        updateLocationsList();
    });
}

function resetLocations() {
    $.delete(BASE_URL, (success) => {
        locations = [];
        updateLocationsList();
        refreshFusionTableLayer();
    });
}