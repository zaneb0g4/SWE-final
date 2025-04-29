from flask import Flask, request, jsonify, render_template, redirect, url_for
from google.cloud import datastore

app = Flask(__name__)
datastore_client = datastore.Client()

@app.route('/create', methods=['POST'])
def create():
    try:
        name = request.form.get('name')
        description = request.form.get('description')

        # Create new entity
        key = datastore_client.key('Item')
        entity = datastore.Entity(key=key)
        entity.update({
            'name': name,
            'description': description
        })
        datastore_client.put(entity)

        return redirect(url_for('home'))
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route("/")
def hello_world():
    return  render_template("frontpage.html")


@app.route("/weekdisplay")
def weekdisplay():
    return render_template("weekdisplay.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)