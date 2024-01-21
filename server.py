from flask import Flask, render_template, send_file
import os


def list_files_in_directory(directory, list_of_files):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            list_of_files.append(f'{directory}\\{filename}')


app = Flask(__name__)

plan = 'empty'

current_file_indices = {
    'un-speed-traffic': 0,
    'lim-speed-un-traffic': 0,
    'un-speed-lim-traffic': 0
}


@app.route('/', methods=['GET'])
def hello():
    return render_template('main.html')


@app.route('/un-speed-traffic', methods=['GET'])
def download_page_u():
    global plan
    plan = 'un-speed-traffic'
    return render_template('survey.html')


@app.route('/lim-speed-un-traffic', methods=['GET'])
def download_page_lu():
    global plan
    plan = 'lim-speed-un-traffic'
    return render_template('survey.html')


@app.route('/un-speed-lim-traffic', methods=['GET'])
def download_page_ul():
    global plan
    plan = 'un-speed-lim-traffic'
    return render_template('survey.html')


@app.route('/submit', methods=['POST'])
def submit():
    return render_template('download.html')


@app.route('/download')
def download_file():
    global plan
    global current_file_indices

    file_lists = {
        'un-speed-traffic': [],
        'lim-speed-un-traffic': [],
        'un-speed-lim-traffic': []
    }

    list_files_in_directory(f'configs/{plan}', file_lists['un-speed-traffic'])
    list_files_in_directory(f'configs/{plan}', file_lists['lim-speed-un-traffic'])
    list_files_in_directory(f'configs/{plan}', file_lists['un-speed-lim-traffic'])

    current_index = current_file_indices.get(plan, 0)

    if current_index < len(file_lists[plan]):
        file_path = file_lists[plan][current_index]
        current_file_indices[plan] += 1
        return send_file(file_path, as_attachment=True)
    else:
        return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
