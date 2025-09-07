
import csv
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reserve', methods=['GET', 'POST'])
def reserve():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        date = request.form['date']
        time = request.form['time']
        people = request.form['people']

        with open('reservations.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, email, date, time, people])

        return redirect('/')
    return render_template('reserve.html')

@app.route('/dashboard')
def dashboard():
    reservations = []
    try:
        with open('reservations.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            reservations = list(reader)
    except FileNotFoundError:
        pass  # No reservations yet

    return render_template('dashboard.html', reservations=reservations)

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        address = request.form['address']
        item = request.form['item']

        with open('orders.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, mobile, address, item])

        return redirect('/')

    item = request.args.get('item', 'Unknown')
    return render_template('order.html', item=item)


if __name__ == '__main__':
    app.run(debug=True, port=5501)
