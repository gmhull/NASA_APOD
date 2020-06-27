import datetime, requests, os
from PIL import Image
from io import BytesIO

def get_image(base_url, dir, days):
    for file in os.listdir(dir):
        file_path = os.path.join(dir, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except:
            print("File Didn't Delete")
    for day in range(days):
        DATE = datetime.datetime.now() - datetime.timedelta(days=day)
        DATE = DATE.strftime("%Y-%m-%d")
        url = base_url + DATE
        NASA_POD_URL = requests.get(url).json()['url']
        print(requests.get(url).json()['explanation'])
        img = requests.get(NASA_POD_URL)
        img = Image.open(BytesIO(img.content))
        img.save(dir + '/APOD_' + DATE + ".JPG")

def main():
    API_KEY = '2Yi6UDVVE4lMtSRex9pdBhPjXuhft3ylshAOvPVO'
    DAYS = 1
    DIRECTORY = 'C:/Users/Garth/Pictures/Wallpaper'
    NASA_API_URL = "https://api.nasa.gov/planetary/apod?api_key=%s&date=" % (API_KEY)
    get_image(NASA_API_URL, DIRECTORY, DAYS)

if __name__ == "__main__":
    main()
