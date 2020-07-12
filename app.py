from flask import Flask, Response
import fun
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/player/<int:nid>')
def player(nid):
    file_path = 'noImage/player' + str(nid) + '.txt'
    if os.path.exists(file_path):
        return "This player does not have enough information", 404

    image_path = 'image/player' + str(nid) + '.png'
    if not os.path.exists(image_path):
        name = fun.find_player_name(nid)
        news_list = fun.calculate_news(name)
        keywords = fun.calculate_keywords(news_list)
        ret = fun.draw_word_cloud(keywords, nid, 0)
        if not ret:
            with open(file_path, 'w') as f0:
                f0.write(str(nid))
                return "This player does not have enough information", 404
    with open(image_path, 'rb') as f:
        image = f.read()
    resp = Response(image, mimetype="image/png")
    return resp


@app.route('/team/<int:nid>')
def team(nid):
    file_path = 'noImage/team' + str(nid) + '.txt'
    if os.path.exists(file_path):
        return "This team does not have enough information", 404

    image_path = 'image/team' + str(nid) + '.png'
    if not os.path.exists(image_path):
        name = fun.find_team_name(nid)
        news_list = fun.calculate_news(name)
        keywords = fun.calculate_keywords(news_list)
        ret = fun.draw_word_cloud(keywords, nid, 1)
        if not ret:
            with open(file_path, 'w') as f0:
                f0.write(str(nid))
                return "This team does not have enough information", 404
    with open(image_path, 'rb') as f:
        image = f.read()
    resp = Response(image, mimetype="image/png")
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0')
