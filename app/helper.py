from database_setup import User
from flask import session as login_session


# User Helper Functions
def createUser(login_session, session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id, session):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email, session):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


def userIsLoggedIn():
    if 'username' not in login_session:
        return False
    else:
        return True


def userIDofLoggedInUser(session):
    if 'email' in login_session:
        user = session.query(User).filter_by(email=login_session['email']).one()
        return user.id
    else:
        return None