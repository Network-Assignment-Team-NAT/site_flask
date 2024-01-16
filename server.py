from flask import Flask, render_template, send_file
import os


def list_files_in_directory(directory, list_of_files):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            list_of_files.append(f'{directory}\\{filename}')


app = Flask(__name__)

plan = 'empty'


@app.route('/', methods=['GET'])
def hello():
    return render_template('hello.html')


@app.route('/un-speed-traffic', methods=['GET'])
def download_page_u():
    global plan
    plan = 'uu'
    return render_template('download.html')


@app.route('/lim-speed-un-trafic', methods=['GET'])
def download_page_lu():
    global plan
    plan = 'lu'
    return render_template('download.html')


@app.route('/un-speed-lim-traffic', methods=['GET'])
def download_page_ul():
    plan = 'ul'
    return render_template('download.html')


current_file_index = 0


@app.route('/download')
def download_file():
    global current_file_index

    file_list = []
    list_files_in_directory(f'configs/{plan}', file_list)

    if current_file_index < len(file_list):
        file_path = file_list[current_file_index]
        current_file_index += 1
        return send_file(file_path, as_attachment=True)
    else:
        return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
