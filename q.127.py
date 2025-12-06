import json
import yaml

def restructure_file(input_file):
    with open(input_file, "r") as f:
        if input_file.endswith(".json"):
            data = json.load(f)
        else:
            data = yaml.safe_load(f)

    output = {}
    for key, value in data.items():
        clean_key = key.lower().replace(" ", "_")
        output[clean_key] = value

    with open("clean_output.json", "w") as f:
        json.dump(output, f, indent=4)

    return output
