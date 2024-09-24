from flask import Flask, render_template, url_for, request

import data
import utils

app = Flask(__name__)

# Used to add, remove, or modify the data collected by the website.
data = data.Data()


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data.add_job(
            title=request.form['job_title'],
            company=request.form['company'],
            description=request.form['job_desc'],
            salary=request.form['salary']
        )
        data.commit()
        return render_template('index.html')
    else:
        return render_template('add_job.html')


@app.route('/lookup', methods=['GET', 'POST'])
def lookup():
    if request.method == 'POST':
        filters = request.form['query'].split(' ')
        jobs = []
        fields = ('title', 'description', 'company')
        for filter in filters:
            for field in fields:
                potential_matches = data.filter(**{field: filter})
                for match in potential_matches:
                    match['salary'] = utils.parse_salary(match['salary'])
                    if not match in jobs:
                        jobs.append(match)
        return render_template('lookup.html', jobs_found=jobs)
    else:
        return render_template('lookup.html')


@app.route('/job/<job_id>')
def job(job_id):
    selected_job = data.get_job(job_id)
    return render_template('job_display.html', **selected_job)


if __name__ == '__main__':
    app.run(debug=True)
