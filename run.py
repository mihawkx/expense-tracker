from app import create_app, db
from app.models import Category

app = create_app()

def seed_categories():
    if Category.query.count() == 0:
        categories = [
            Category(name='Alimentação'), # type: ignore
            Category(name='Transporte'), # type: ignore
            Category(name='Saúde'), # type: ignore
            Category(name='Lazer'), # type: ignore
            Category(name='Moradia'), # type: ignore
            Category(name='Educação'), # type: ignore
            Category(name='Outros') # type: ignore
        ]
        db.session.add_all(categories)
        db.session.commit()
        print("Categorias criadas com sucesso.")

with app.app_context():
    db.create_all()
    seed_categories()

if __name__ == '__main__':
    app.run(debug=True)