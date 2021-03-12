import os

def generate_text(dir):
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

    return feedbacks

if __name__ == '__main__':
    dir = '/home/irfancr/Practices/Bangkit/autopy/6_AutomatingRealTask/text'
    print(generate_text(dir))