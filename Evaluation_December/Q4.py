import requests
BASE_URL = "https://jsonplaceholder.typicode.com/postskkkkl;aa  'alssa's"

def read_post(post_id):
    response = requests.get(f"{BASE_URL}/{post_id}")
    if response.status_code == 200:
        print("Read Success:", response.json())
    else:
        print("Error:", response.status_code)

def delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/{post_id}")
    print("Delete Status:", response.status_code)

if __name__ == "__main__":
    read_post(1)           
    delete_post(1)  