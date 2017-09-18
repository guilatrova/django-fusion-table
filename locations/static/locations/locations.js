var locations = [];

function updateLocationsList() {
    $('#markers-added ol').html(
        locations.map(location => `<li>LAT: ${location.lat()}; LNG: ${location.lng()}</li>`)
    );
}

function saveLocation(location) {
    locations.push(location)
    updateLocationsList();
}

function retrieveLocations() {

}