from flask import Flask, request, jsonify, send_from_directory
from flask_pymongo import PyMongo
from fpdf import FPDF
import os
import uuid
from datetime import datetime

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/certdb"
mongo = PyMongo(app)

CERT_DIR = "certificates"
os.makedirs(CERT_DIR, exist_ok=True)

def get_next_id():
    last = mongo.db.certificates.find_one(sort=[("id", -1)])
    return (last["id"] + 1) if last and "id" in last else 1

#http://localhost:8093/generate  cree certif
@app.route("/generate", methods=["POST"])
def generate_certificate():
    data = request.json
    username = data.get("username")
    exam_title = data.get("exam_title")
    score = data.get("score")
    date = data.get("date", datetime.today().strftime("%Y-%m-%d"))

    filename = f"{username}_{exam_title.replace(' ', '_')}.pdf"
    filepath = os.path.join(CERT_DIR, filename)

    # Génération PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Certificate of Completion", ln=True, align='C')
    pdf.ln(20)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"This certifies that {username}", ln=True, align='C')
    pdf.cell(200, 10, txt=f"has successfully passed the exam:", ln=True, align='C')
    pdf.cell(200, 10, txt=f"{exam_title}", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Score: {score}/20", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Date: {date}", ln=True, align='C')
    pdf.output(filepath)

    # Générer l'id personnalisé
    cert_id = get_next_id()

    # Sauvegarde dans MongoDB
    mongo.db.certificates.insert_one({
        "id": cert_id,
        "username": username,
        "exam_title": exam_title,
        "score": score,
        "date": date,
        "filename": filename,
        "created_at": datetime.now()
    })
    
    return jsonify({
        "message": "Certificate created successfully",
        "certificate_url": f"http://localhost:5001/certificates/{filename}"
    })

#http://localhost:8093/certificates/nour5_Spring_Boot.pdf (telecharger pdf)
@app.route("/certificates/<filename>")
def download_certificate(filename):
    return send_from_directory(CERT_DIR, filename)

from bson import ObjectId
#http://localhost:8093/certificates  recuper tout certif
@app.route("/certificates", methods=["GET"])
def list_certificates():
    certs = []
    for cert in mongo.db.certificates.find():
        cert["_id"] = str(cert["_id"])  # Convertir ObjectId en string
        certs.append(cert)
    return jsonify(certs)

#http://localhost:8093/certificates/1
#{ "score": 17, "date": "2025-04-14"}

@app.route("/certificates/<cert_id>", methods=["PUT"])
def update_certificate(cert_id):
    try:
        cert_id = int(cert_id)
    except ValueError:
        return jsonify({"error": "Invalid ID"}), 400

    data = request.json
    update_fields = {}
    if "score" in data:
        update_fields["score"] = data["score"]
    if "date" in data:
        update_fields["date"] = data["date"]
    if not update_fields:
        return jsonify({"error": "No fields to update"}), 400

    result = mongo.db.certificates.update_one(
        {"id": cert_id},
        {"$set": update_fields}
    )

    if result.matched_count == 0:
        return jsonify({"error": "Certificate not found"}), 404

    return jsonify({"message": "Certificate updated"})



#http://localhost:8093/certificates/2
@app.route("/certificates/<cert_id>", methods=["DELETE"])
def delete_certificate(cert_id):
    try:
        cert_id = int(cert_id)
    except ValueError:
        return jsonify({"error": "Invalid ID"}), 400

    cert = mongo.db.certificates.find_one_and_delete({"id": cert_id})
    if not cert:
        return jsonify({"error": "Certificate not found"}), 404

    file_path = os.path.join(CERT_DIR, cert["filename"])
    if os.path.exists(file_path):
        os.remove(file_path)

    return jsonify({"message": "Certificate deleted"})

#http://localhost:8093/certificates/id/2
@app.route("/certificates/id/<cert_id>", methods=["GET"])
def get_certificate_by_id(cert_id):
    try:
        cert_id = int(cert_id)
    except ValueError:
        return jsonify({"error": "Invalid ID"}), 400

    cert = mongo.db.certificates.find_one({"id": cert_id})
    if not cert:
        return jsonify({"error": "Certificate not found"}), 404

    cert["_id"] = str(cert["_id"])
    return jsonify(cert)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
