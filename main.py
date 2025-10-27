from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def face():
    return render_template('face.html') 

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        date = request.form['date']
        service = request.form['service']
        location = request.form['location']
        notes = request.form.get('notes', '')
        print(f"New booking: {name}, {email}, {date}, {service}, {location}, {notes}")

        return render_template('bookings.html', success=True, data={
            'name': name,
            'email': email,
            'date': date,
            'service': service,
            'location': location,
            'notes': notes
        })

    return render_template('bookings.html', success=False)


@app.route('/gallery1')
def gallery1_pretty():
    return render_template('gallery1.html')

@app.route('/gallery2')
def gallery2():
    return render_template('gallery2.html')

@app.route('/gallery3')
def gallery3():
    return render_template('gallery3.html')

@app.route('/gallery4')
def gallery4():
    return render_template('gallery4.html')

@app.route('/gallery5')
def gallery5():
    return render_template('gallery5.html')

@app.route('/gallery6')
def gallery6():
    return render_template('gallery6.html')

if __name__ == '__main__':
    app.run(debug=True)
