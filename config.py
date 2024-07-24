from decouple import config

QUANDL_API_KEY = config('QUANDL_API_KEY', default="")

if __name__ == "__main__":
    pass