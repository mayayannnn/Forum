# 掲示板サイト

Flask、Peewee、Python、HTML、CSSを使用したシンプルな掲示板サイトです。

## 機能

- **掲示板一覧ホーム**: 投稿数が多い順にスレッドを表示
- **スレッド詳細**: 各スレッドの投稿を閲覧し、新しい投稿を追加
- **新規スレッド作成**: 新しいスレッドを開始

## セットアップ

1. 必要なパッケージをインストール:
```bash
pip install -r requirements.txt
```

2. アプリケーションを起動:
```bash
python app.py
```

3. ブラウザで `http://localhost:5000` にアクセス

## データベース

SQLiteデータベース（`forum.db`）が自動的に作成されます。

## プロジェクト構造

```
forum/
├── app.py              # Flaskアプリケーション
├── models.py           # Peeweeモデル定義
├── requirements.txt    # 依存パッケージ
├── forum.db           # SQLiteデータベース（自動生成）
├── templates/         # HTMLテンプレート
│   ├── base.html
│   ├── index.html
│   ├── thread.html
│   └── new_thread.html
└── static/
    └── css/
        └── style.css  # スタイルシート
```
