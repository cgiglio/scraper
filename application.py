from flask import Flask, render_template, request
from application import db
from application.models import Article
from application.forms import RetrieveDBInfo
from bs4 import BeautifulSoup
import urllib2

# Elastic Beanstalk initalization
application = Flask(__name__)
application.debug=True
# change this to your own value
application.secret_key = 'cC1YCIWOj9GgWspgNEo2'

def scrape():
    Article.query.delete()
    response = urllib2.urlopen('http://techcrunch.com/')
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    for article in soup.findAll('li', {'class' : 'river-block'}):
        title = str(article.findAll('h2', {'class' : 'post-title'}))[1:-1]
        description = str(article.findAll('p', {'class' : 'excerpt'}))[1:-1]
        byline = str(article.findAll('div', {'class' : 'byline'}))[1:-1]
        image = str(article.findAll('img'))[1:-1]
        a = Article(title, description, byline, image)
        db.session.add(a)
        db.session.commit()

@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    scrape()
    form1 = RetrieveDBInfo(request.form)

    if request.method == 'POST' and form1.validate():
        try:
            query_db = Article.query.order_by(Article.id)
            for q in query_db:
                print(q.title)
            db.session.close()
        except:
            db.session.rollback()
        return render_template('results.html', results=query_db)

    return render_template('index.html', form1=form1)

if __name__ == '__main__':
    application.run(host='0.0.0.0')
