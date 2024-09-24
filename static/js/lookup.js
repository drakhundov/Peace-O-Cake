document.addEventListener('DOMContentLoaded', function() {
    let queryInput = document.querySelector('#query')
    let resultList = document.querySelector('#result')
    queryInput.addEventListener('keyup', function() {
        $.get('/lookup?q=' + queryInput.value, function(jobs) {
            html = ''
            for (let i in jobs)
            {
                // TODO: Add links to jobs.
                html += '<li>' + jobs[i].title + '</li>'
            }
            resultList.innerHTML = html
        });
    });
});
