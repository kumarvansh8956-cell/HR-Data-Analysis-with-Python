import pandas as p

def read_Data(path):

  
  return p.read_csv(path)


def explorating(df):

  print("=="*60)
  print(('##'*15)+'| ~EXPLORATION OF THE DATAFRAME~ |'+('##'*15))
  print("=="*60)

  print("<><>"*12 + '| SHAPE |'+ "<><>"*12 )

  print(df.shape)
  print("<><>"*12 + '| COLUMNS NAME |'+ "<><>"*12 )

  print( df.columns.tolist())
  print("<><>"*12 + '| DATATYPE |'+ "<><>"*12 )
  print(df.dtypes)

  print("<><>"*12 + '| INFORMATION |'+ "<><>"*12 )

  print(df.info())

  print("<><>"*12 + '| TOTAL MISSING DATA |'+ "<><>"*12 )

  print( df.isnull().sum())

  print("<><>"*12 + '| DUPLICATE DATA |'+ "<><>"*12 )


  print( df.duplicated().sum())
  print("<><>"*12 + '| TOP FIVE ROWS |'+ "<><>"*12 )

  print(df.head())

  print("<><>"*12 + '| BOTTOM FIVE ROWS |'+ "<><>"*12 )

  print(df.tail())
  
  print("<><>"*12 + '| STATICAL DESCRIPTION |'+ "<><>"*12 )

  print(df.describe())
  print("<><>"*12 + '| ~ EXPOSURE OF DATAFRAME END ~ |'+ "<><>"*12 )


def Checking_data(df):
  print("=="*60)
  print(('##'*15)+'| CHECKING FOR IMPROPER DATA IN THE PROVIDING DATAFRAME|'+('##'*15))
  print("=="*60)
  for col in df.columns:
    print("<><>"*12 + f'| {col.upper()} |'+ "<><>"*12 )
    print("---"*12 + f'| top rows |'+ "---"*12 )
    
    print(df[col].head())
    print("---"*12 + f'| Bottom rows |'+ "---"*12 )
    print(df[col].tail())
