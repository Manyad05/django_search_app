document.addEventListener('DOMContentLoaded', function () {
    const searchBar = document.getElementById('searchBar');
    const resultsContainer = document.getElementById('results');

    searchBar.addEventListener('input', function () {
        const query = searchBar.value;

        if (query.length > 3) {
            fetch(`/search-items/?query=${encodeURIComponent(query)}`)
                .then(response => response.json())
                .then(data => {
                    resultsContainer.innerHTML = '';
                    if (data.length > 0) {
                        data.forEach(item => {
                            resultsContainer.innerHTML += `
                                <div class="card mb-2">
                                    <div class="row no-gutters">
                                        <div class="col-md-4">
                                            <img src="${item.image}" class="card-img" alt="${item.name}">
                                        </div>
                                        <div class="col-md-8">
                                            <div class="card-body">
                                                <h5 class="card-title">${item.name}</h5>
                                                <p class="card-text">${item.description}</p>
                                                <p class="card-text"><strong>Price: $${item.price}</strong></p>
                                            </div>
                                        </div>
                                    </div>
                                </div>`;
                        });
                    } else {
                        resultsContainer.innerHTML = '<p>No results found.</p>';
                    }
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                });
        } else {
            resultsContainer.innerHTML = '';
        }
    });
});
