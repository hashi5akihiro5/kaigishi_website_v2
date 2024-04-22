# ベースイメージ
FROM python:3.8.5

# 環境変数の設定
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

# 作業ディレクトリの設定
WORKDIR /code

# 依存関係のインストール
COPY requirements.txt /code/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt


# プロジェクトのコピー
COPY . /code/