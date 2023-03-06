from flask import Blueprint, render_template, redirect

articles_app = Blueprint('articles_app', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    1: ['Article 1', 'Text 1', 1],
    2: ['Article 2', 'Text 2', 2],
    3: ['Article 3', 'Text 3', 3],
}


@articles_app.route('/', endpoint='list')
def article_list():
    return render_template(
        'articles/list.html',
        articles=ARTICLES,
    )


@articles_app.route('/<int:article_id>/', endpoint='details')
def details(article_id: int):
    try:
        title = ARTICLES[article_id][0]
        text = ARTICLES[article_id][1]
        author = ARTICLES[article_id][2]
    except KeyError:
        return redirect('/articles/')
    return render_template(
        'articles/details.html',
        article_id=article_id,
        title=title,
        text=text,
        author=author,
    )
