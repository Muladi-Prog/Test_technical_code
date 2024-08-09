from flask import Flask, render_template, request

app = Flask(__name__)


def generate_odds_numbers(n):
    return [i for i in range(1, n+1) if i % 2 == 1]


def generate_prime_numbers(n):
    list_primes = []
    for i in range(2, n + 1):  # start from 2, since 1 is not prime
        flag = True
        for j in range(2, i):  # check apakah bsa dibagi 2 from up to the number itself?
            if i % j == 0:
                flag = False
                break
        if flag == True:
            list_primes.append(i)
    return list_primes


def generate_triangles(n):
    len_n = len(str(n))
    triangle = []
    for i in range(1, len_n+1):
        # print(str(n)[:i])
        triangle.append(str(n)[i-1] + '0' * (i-1))
    return triangle


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if (request.method == 'POST'):
        number = int(request.form['number'])
        if 'prime' in request.form:
            result = generate_prime_numbers(number)
        elif 'odd' in request.form:
            result = generate_odds_numbers(number)
        elif 'triangle' in request.form:
            result = generate_triangles(number)
            # print(result)
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run()
