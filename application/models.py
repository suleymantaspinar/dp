from . import db


class Category(db.Model):
  __tablename__ = 'category'
  
  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.String(100),
                   index=False,
                   unique=True,
                   nullable=False)
  
  def __init__(self,name):
      self.name = name



# StockData Class/Model
class Price(db.Model):

  __tablename__ = "price"

  id = db.Column(db.Integer,primary_key=True)
  open = db.Column(db.String(100),unique=True)
  high = db.Column(db.String(200))
  low = db.Column(db.Float)
  currency = db.Column(db.String(20))
  date = db.Column(db.Date)
  
  def __init__(self, name, high, low, currency, date):
    self.name = name
    self.high = high
    self.low = low
    self.currency = currency
    self.date = date


# Stock Class/Model
class Asset(db.Model):
  __tablename__ = "asset"

  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.String(100),unique=True)
  fullname = db.Column(db.String(200))
  isin = db.Column(db.Float)
  currency = db.Column(db.Integer)
  symbol = db.Column(db.String(30))

  def __init__(self, name, fullname, isin, currency, symbol):
    self.name = name
    self.fullname = fullname
    self.isin = isin
    self.currency = currency
    self.symbol = symbol