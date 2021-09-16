from pathlib import Path

import os
import requests
import sys

import config
import image_solver

class Viz:
    def __init__(self, manga_id):
        self.session = requests.Session()
        if manga_id:
            self.manga_id = manga_id
        self.token = ""
        if config.LOGIN != "" and config.PASSWORD != "":
            self.login()

    
    def login(self):
        headers = dict(config.API_HEADERS)
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        data = {
            "login": config.LOGIN,
            "pass": config.PASSWORD,
            "uid": 0,
            "rem_user": 1,
        }
        try:
            response = self.session.post(config.API_LOGIN_URL, headers=config.API_HEADERS, data=data).json()
            if "trust_user_jwt" in response:
                self.token = response["trust_user_jwt"]
                print("Logged in successfully")
        except:
            pass


    def get_resource(self, page=0, metadata=False):
        url = f"{config.API_DOWNLOAD_URL}?device_id=3&manga_id={self.manga_id}&page={page}"
        if metadata:
            url += "&metadata=1"
        if self.token != "":
            url += "&trust_user_jwt=" + self.token
        
        response = self.session.get(url, headers=config.API_HEADERS)
        
        if "error" in response.text or response.status_code != 200:
            return None

        return self.session.get(response.text)


    def get_chapter(self):
        if self.token != "":
            self.session.get(f"{config.API_AUTH_URL}?device_id=3&manga_id={self.manga_id}")

        response = self.get_resource(metadata=True)
        if response == None:
            print("Invalid id")
            return False

        self.title = response.json()["title"]

        response = self.get_resource(page=0)
        if response == None:
            print("Login required")
            return False
        
        print(f"{self.manga_id} : {self.title}")
        return True


    def download(self):
        cwd = os.getcwd()
        output_folder = os.path.join(cwd, "viz_out")
        Path(output_folder).mkdir(exist_ok=True)
        content_folder = os.path.join(output_folder, self.title)
        Path(content_folder).mkdir(exist_ok=True)

        i = 0
        while True:
            page_response = self.get_resource(i)
            if page_response == None:
                break
            
            print("\rDownloading page {0} . . .".format(str(i).zfill(3)), end='')
            page = image_solver.solve(page_response.content)
            page.save(os.path.join(content_folder, str(i) + ".png"))

            i += 1
        
        print("\nDone! Content saved to " + str(content_folder))
        

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage:\nviz <manga_id>\n - Downloads the content for the specified item id")
        exit()
    
    viz = Viz(sys.argv[1])
    if viz.get_chapter():
        viz.download()
