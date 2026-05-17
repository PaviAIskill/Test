from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bmi_calculator():

    bmi = None
    category = ""

    if request.method == "POST":

        weight = float(request.form["weight"])
        height = float(request.form["height"])

        # Convert cm to meters
        height = height / 100

        # BMI Formula
        bmi = weight / (height * height)

        # Round BMI
        bmi = round(bmi, 2)

        # BMI Category
        if bmi < 18.5:
            category = "Underweight"

        elif bmi < 25:
            category = "Normal Weight"

        elif bmi < 30:
            category = "Overweight"

        else:
            category = "Obese"

    return render_template(
        "index.html",
        bmi=bmi,
        category=category
    )

if __name__ == "__main__":
    app.run(debug=True)