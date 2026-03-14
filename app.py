from flask import Flask, render_template, request, redirect, url_for
from models import db, Thread, Post
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['DATABASE'] = 'sqlite:///forum.db'

# データベース初期化

@app.before_request
def before_request():
    db.connect()

@app.after_request
def after_request(response):
    db.close()
    return response

@app.route('/')
def index():
    """掲示板一覧ホーム - 投稿数が多い順に表示"""
    threads = Thread.select().order_by(Thread.post_count.desc())
    return render_template('index.html', threads=threads)

@app.route('/thread/<int:thread_id>')
def thread_detail(thread_id):
    """スレッド詳細ページ - 投稿一覧と投稿フォーム"""
    try:
        thread = Thread.get(Thread.id == thread_id)
        posts = Post.select().where(Post.thread == thread).order_by(Post.created_at.desc())
        return render_template('thread.html', thread=thread, posts=posts)
    except Thread.DoesNotExist:
        return redirect(url_for('index'))

@app.route('/thread/<int:thread_id>/post', methods=['POST'])
def add_post(thread_id):
    """スレッドに投稿を追加"""
    try:
        thread = Thread.get(Thread.id == thread_id)
        content = request.form.get('content', '').strip()
        name = request.form.get('name', '').strip()
        
        if content and name:
            Post.create(
                thread_id=thread,
                content=content,
                name=name,
                created_at=datetime.now()
            )
            # 投稿数を更新
            thread.post_count = Post.select().where(Post.thread == thread).count()
            thread.save()
        
        return redirect(url_for('thread_detail', thread_id=thread_id))
    except Thread.DoesNotExist:
        return redirect(url_for('index'))

@app.route('/new_thread', methods=['GET', 'POST'])
def new_thread():
    """新しいスレッドを作成"""
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()
        name = request.form.get('name', '').strip()
        
        if title and content and name:
            thread = Thread.create(
                title=title,
                created_at=datetime.now(),
                post_count=1
            )
            Post.create(
                thread=thread,
                content=content,
                name=name,
                created_at=datetime.now()
            )
            return redirect(url_for('thread_detail', thread_id=thread.id))
    
    return render_template('new_thread.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_tables([Thread, Post], safe=True)
    app.run(debug=True)
