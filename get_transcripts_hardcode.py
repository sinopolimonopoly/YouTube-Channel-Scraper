import sys
sys.stdout.reconfigure(encoding='utf-8')

import csv
import os

import time
import random

from api_scripts.transcript_scripts.transcript_getter import get_transcript

video_ids = ['gAj7I7nt_XA', 'Hkg2e_9PjMI', 'l9Yo0I3GSJ4', 'ESBJgrUdykY', '5XC6GjfM7Os', '3_OArk8bZNU', 'F75zF9pjVUM', 'fWH79nI3DFU', 'kU_W_YIsFL4', 'lZI4IT2EbIc', 'AJ3Py2n_cUY', 'DWgJ57LV4RE', 'y3I17q1I0UQ', 'blDev_gChA4', '-2exRhKYqRk', 'iuhIgUfRz0Y', 'LJaj3E29N_4', 'KzWS_w6An1U', 'WUGzlHBvm-E', 'koNFDjyt6zw', 'i-15DZuO3u0', '53gyRm319-c', '5KLhlKMPKss', 'qc1aPTPIgvA', '18lSwA77zcs', 'sZKQVbWVNYI', 'Mh_IOsM88Ik', 'fGEDb2lUWI4', 'SfkoDFjAZ8g', 'WXKp_11ehbQ', 'BjHLQzkMJtw', 'Cun-ny0N4dw', '9cBVeyhW_SE', 'jrqt8aIvKDo', 'sNsfvfEi27Y', 'keAOhf4FFkQ', 'Hywmhl2eQlQ', '6KrsRM5d_0s', '0AQ_eSNlH78', 'MDJjWi0Wzh8', 'DvawYzNvGbk', 'MRWYEzIF3wM', 'H4lekFAtUZM', 'gEQeKJsAFSk', 'hSg7OFHr1zo', '_ndG_gpa3so', '0Bngto6HLh0', '9FpA4sHH-BA', 'fnXL_svhMoQ', 'UKKxynoBO_w', 'sigPLhr_zFk', 'bv_mX6fbb38', 'KsQeQ1nJOP4', 'EbxQnE0d5Lc', 'A3Tqm5k1IA4', 'kUXXjApmS-E', 'xPl9Qf7UGWM', 'PWrP6XwudJM', 'JU7q3vcEeM0', '4UwJhzIKbLw', 'VtPsXzlzVNM', 'zQyaFzqnoJQ', 'rBQFGw8li4c', 'bG98sWNFymA', '-Qp7n1It40c', 'biZupXfvcYM', 'l07-1bHwBp4']
titles = ['Prime Rib Reuben #shorts', 'What happens if you don’t rest your roast? #shorts', 'How to Prep & French a Prime Rib #shorts', 'Holiday Prime Rib (Thicc crust) #shorts', 'I (kinda) got kicked out of Wendy’s parking lot #shorts', "CAR COOKING: Sleepover at Wendy's (Max vs Baconator) #shorts", 'Dry Aged Striped Bass #shorts', 'Car Cooking x Does it Deep Fry: McRib #shorts', 'The Tomahawk King (well done & rare) #shorts', 'The Old Fashioned: Orange & Whisky Dry Age #shorts', 'The Ultimate Seafood Tower #shorts', 'Does it Deep Fry: Whole Duck #shorts', 'Pulled Pork Cinnamon Rolls #shorts', '$1 vs $100 bite - what does an 8 yr old like more? #shorts', 'Green Dry Aged Turkey #shorts', 'Surf & Turf Sandwich #shorts', 'The right way to carve a Turkey #shorts', '🍆 Wellington #shorts', 'Tomato Wellington 🍅 #shorts', 'The Perfect Thanksgiving Turkey #shorts', '100 Day Dry Age Wagyu Beef Shank #shorts', 'The Turkey Wellington #shorts', 'Dry Aged Tuna Sushi ($4,000!!) #shorts', 'Bacon Wrapped Tomahawk #shorts', "Sour patch kids dry age experiment (don't try this at home) #shorts", 'Eating Duck with Mark Zuckerberg #shorts', 'The Ostrich Egg Exploded Before I Could Slice It 🥲 #shorts', 'Should you really cut steaks AGAINST the grain? (Real fire pit) #shorts', 'How I almost burned down my house #shorts', 'Pumpkin Spice Dry Aged Ribeye #shorts', 'Does it Deep Fry: Ice #shorts', 'How I almost died buying my first smoker #shorts', 'I dropped this steak in real dirt #shorts', 'Steak School: New York Strip (Strip Steak) #shorts', 'Chocolate & Coffee Dry Aged Ribeye #shorts', '6 Steak Temps (Ketchup - Vampire) #shorts', 'Does it Deep Fry: Pork Belly #shorts', 'The Steak Review: Longhorn #shorts', 'Turned 29 so cooked 🥩 #shorts', 'Steak Battles: Max vs Longhorn Steakhouse #shorts', 'Steak of the Sea #shorts', 'Spicy Toro Crispy Rice #shorts', 'Grilled Lobster Roll x Truffle Fries #shorts', 'Team Medium Rare or Well Done? #shorts', 'Did I overreact eating the eyeball? #shorts', 'Pizza Wings #shorts', 'Beefsteak 🍅 #shorts', 'The best way to cook a tomato #shorts', 'Lamb & Peaches for Snoop Dogg #shorts', 'Steak Battles: Max vs. Texas Roadhouse #shorts', 'Dry Aged Wagyu Burger #shorts', 'Steak & Oysters #shorts', 'Next Level Rib Corndogs #shorts', 'Best “it’s raw” comment wins #shorts', 'Teriyaki WAGYU Burnt Ends #shorts', 'Butter Basted Steak Tutorial #shorts', 'Vegan sister makes tuna #shorts', 'Watermelon tuna #shorts', "something's fishy #shorts", 'Filet & Caprese #shorts', 'Black Truffle & Cognac Wagyu Ribeye #shorts', 'Beef Bacon Steak #shorts', 'How to make smoked watermelon taste good #shorts', 'Never wrap with tinfoil... #shorts', 'Most Expensive Beef Jerky? #shorts', 'Prime Rib: Beef Bacon X Blue Cheese #shorts', 'Beef Bacon Burnt Ends #shorts']

if not (len(video_ids) == len(titles)):
    print("different id and title lengths")
    exit()

channel = "maxthemeatguy"
file_name = channel + "_transcripts_4_2.csv"

output_folder = "transcript_output"

file_path = os.path.join(output_folder, file_name)

with open(file_path, 'w', newline='', encoding='utf-8') as transcript_csv:
    writer = csv.writer(transcript_csv)

    writer.writerow(["Video Id", "Title", "Transcript"])
    for idx in range (0, len(video_ids)):
        video_id = video_ids[idx]
        title = titles[idx]
        print(video_id + " - Transcript Attempt")
        
        video_transcript = get_transcript(video_ids[idx])
        print(video_transcript[0:20] + "\n")
        time.sleep(random.uniform(2,6))
        
        writer.writerow([video_id, title, video_transcript])

