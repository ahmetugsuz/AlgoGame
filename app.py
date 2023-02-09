from flask import Flask, redirect, jsonify, request

app = Flask(__name__)

# A bit of C syntaks where global values is CAPS LOCKED
ENEMIES_PLAYED = []
ALGORITME = ""
ANTALL_BOKS = 0
TOTAL_POINTS = 0

@app.route("/")
def main():
    return "Server is working"

def control_receives():
    print("Control API DEBUG: ENEMIES_PLAYED: ", ENEMIES_PLAYED, ", ALGORITME: ", ALGORITME, ", ANTALL_BOKS: ",ANTALL_BOKS, "TOTAL_POINTS: ",TOTAL_POINTS)

@app.route("/to_optionpage", methods=['POST'])
def restart_and_to_optionpage():
    global ENEMIES_PLAYED
    global ALGORITME
    global ANTALL_BOKS
    global TOTAL_POINTS

    ENEMIES_PLAYED.clear()
    ALGORITME = ""
    ANTALL_BOKS = 0
    TOTAL_POINTS = 0
 
    response = jsonify({})
    response.status_code = 302
    response.headers['locate'] = "/optionpage"
    return response


@app.route("/algoritme_data", methods=['POST'])
def start_game():
    data = request.get_json()
    global ALGORITME
    global ANTALL_BOKS

    ALGORITME = data["algoritme"]
    ANTALL_BOKS = data["antall"]

    control_receives()

    response = jsonify({})
    response.status_code = 302
    response.headers['algo'] = ALGORITME
    response.headers['ant'] = ANTALL_BOKS
    return response


if __name__ == "__main__":
    app.run(debug=True)
