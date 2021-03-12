import os
import requests

def generate_post(dir, url):

    feedbacks = []
    
    for txt in os.listdir(dir):
        # Open file
        with open('{}/{}'.format(dir, txt)) as txt_file:
            lines = txt_file.readlines()

            feedbacks.append({
                'title': lines[0].replace('\n', ''),
                'name': lines[1].replace('\n', ''),
                'date': lines[2].replace('\n', ''),
                'feedback': lines[3].replace('\n', '')
            })

    for feedback in feedbacks:
        response = requests.post(url, json=feedback)

        if not response.ok:
            raise Exception("FAILED to POST, reponse: {}, text title: {}".format(response.status_code, feedback['title']))
        print("Feedback title: {} added!, response: {}".format(feedback['title'], response.status_code))


if __name__ == '__main__':
    dir = '/home/irfancr/Practices/Bangkit/autopy/6_AutomatingRealTask/text'
    url = 'http://<url>/feedback/'
    print(generate_post(dir, url))