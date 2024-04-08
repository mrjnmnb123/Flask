from flask import Flask

app = Flask(__name__)

@app.route('/')
def display_info():
    full_name = "Ma. Rejean N. Manaba"
    address = "Cabanban, Oton, Iloilo"
    return f"My full name is {full_name} and my address is {address}."

if __name__ == '__main__':
    app.run(debug=True)
