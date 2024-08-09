from flask import Flask, render_template, redirect, url_for, abort, request

app = Flask(__name__)
items = {}
next_id = 0


@app.route('/')
def index():
    return render_template('index.html', items=items)


@app.route('/items', methods=['POST'])
def create_item():
    global next_id
    name = request.form.get('name')
    if not name:
        abort(400, description="Bad Request: Missing 'name'")
    item = {
        'id': next_id,
        'name': name,
    }
    items[next_id] = item
    next_id += 1
    return redirect(url_for('index'))


if (__name__ == '__main__'):
    app.run()
