import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from flask import Flask, render_template, request
from quantum.bell_states import create_bell, run_circuit, save_histogram
from quantum.entanglement import create_entanglement, run_entanglement 
from quantum.teleportation import create_teleportation, run_teleportation  


app = Flask(__name__)

@app.route("/") #homepage
def home(): 
    return render_template("index.html")


    
@app.route("/bell") #bell state page
def bell():
    qc = create_bell()
    counts = run_circuit(qc)
    save_histogram(counts)  # Save the histogram as an image
    return render_template("/bell.html", counts=counts, histogram="histogram.png")  

@app.route("/entanglement") #entanglement page
def entanglement():
    qc = create_entanglement()
    counts = run_entanglement(qc)
    return render_template("entanglement.html", counts=counts)

@app.route("/teleportation") #teleportation page
def teleportation():
    qc = create_teleportation()
    counts = run_teleportation(qc)
    return render_template("teleportation.html", counts=counts)

if __name__ == "__main__":
    app.run(debug=True)