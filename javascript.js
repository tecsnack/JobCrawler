javascript
document.getElementById('search-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    var keywords = document.getElementById('keywords').value;
    
    fetch('/crawl?keywords=' + keywords)
        .then(response => response.json())
        .then(data => {
            var jobListings = document.getElementById('job-listings');
            jobListings.innerHTML = '';
            
            if (data.length > 0) {
                data.forEach(function(job) {
                    var jobListing = document.createElement('div');
                    jobListing.classList.add('job-listing');
                    
                    var title = document.createElement('h2');
                    title.textContent = job.Jobtitel;
                    
                    var description = document.createElement('p');
                    description.textContent = job.Beschreibung;
                    
                    var company = document.createElement('span');
                    company.textContent = 'Unternehmen: ' + job.Unternehmen;
                    
                    var postedDate = document.createElement('span');
                    postedDate.textContent = 'Veröffentlicht am: ' + job['Veröffentlicht am'];
                    
                    var link = document.createElement('a');
                    link.href = job.Link;
                    link.textContent = 'Mehr erfahren';
                    
                    jobListing.appendChild(title);
                    jobListing.appendChild(description);
                    jobListing.appendChild(company);
                    jobListing.appendChild(postedDate);
                    jobListing.appendChild(link);
                    
                    jobListings.appendChild(jobListing);
                });
            } else {
                var noResults = document.createElement('p');
                noResults.textContent = 'Keine Ergebnisse gefunden.';
                jobListings.appendChild(noResults);
            }
        })
        .catch(error => console.log(error));
});