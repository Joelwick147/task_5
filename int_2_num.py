from flask import Flask, request, render_template_string

app = Flask(__name__)

def integer_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ""
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        user_input = request.form.get("number", "")
        if user_input.isdigit():
            num = int(user_input)
            if 1 <= num <= 3999:
                result = f"The Roman numeral for {num} is: {integer_to_roman(num)}"
            else:
                result = "Please enter a number between 1 and 3999."
        else:
            result = "Invalid input. Please enter a valid integer."

    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Roman Numeral Converter</title>
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" />
        <style>
            body {
                background-color: #f8f9fa;
                font-family: Arial, sans-serif;
            }
            .custom-container {
                padding: 30px;
                max-width: 600px;
                margin: 50px auto;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
            input[type="text"] {
                font-size: 1rem;
            }
            button {
                font-size: 1rem;
            }
            .result-alert {
                margin-top: 20px;
                font-size: 1.2rem;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="custom-container">
            <h2 class="text-center mb-4 text-secondary">Convert a Number to Roman Numeral</h2>
            <form method="POST" class="d-flex justify-content-center gap-3">
                <input type="text" name="number" class="form-control w-50" placeholder="Enter a number" required>
                <button type="submit" class="btn btn-primary">Convert</button>
            </form>
            {% if result %}
            <div class="alert alert-info result-alert" role="alert">
                {{ result }}
            </div>
            {% endif %}
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    '''
    return render_template_string(html, result=result)

if __name__ == "__main__":
    app.run(debug=True)