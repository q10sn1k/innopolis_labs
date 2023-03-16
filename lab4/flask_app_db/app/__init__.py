# импортируем библиотеки
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# создаем объекты SQLAlchemy и Migrate
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # загружаем конфигурацию
    app.config.from_object('app.config.Config')

    # инициализируем расширения
    db.init_app(app)

    # регистрируем маршруты
    from app.routes import user_routes, order_routes
    app.register_blueprint(user_routes.bp)
    app.register_blueprint(order_routes.bp)

    return app
