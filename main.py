from flask import Flask,jsonify,request
import csv

all_movie = []
likedmovies = []
unlikedmovies = []
didnotwatch = []

with open("data.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movie = data[1:]

app = Flask(__name__)


@app.route("/getmovie")
def getmovies():
    return jsonify({
        "data":all_movie[0],
        "status": "sucess"
        }),200
    
# @app.route("/likemovies",method = ["POST"])
# def liked_movies():
#     movies_data = all_movie[0]
#     likedmovies.append(movies_data)
#     all_movie.pop(0)
#     return jsonify({
#         "status":"success"
#     }),200
    
    

# @app.route("/unlikemovies",method = ["POST"])

# def unlikemoviest():
#     movies_data = all_movie[0]
#     unlikedmovies.append(movies_data)
#     all_movie.pop(0)
#     return jsonify({
#         "status":"success"
#     }),200

# @app.route("/didnotwatch",method = ["POST"])

# def didnotwatch():
#     movies_data = all_movie[0]
#     didnotwatch.append(movies_data)
#     all_movie.pop(0)
#     return jsonify({
#         "status":"success"
#     }),200

if __name__ == "__main__":
    app.run()