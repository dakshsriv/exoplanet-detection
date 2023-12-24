
import os, requests, argparse, sys

parser = argparse.ArgumentParser()

parser.add_argument(
    "--kepler_id",
    type=int,
    required=True,
    help="Kepler ID of the target star.")

#https://exoplanetarchive.ipac.caltech.edu/cgi-bin/IceTable/nph-iceTbl?log=TblView.ExoplanetArchive&workspace=2023.12.05_17.48.28_025132/TblView/2023.12.16_15.55.57_017227&table=/exodata/kvmexoweb/ExoTables/q1_q17_dr24_tce.tbl&pltxaxis=&pltyaxis=&checkbox=1&initialcheckedval=1&splitlabel=0&wsoverride=1&rowLabel=rowlabel&constraint=kepid_display like '%11442793%'&newSchema=0&dhxr1702770970964=1

import requests

# Define the base URL for the NASA Exoplanet Archive API
base_url = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI"

# Define the parameters for your query
#kepler_id = int(input('What is the Kepler ID? '))  # Replace this with your desired Kepler ID
FLAGS, unparsed = parser.parse_known_args()

params = {
    'table': 'q1_q17_dr24_tce',
    'format': 'json',
    'where': f'kepid={FLAGS.kepler_id}'
}


# Make the API request
response = requests.get(base_url, params=params)

data = []

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data1 = response.json()

    # Now 'data' contains the information from the API response
    # You can process and analyze the data as needed
    #print(data1)
else:
    print(f"Error: {response.status_code} - {response.text}")



data = [
   #{'firstfour':'0114', 'fullId': '011442793', 'KIC': '11442793', 'period': 14.44912, 't0': 2.2, 'duration': 0.11267, 'star_radius': 1.2, 'real_radius': 1.32},
   #{'firstfour':'0102', 'fullId': '010227020', 'KIC': '10227020', 'period': 9.8482, 't0': 0.5182, 'duration': 0.24, 'star_radius': 1, 'real_radius': 3}, 
   #{'firstfour':'0128', 'fullId': '012885212', 'KIC': '12885212', 'period': 95.9071, 't0': 35.0988, 'duration': 0.16, 'star_radius': 0.653, 'real_radius': 2.113}, 
   #{'firstfour':'0128', 'fullId': '012834874', 'KIC': '12834874', 'period': 7.6588, 't0': 4.5464, 'duration': 0.128, 'star_radius': 0.855, 'real_radius': 2.325}, 
   #{'firstfour':'0127', 'fullId': '012785320', 'KIC': '12785320', 'period': 57.3838, 't0': 55.9644, 'duration': 0.1634, 'star_radius': 0.79, 'real_radius': 1.45}, 
   #{'firstfour':'0127', 'fullId': '012784167', 'KIC': '12784167', 'period': 1.84787, 't0': 1, 'duration': 0.0767, 'star_radius': 0.853, 'real_radius': 1.481}, 
   #{'firstfour':'0127', 'fullId': '012737015', 'KIC': '12737015', 'period': 24.668, 't0': 13.311, 'duration': 0.3364, 'star_radius': 1.528, 'real_radius': 1.608},
   #{'firstfour':'0127', 'fullId': '012735830', 'KIC': '12735830', 'period': 31.8277, 't0': 7.285, 'duration': 0.0645, 'star_radius': 0.686, 'real_radius': 1.571}, (Finds it is an exoplanet correctly, but does not successfully find the exoplanet radius)
   #{'firstfour':'0126', 'fullId': '012647577', 'KIC': '12647577', 'period': 12.636, 't0': 8.106, 'duration': 0.154, 'star_radius': 0.867, 'real_radius': 1.041}, (Successful)
   #{'firstfour':'0126', 'fullId': '012645057', 'KIC': '12645057', 'period': 6.83, 't0': 5.989, 'duration': 0.1315, 'star_radius': 0.81, 'real_radius': 1.097}, (Successful)
   ]  # CONVERT duration into days

for entry in data1:
  firstfour = '0' + str(FLAGS.kepler_id)[:3]
  fullId = '0' + str(FLAGS.kepler_id)
  kic = str(FLAGS.kepler_id)
  period = entry['tce_period']
  t0 = entry['tce_time0bk']
  duration = entry['tce_duration']
  t0 = round(t0 % period, 4)
  duration /= 24
  duration = round(duration, 4)
  data.append({'firstfour':firstfour, 'fullId': fullId, 'KIC': kic, 'period': period, 't0': t0, 'duration': duration})

print('IDs retrieved')

for x in data:
    os.system(f'mkdir /home/daksh/Projects/exoplanet-detection/exoplanet-ml/data/{x["firstfour"]} >/dev/null 2>&1 \
             && mkdir /home/daksh/Projects/exoplanet-detection/exoplanet-ml/data/{x["firstfour"]}/{x["fullId"]} >/dev/null 2>&1')
    os.system(f' wget -nH --cut-dirs=6 -r -l0 -c -N -np -erobots=off -R "index*" -A _llc.fits \
  -P /home/daksh/Projects/exoplanet-detection/exoplanet-ml/data/{x["firstfour"]}/{x["fullId"]} \
  http://archive.stsci.edu/pub/kepler/lightcurves/{x["firstfour"]}/{x["fullId"]}/ >/dev/null 2>&1')

print('Star data successfully retrieved')

successes = 0
nae = 0
fails = 0
misc = 0

for x in data:
    os.system(f'bazel-bin/astronet/predict   --model=AstroCNNModel   --config_name=local_global   --model_dir=/home/daksh/Projects/exoplanet-detection/exoplanet-ml/astronet/model   --kepler_data_dir=/home/daksh/Projects/exoplanet-detection/exoplanet-ml/data   --kepler_id={x["KIC"]}   --period={x["period"]}   --t0={x["t0"]}   --duration={x["duration"]} >/dev/null 2>&1')
    #print("Hello")
    with open('/home/daksh/Projects/exoplanet-detection/exoplanet-ml/res.txt', 'r') as wr:
      l = wr.read()
      print(f'The TCE with KIC {x["KIC"]}, period {x["period"]}, duration {x["duration"]}, and t0 {x["t0"]} {l}')
    with open('/home/daksh/Projects/exoplanet-detection/exoplanet-ml/res.txt', 'w') as wtr:
      pass

#os.system('rm ')