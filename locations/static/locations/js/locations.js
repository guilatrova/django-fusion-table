const BASE_URL = 'http://localhost:8000/api/locations/';
var locations = [];

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
    $.post(BASE_URL, location, (data) => {
        locations.push(data);
        updateLocationsList();
    });    
}

function resetLocations() {
    $.delete(BASE_URL, (success) => {
        locations = [];
        updateLocationsList();
    });
}

jQuery.each( [ "put", "delete" ], function( i, method ) {
    jQuery[ method ] = function( url, data, callback, type ) {
      if ( jQuery.isFunction( data ) ) {
        type = type || callback;
        callback = data;
        data = undefined;
      }
   
      return jQuery.ajax({
        url: url,
        type: method,
        dataType: type,
        data: data,
        success: callback
      });
    };
  });