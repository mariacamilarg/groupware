from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from keepcode.auth import login_required
from keepcode.db import get_db

import datetime

bp = Blueprint('board', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id,'
        ' last_updated, programming_language, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    users = db.execute(
        'SELECT id, username, last_login, online'
        ' FROM user u'
        ' ORDER BY last_login DESC'
    ).fetchall()
    #for u in users:
    #    print(u['username'], u['online'])
    return render_template('board/index.html', posts=posts, users=users)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        programming_language = request.form['programming_language']
        error = None

        if not title:
            error = 'Title is required.'
        if not body:
            error = 'Code is required.'
        if not programming_language:
            error = 'Programming language is required.'

        if error is not None:
            flash(error)
            print(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, programming_language, author_id)'
                ' VALUES (?, ?, ?, ?)',
                (title, body, programming_language, g.user['id'])
            )
            db.commit()
            return redirect(url_for('board.index'))

    return render_template('board/create.html')

def get_post(id, check_author=False):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id,'
        ' last_updated, programming_language, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post

@bp.route('/<int:id>/view')
@login_required
def view(id):
    post = get_post(id)
    return render_template('board/view.html', post=post)

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id, check_author=False)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        programming_language = request.form['programming_language']
        error = None

        if not title:
            error = 'Title is required.'
        if not body:
            error = 'Code is required.'
        if not programming_language:
            error = 'Programming language is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            current_time = datetime.datetime.now()
            db.execute(
                'UPDATE post SET title = ?, body = ?, programming_language = ?, last_updated = ?'
                ' WHERE id = ?',
                (title, body, programming_language, current_time, id)
            )
            db.commit()
            return redirect(url_for('board.index'))

    return render_template('board/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('board.index'))