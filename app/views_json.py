from app import app
from app import session
from database_setup import Category, Item
from sqlalchemy import asc, desc
from flask import jsonify


# all categories formatted in JSON
@app.route('/categories/JSON')
@app.route('/catalog/JSON')
def categoriesJSON():
    categories = session.query(Category).order_by(asc(Category.name)).all()
    return jsonify(Categories=[c.serialize for c in categories])


# all item of a specific category formatted in JSON
@app.route('/catalog/<category>/JSON')
def itemOfCategoryJSON(category):
    category = session.query(Category).filter_by(name=category).one()
    if category:
        items = session.query(Item).filter_by(
            category_id=category.id).order_by(desc(Item.created_at))
    else:
        return ""
    return jsonify(items=[i.serialize for i in items])


# details of a specific item of a specific category
@app.route('/catalog/<category>/<item>/JSON')
def detailsOfItemJSON(category, item):
    category = session.query(Category).filter_by(name=category).one()
    if category:
        item = session.query(Item).filter_by(name=item).filter_by(
            category_id=category.id).one()
    else:
        return ""
    return jsonify(Item=item.serialize)
