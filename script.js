// Initialize the map
const map = L.map('map').setView([0, 0], 2);

// Add the map tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Search button click event
document.getElementById('searchButton').addEventListener('click', () => {
    const searchInput = document.getElementById('searchInput').value;
    if (searchInput) {
        searchLocation(searchInput);
    }
});

// Function to search for a location
function searchLocation(query) {
    fetch(`https://nominatim.openstreetmap.org/search?q=${query}&format=json`)
        .then(response => response.json())
        .then(data => {
            if (data.length > 0) {
                const lat = parseFloat(data[0].lat);
                const lon = parseFloat(data[0].lon);
                map.setView([lat, lon], 10); // Adjust the zoom level as needed
                L.marker([lat, lon]).addTo(map)
                    .bindPopup(data[0].display_name)
                    .openPopup();
            } else {
                alert('Location not found.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
