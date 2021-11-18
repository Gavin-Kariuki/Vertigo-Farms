from flask import render_template, request, redirect, url_for, flash, abort
from . import main
# from ..email import mail_message
from app import db, photos
from ..models import Post, Comment, User
from .forms import CommentForm, PostForm, UpdateProfile
from flask_login import login_required, current_user


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home, Vertigo-Farms'
    return render_template('index.html', title = title)


@main.route('/<title>', methods=['GET','POST'])
def post(title):
    '''
    view blog page function that will return the blog item
    '''
    form = CommentForm()
    post = Post.query.filter_by(title = title).first()
    comments = post

    if form.validate_on_submit():
        comment = Comment(comment = form.comment.data, author_id = current_user.id, post_id = post.id)
        db.session.add(comment)
        db.session.commit()

        return redirect(url_for('main.post', title = title))

    return render_template('post.html', post = post, form = form, comments = comments)


@main.route('/create_blog', methods=['GET', 'POST'])
@login_required
def create_post():
    
    form = PostForm()

    if form.validate_on_submit():
        post = Post(title = form.title.data, post_content = form.post_content.data, author_id = current_user.id)
        db.session.add(post)
        db.session.commit()

        flash('post created')
        return redirect(url_for('main.show_posts'))

    return render_template('create_post.html', form = form)



@main.route('/<title>/update_post', methods=['POST', 'GET'])
@login_required
def update_post(title):
    post = Post.query.filter_by(title = title).first()
    form = PostForm()

    if form.validate_on_submit():
        title = form.title.data
        post_content = form.post_content.data
        author_id = current_user.id
        db.session.add(post)
        db.session.commit()

        flash('post updated')
        return redirect(url_for('main.show_post', author_id = author_id, post_content = post_content))

    return render_template('auth.update_post.html', form = form)


@main.route('/posts')
def show_posts():
    posts = Post.query.order_by(Post.posted.desc())

    return render_template('show_posts.html', posts = posts)


@main.route('/post/comment/new/<int:id>', methods=['GET', 'POST'])
def new_comment(id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(comment_content = form.comment_content.data)
        new_comment = Comment.save_comment()
        return redirect(url_for('post', id = post.id))

    return render_template('new_comment.html', form = form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template('/profile/profile.html',user = user)


@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))

    return render_template('profile/update.html', form = form)


@main.route('/user/<uname>/update/pic', methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile', uname = uname))


@main.route('/post/delete/<title>')
@login_required
def delete_post(title):
    '''
    Function that will delete a post
    '''
    post = Post.query.filter_by(title = title ).first()

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('main.show_posts'))


