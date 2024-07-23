'''

1.  apakah API itu berlaku sebagai copyan dari server atau database yang diinteraksikan ???
        solved :  bukan API itu kaya semacam seorang messenger untuk akses ke server atau database
2.  


'''
from  fastapi import FastAPI,Request,Header , HTTPException
import pandas as pd


df = pd.DataFrame()

# membuat dan mengisi dataframe
df['Username'] = ['bob','bono','max']
df['Location'] = ['USA','UK','Netherland']

app = FastAPI()

API_KEY = "testingapitokenkey1234"

# Membuat endpoint == function + url

# .get('the url' default is just using "/")

''' untuk agar bisa selalu updatenya ditampilkan run diterminalnnya harus menggunakan formatnya 
uvicorn "filenamewithoutitsformat":"namavariableyangmenyimpan FastAPI()" --reload '''

@app.get("/")
def handler_data(request: Request) :     # this line of code is to handle .get() function , and it should be close to .get() function
    
    headers = request.headers
    
    return {
        "Hello": "World",
        "Owner" : "qwe" ,
        "headers" : headers
        }

@app.get("/secret")
def handlersecret(password: str=Header(None)):
    #check api key

    if password != API_KEY or password == None:
        raise HTTPException(detail="incorrect password, access denied", status_code=401)
        

    else:
        return {
                "secret":"hanya saya"
                }


@app.get("/data/{loc}")
def getdf(loc) :     # this line of code is to handle .get() function , and it should be close to .get() function
    
    # filter dataframe
    result = df.query(f"Location == '{loc}'")

    return result.to_dict(orient="records")