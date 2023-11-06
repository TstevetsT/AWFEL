# This is a fire and forget batch processor that will run multiple python scripts listed in the commands table with the arguments following commands

import subprocess

# Define a list of commands to execute
commands = [
    # ["python", "01OCR2Raw.py", "2281", "2282", "20221005"],
    # ["python", "02Raw2parsed.py", "20221005_raw"],
    ["python", "03parsed2excel.py", "20221005_parsed"],
    # ["python", "01OCR2Raw.py", "2284", "2285", "20221007"],
    # ["python", "02Raw2parsed.py", "20221007_raw"],
    ["python", "03parsed2excel.py", "20221007_parsed"],
    # ["python", "01OCR2Raw.py", "2287", "2290", "20221012"],
    # ["python", "02Raw2parsed.py", "20221012_raw"],
    ["python", "03parsed2excel.py", "20221012_parsed"],    
    # ["python", "01OCR2Raw.py", "2292", "2294", "20221014"],
    # ["python", "02Raw2parsed.py", "20221014_raw"],
    ["python", "03parsed2excel.py", "20221014_parsed"],    
    # ["python", "01OCR2Raw.py", "2296", "2297", "20221017"],
    # ["python", "02Raw2parsed.py", "20221017_raw"],
    ["python", "03parsed2excel.py", "20221017_parsed"],    
    # ["python", "01OCR2Raw.py", "2299", "2301", "20221019"],
    # ["python", "02Raw2parsed.py", "20221019_raw"],
    ["python", "03parsed2excel.py", "20221019_parsed"],
    # ["python", "01OCR2Raw.py", "2303", "2304", "20221024"],
    # ["python", "02Raw2parsed.py", "20221024_raw"],
    ["python", "03parsed2excel.py", "20221024_parsed"],
    # ["python", "01OCR2Raw.py", "2306", "2308", "20221025"],
    # ["python", "02Raw2parsed.py", "20221025_raw"],
    ["python", "03parsed2excel.py", "20221025_parsed"],
    # ["python", "01OCR2Raw.py", "2310", "2313", "20221027"],
    # ["python", "02Raw2parsed.py", "20221027_raw"],
    ["python", "03parsed2excel.py", "20221027_parsed"],    
    # ["python", "01OCR2Raw.py", "2316", "2319", "20221102"],
    # ["python", "02Raw2parsed.py", "20221102_raw"],
    ["python", "03parsed2excel.py", "20221102_parsed"],    
    # ["python", "01OCR2Raw.py", "2321", "2323", "20221107"],
    # ["python", "02Raw2parsed.py", "20221107_raw"],
    ["python", "03parsed2excel.py", "20221107_parsed"],        
    # ["python", "01OCR2Raw.py", "2325", "2326", "20221121"],
    # ["python", "02Raw2parsed.py", "20221121_raw"],
    ["python", "03parsed2excel.py", "20221121_parsed"],    
    # ["python", "01OCR2Raw.py", "2328", "2329", "20221128"],
    # ["python", "02Raw2parsed.py", "20221128_raw"],
    ["python", "03parsed2excel.py", "20221128_parsed"],    
    # ["python", "01OCR2Raw.py", "2332", "2335", "20221219"],
    # ["python", "02Raw2parsed.py", "20221219_raw"],
    ["python", "03parsed2excel.py", "20221219_parsed"],        
    # ["python", "01OCR2Raw.py", "2338", "2338", "20230123"],
    # ["python", "02Raw2parsed.py", "20230123_raw"],
    ["python", "03parsed2excel.py", "20230123_parsed"],            
    # ["python", "01OCR2Raw.py", "2341", "2341", "20230201"],
    # ["python", "02Raw2parsed.py", "20230201_raw"],
    ["python", "03parsed2excel.py", "20230201_parsed"],            
    # ["python", "01OCR2Raw.py", "2343", "2345", "20230203"],
    # ["python", "02Raw2parsed.py", "20230203_raw"],
    ["python", "03parsed2excel.py", "20230203_parsed"],            
    # ["python", "01OCR2Raw.py", "2347", "2348", "20230207"],
    # ["python", "02Raw2parsed.py", "20230207_raw"],
    ["python", "03parsed2excel.py", "20230207_parsed"],              
    # ["python", "01OCR2Raw.py", "2351", "2356", "20230515"],
    # ["python", "02Raw2parsed.py", "20230515_raw"],
    ["python", "03parsed2excel.py", "20230515_parsed"],          
    # ["python", "01OCR2Raw.py", "2358", "2365", "20230516"],
    # ["python", "02Raw2parsed.py", "20230516_raw"],
    ["python", "03parsed2excel.py", "20230516_parsed"],            
    # ["python", "01OCR2Raw.py", "2367", "2372", "20230518"],
    # ["python", "02Raw2parsed.py", "20230518_raw"],
    ["python", "03parsed2excel.py", "20230518_parsed"],                
    # ["python", "01OCR2Raw.py", "2374", "2377", "20230522"],
    # ["python", "02Raw2parsed.py", "20230522_raw"],
    ["python", "03parsed2excel.py", "20230522_parsed"],                
    # ["python", "01OCR2Raw.py", "2379", "2386", "20230523"],
    # ["python", "02Raw2parsed.py", "20230523_raw"],
    ["python", "03parsed2excel.py", "20230523_parsed"],                
    # ["python", "01OCR2Raw.py", "2388", "2399", "20230526"],
    # ["python", "02Raw2parsed.py", "20230526_raw"],
    ["python", "03parsed2excel.py", "20230526_parsed"]            
    # ["python", "02Raw2parsed.py", "20220908_raw"],
    # ["python", "02Raw2parsed.py", "20220912_raw"],
    # ["python", "02Raw2parsed.py", "20220915_raw"],
    # ["python", "02Raw2parsed.py", "20220916_raw"],
    # ["python", "02Raw2parsed.py", "20220923_raw"],
    # ["python", "02Raw2parsed.py", "20220926_raw"],
    # ["python", "02Raw2parsed.py", "20220930_raw"]
    # ["python", "03parsed2excel.py", "20220908_parsed"],
    # ["python", "03parsed2excel.py", "20220912_parsed"],
    # ["python", "03parsed2excel.py", "20220915_parsed"],
    # ["python", "03parsed2excel.py", "20220916_parsed"],
    # ["python", "03parsed2excel.py", "20220923_parsed"],
    # ["python", "03parsed2excel.py", "20220926_parsed"],
    # ["python", "03parsed2excel.py", "20220930_parsed"]
]

# Run each command in the list
for cmd in commands:
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {cmd}\n{e}")
