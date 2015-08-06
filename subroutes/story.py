"""
    story.py
"""

from bottle import Bottle, template

app = Bottle()


@app.route('/')
def story_main():
    pass


@app.route('/<story_num:int>')
def show_story(story_num):
    pass


@app.error(404)
def error404(error):
    return 'Nothing Here...'
