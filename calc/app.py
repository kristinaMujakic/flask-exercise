# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def adds():
    '''Adds a and b and returns result as the body.'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)
    return str(result)


@app.route('/sub')
def subtracts():
    '''Subtracts b from a and returns result as the body.'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)
    return str(result)


@app.route('/mult')
def multiplies():
    '''Multiplies a and b and returns result as the body.'''
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    return str(result)


@app.route('/div')
def divides():
    '''Divides a by b and returns result as the body'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)
    return str(result)

# FURTHER STUDY


math_operations = {
    'adds': adds,
    'subtracts': subtracts,
    'multiplies': multiplies,
    'divides': divides,
}


@app.route('/math/<operator>')
def do_math(operator):
    '''With given a and b, do math operations'''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operator(a, b)

    return str(result)
