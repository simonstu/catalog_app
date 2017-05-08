from app import app
from app import session
from flask import render_template, request, redirect, url_for
from database_setup import Category, Item
from sqlalchemy import asc, desc
from helper import *


# Show all categories and newest items
@app.route('/')
@app.route('/categories/')
@app.route('/catalog/')
def showCategories():
    categories = session.query(Category).order_by(asc(Category.name))
    latestItems = session.query(Item).order_by(desc(Item.created_at)).limit(10)
    return render('categories.html',
                  categories=categories,
                  latestItems=latestItems)


# show items of a specific category
@app.route('/catalog/<category>')
def showCategory(category):
    categories = session.query(Category).order_by(asc(Category.name))
    category = session.query(Category).filter_by(name=category).one()
    if category:
        items = session.query(Item).filter_by(
            category_id=category.id).order_by(desc(Item.created_at))
    return render('category.html',
                  categories=categories,
                  selected_category=category,
                  items=items)


# details of a specific item
@app.route('/catalog/<category>/<item>')
def showItem(category, item):
    categories = session.query(Category).order_by(asc(Category.name))
    category = session.query(Category).filter_by(name=category).one()
    if category:
        item = session.query(Item).filter_by(name=item).filter_by(
            category_id=category.id).one()
    userOwnsItem = userIDofLoggedInUser(session) == item.user_id
    return render('item.html',
                  categories=categories,
                  selected_category=category,
                  selected_item=item,
                  userOwnsItem=userOwnsItem)


# add a new item
@app.route('/catalog/newItem', methods=['GET', 'POST'])
def newItem():
    user = userIsLoggedIn()
    if not user:
        return redirect(url_for('showCategories'))
    if request.method == 'POST':
        user_id = userIDofLoggedInUser(session)
        newItem = Item(name=request.form['name'],
                       description=request.form['description'],
                       category_id=request.form['category'],
                       user_id=user_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('showCategories'))

    else:
        categories = session.query(Category).order_by(asc(Category.name))
        return render('item_new.html',
                      categories=categories)


# edit an item, if user is allowed to
@app.route('/catalog/editItem/<category>/<item>', methods=['GET', 'POST'])
def editItem(category, item):
    # check if user is logged in
    user = userIsLoggedIn()
    category = session.query(Category).filter_by(name=category).one()
    if category:
        item = session.query(Item).filter_by(name=item).filter_by(
            category_id=category.id).one()
    # check if user created the item he wants to edit
    if item:
        userOwnsItem = userIDofLoggedInUser(session) == item.user_id
    if not user or not userOwnsItem:
        return redirect(url_for('showCategories'))
    # change item as user edited it
    if request.method == 'POST':
        if request.form['name']:
            item.name = request.form['name']
        if request.form['description']:
            item.description = request.form['description']
        if request.form['category']:
            item.category_id = request.form['category']
        session.add(item)
        session.commit()
        return redirect(url_for('showCategories'))
    # show form to edit this item as user owns it
    else:
        categories = session.query(Category).order_by(asc(Category.name))
        return render('item_edit.html',
                      categories=categories,
                      previous_category=category,
                      item=item)


# delete an item, if user is allowed to
@app.route('/catalog/deleteItem/<category>/<item>', methods=['GET', 'POST'])
def deleteItem(category, item):
    # check if user is logged in
    user = userIsLoggedIn()
    category = session.query(Category).filter_by(name=category).one()
    if category:
        item = session.query(Item).filter_by(name=item).filter_by(
            category_id=category.id).one()
    # check if user created the item he wants to delete
    if item:
        userOwnsItem = userIDofLoggedInUser(session) == item.user_id
    if not user or not userOwnsItem:
        return redirect(url_for('showCategories'))
    if request.method == 'POST':
        session.delete(item)
        session.commit()
        return redirect(url_for('showCategories'))
    # ask user if he really wants to delete this item
    else:
        return render('item_delete.html',
                      category=category,
                      item=item)
