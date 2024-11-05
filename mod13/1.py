from flask import Flask, jsonify


app = Flask(__name__)

def alkuluku(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5)+1):
       if number % i == 0:
           return False
    return True

@app.route('/alkuluku/<int:number>' , methods=['GET'])
def katso_alkuluku(number):
    result = {
        "number": number,
        "alkuluku": alkuluku(number)
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
