from flask import Flask

app = Flask(__name__)

@app.get('/')
def get_admin():
    return 'hellow'
        

if __name__ == '__main__':
    app.run(host='192.168.1.110',debug=True)        