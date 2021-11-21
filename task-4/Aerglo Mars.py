import argparse
import datetime
import requests

key = "dFlpE62l4DGuMqThDSUlrv9a6fHTkfaEsruqmqXA"

argparser = argparse.ArgumentParser(description = "Show image URL for Mars Rover Photos")

argparser.add_argument(
    'Date',
    metavar='date',
    type = str,
    help = "Earth date in dd.mm.yyyy format."
    )

argparser.add_argument(
    'RoverName',
    metavar='rover_name',
    type = str,
    help = "Mars rover name: Curiosity, Opportunity, or Spirit"
    )

argparser.add_argument(
    'PictureId',
    metavar='picture_id',
    type = int,
    help = "Mars rover picture id"
    )
args = argparser.parse_args()


date = datetime.datetime.strptime(args.Date,"%d.%m.%Y")
date = datetime.datetime.strftime(date,"%Y-%m-%d")

name = args.RoverName.lower()
name.strip()
if name not in ["curiosity", "opportunity", "spirit"]:
    raise ValueError

pid = args.PictureId

link = "https://api.nasa.gov/mars-photos/api/v1/rovers/{}/photos?earth_date={}&api_key={}".format(name,date,key)
print ("The link is: {}".format(link))

data = requests.get(link)
data = data.json()
pics = data['photos']
pid_found = False
for pic in pics:
    if pic["id"] == pid:
        print ("Downloading image form url: {}".format(pic["img_src"]))
        img_file = requests.get(pic["img_src"]).content
        img_filename = "{}.jpg".format(pid)
        with open(img_filename, "wb") as f:
            f.write(img_file)
        print ("Image saved as {}.".format(img_filename))
        pid_found = True
if not pid_found:
    print ("Invalid picture id. Valid picture ids for the selected date are:")
    for pic in pics:
        print (pic["id"])
