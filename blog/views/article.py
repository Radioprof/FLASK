from flask import Blueprint, render_template, redirect, request, url_for, current_app
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError

from blog.forms.article import ArticleCreateForm
from blog.models import Article, Author
from blog.models.database import db

articles_app = Blueprint('articles_app', __name__, url_prefix='/articles', static_folder='../static')


@articles_app.route('/', methods=['GET'], endpoint='list')
@login_required
def article_list():
    _articles = Article.query.all()
    return render_template(
        'articles/list.html',
        articles=_articles,
    )


@articles_app.route('/<int:article_id>/', methods=['GET'], endpoint='details')
@login_required
def details(article_id: int):
    _article = Article.query.filter_by(id=article_id).one_or_none()
    try:
        title = _article.title
        text = _article.text
        author = _article.author
    except KeyError:
        return redirect('/articles/')
    return render_template(
        'articles/details.html',
        article=_article,
        title=title,
        text=text,
        author=author,
    )


@articles_app.route('/create/', methods=['GET', 'POST'], endpoint='create')
@login_required
def article_create():
    form = ArticleCreateForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        article = Article(title=form.title.data.strip(), text=form.text.data)
        if current_user.author:
            article.author_id = current_user.id
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            article.author_id = author.id
        try:
            db.session.add(article)
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article!")
        else:
            return redirect(url_for('articles_app.details', article_id=article.id))

    return render_template('articles/create.html', form=form)
