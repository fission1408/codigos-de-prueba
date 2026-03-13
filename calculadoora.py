from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    datos = None

    if request.method == "POST":
        edad = int(request.form["edad"])
        peso = float(request.form["peso"])
        altura = float(request.form["altura"])
        sexo = request.form["sexo"]
        actividad = request.form["actividad"]
        objetivo = request.form["objetivo"]
        cintura = float(request.form["cintura"])
        cuello = float(request.form["cuello"])
        cadera = request.form.get("cadera")

        # TMB (Mifflin-St Jeor)
        if sexo == "hombre":
            tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + 5
        else:
            tmb = (10 * peso) + (6.25 * altura) - (5 * edad) - 161

        # Factor actividad
        factores = {
            "sedentario": 1.2,
            "ligero": 1.375,
            "moderado": 1.55,
            "alto": 1.725
        }
        mantenimiento = tmb * factores[actividad]

        # Objetivo
        if objetivo == "bajar":
            calorias = mantenimiento - 500
        elif objetivo == "subir":
            calorias = mantenimiento + 500
        else:
            calorias = mantenimiento

        # Grasa corporal
        if sexo == "hombre":
            grasa = 86.010 * math.log10(cintura - cuello) - 70.041 * math.log10(altura) + 36.76
        else:
            grasa = (
                163.205 * math.log10(cintura + float(cadera) - cuello)
                - 97.684 * math.log10(altura)
                - 78.387
            )

        datos = {
            "tmb": round(tmb),
            "mantenimiento": round(mantenimiento),
            "calorias": round(calorias),
            "grasa": round(grasa, 2)
        }

    return render_template("index.html", datos=datos)

if __name__ == "__main__":
    app.run(debug=True)
