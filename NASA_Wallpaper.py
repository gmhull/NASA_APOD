import datetime, requests, os
from PIL import Image
from io import BytesIO

def get_image(base_url, dir, years):
    for file in os.listdir(dir):
        file_path = os.path.join(dir, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except:
            print("File Didn't Delete")
    for year in range(years):
        DATE = datetime.datetime.now() - datetime.timedelta(days=365*year)
        DATE = DATE.strftime("%Y-%m-%d")
        url = base_url + DATE
        if requests.get(url).json()['media_type'] == "image":
            NASA_POD_URL = requests.get(url).json()['hdurl']
            img = requests.get(NASA_POD_URL)
            img = Image.open(BytesIO(img.content))
            img.save(dir + '/APOD_' + DATE + ".JPG")
        else:
            print("%s did not have an image" % (DATE))
            continue

def main():
    API_KEY = 'XXXXXX'
    YEARS = 10
    DIRECTORY = 'XXXXXX'
    NASA_API_URL = "https://api.nasa.gov/planetary/apod?api_key=%s&date=" % (API_KEY)
    get_image(NASA_API_URL, DIRECTORY, YEARS)

if __name__ == "__main__":
    main()
