from flask import Flask, render_template, request, redirect, url_for, abort
import json
import markdown
import datetime
import os

app = Flask(__name__)


# Make current_year available in all templates
# Used for copyright footer
@app.context_processor
def inject_current_year():
    return {'current_year': datetime.datetime.now().year}


def load_notes():
    with open('notes.json', 'r') as file:
        return json.load(file)


def load_note_content(filename):
    filepath = os.path.join('notes', filename)
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as file:
        return markdown.markdown(file.read())


def load_posts():
    with open('posts.json', 'r') as file:
        return json.load(file)


def load_post_content(filename):
    filepath = os.path.join('posts', filename)
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file:
        return markdown.markdown(file.read())


def load_projects():
    with open('projects.json', 'r') as file:
        return json.load(file)


def load_project_content(filename):
    filepath = os.path.join('projects', filename)
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file:
        return markdown.markdown(file.read())


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/notes')
def notes():
    notes = load_notes()
    return render_template('notes.html', notes=notes)


@app.route('/notes/<int:note_id>')
def note_detail(note_id):
    notes = load_notes()
    note = next((note for note in notes if note['id'] == note_id), None)
    if note is None:
        abort(404)

    content = load_note_content(f'note{note_id}.md')
    if content is None:
        abort(404)

    return render_template('note_detail.html', note=note, content=content)


@app.route('/projects')
def projects():
    projects = load_projects()
    return render_template('projects.html', projects=projects)


@app.route('/projects/<int:project_id>')
def project_detail(project_id):
    projects = load_projects()
    project = next((project for project in projects if project['id'] == project_id), None)
    if project is None:
        abort(404)

    content = load_project_content(f'project{project_id}.md')
    if content is None:
        abort(404)

    return render_template('project_detail.html', project=project, content=content)


@app.route('/blog')
def blog():
    posts = load_posts()
    return render_template('blog.html', posts=posts)


@app.route('/blog/<int:post_id>')
def post_detail(post_id):
    posts = load_posts()
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is None:
        abort(404)

    content = load_post_content(f'post{post_id}.md')
    if content is None:
        abort(404)

    return render_template('post_detail.html', post=post, content=content)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        return redirect(url_for('contact'))
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
