document.getElementById("folder-form").addEventListener("submit", function (e) {
    e.preventDefault();

    const folderPath = document.getElementById("folder-path").value;

    if (!folderPath) {
        alert("Please enter a folder path.");
        return;
    }

    fetch('/process-folder', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({ folder_path: folderPath })
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById("folder-status").innerText = data.message;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById("folder-status").innerText = "Error processing folder!";
        });
});

document.getElementById("query-button").addEventListener("click", function () {
    const queryInput = document.getElementById("query-input").value;

    if (!queryInput) {
        alert("Please enter a query.");
        return;
    }

    fetch('/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: queryInput })
    })
        .then(response => response.json())
        .then(data => {
            const resultsDiv = document.getElementById("results");
            resultsDiv.innerHTML = "";

            if (data.length === 0) {
                resultsDiv.innerHTML = "<p>No results found!</p>";
            } else {
                data.forEach(imgBase64 => {
                    const imgElement = document.createElement("img");
                    imgElement.src = `data:image/png;base64,${imgBase64}`;
                    resultsDiv.appendChild(imgElement);
                });
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById("results").innerHTML = "<p>Error retrieving results!</p>";
        });
});
