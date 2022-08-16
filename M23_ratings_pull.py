# Code may need to be altered depending on when running it. Current code is for Launch ratings. 
# You may need to alter the iterations in the URLs

import requests
import pandas as pd
import json
import openpyxl


# Most you can return at once is 1000. Therefore you need to offset 1000 each requests in the URL.  

url1 = "https://ratings-api.ea.com/v2/entities/m23-ratings?filter=iteration:launch-ratings&sort=overall_rating:DESC,firstName:ASC&limit=1000&offset=0"
url2 = "https://ratings-api.ea.com/v2/entities/m23-ratings?filter=iteration:launch-ratings&sort=overall_rating:DESC,firstName:ASC&limit=1000&offset=1000"
url3 = "https://ratings-api.ea.com/v2/entities/m23-ratings?filter=iteration:launch-ratings&sort=overall_rating:DESC,firstName:ASC&limit=1000&offset=2000"

data1 = requests.get(url1).text
data2 = requests.get(url2).text
data3 = requests.get(url3).text

jdata1 = json.loads(data1)
jdata2 = json.loads(data2)
jdata3 = json.loads(data3)
df1 = pd.DataFrame.from_dict(jdata1["docs"])
df2 = pd.DataFrame.from_dict(jdata2["docs"])
df3 = pd.DataFrame.from_dict(jdata3["docs"])

frames = [df1, df2, df3]
df = pd.concat(frames)
df = df.convert_dtypes()
df = df.reset_index(drop = True)

df_final = df[[
    'fullNameForSearch', 'firstName', 'lastName', 'plyrAssetname', 'status', 'iteration', 'plyrPortrait', 
    'primaryKey', 'college', 'height', 'weight', 'plyrHandedness', 'plyrBirthdate', 'age', 'teamId', 'team', 
    'jerseyNum', 'archetype', 'position', 'yearsPro', 'totalSalary', 'signingBonus', 'overall_rating', 
    'awareness_rating', 'speed_rating', 'acceleration_rating', 'strength_rating', 'agility_rating', 
    'jumping_rating', 'toughness_rating', 'stamina_rating', 'injury_rating', 'throwPower_rating', 
    'throwAccuracyShort_rating', 'throwAccuracyMid_rating', 'throwAccuracyDeep_rating', 
    'throwUnderPressure_rating', 'throwOnTheRun_rating', 'breakSack_rating', 'playAction_rating', 
    'carrying_rating', 'bCVision_rating', 'runningStyle_rating', 'changeOfDirection_rating', 
    'breakTackle_rating', 'trucking_rating', 'stiffArm_rating', 'jukeMove_rating', 'spinMove_rating', 
    'catching_rating', 'spectacularCatch_rating', 'catchInTraffic_rating', 'release_rating', 
    'shortRouteRunning_rating', 'mediumRouteRunning_rating', 'deepRouteRunning_rating', 
    'impactBlocking_rating', 'leadBlock_rating', 'passBlock_rating', 'passBlockPower_rating', 
    'passBlockFinesse_rating', 'runBlock_rating', 'runBlockPower_rating', 'runBlockFinesse_rating', 
    'blockShedding_rating', 'powerMoves_rating', 'finesseMoves_rating', 'tackle_rating', 
    'hitPower_rating', 'pursuit_rating', 'playRecognition_rating', 'press_rating', 'zoneCoverage_rating', 
    'manCoverage_rating', 'kickPower_rating', 'kickAccuracy_rating','kickReturn_rating']]
    
df_final.to_excel("Madden23_LaunchRatings.xlsx")
