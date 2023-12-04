import requests

def download_inputs(curDay):
    # https://adventofcode.com/2021/day/1/input

    # session_id_filename = "C:/Users/Rasmus/Desktop/adventofcodecookie.txt"
    session_id_filename = "C:/Users/rakrpe/OneDrive - Roskilde Universitet/Desktop/Ting/adventofcodecookie.txt"

    with open(session_id_filename) as file:
        session_id = file.read()

    curYear = 2023
    # curDay = 5
    response = requests.get(f"https://adventofcode.com/{curYear}/day/{curDay}/input",
                cookies={'session': session_id})
    print(response.status_code)

    filename = f'inputs\\day{curDay}.txt'
    with open(filename,'w') as f:
        f.write(response.text)