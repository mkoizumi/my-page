import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'template_project.settings')

import django
django.setup()

#FAKE POP SCRIPT
import random
from template_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

# adds random topic from topics list
def add_topic():
    # indexing of zero at the end to just get the object of tuple (look at the doc)
    # Topic.objects.get_or_create(...) -> creates an OBJECT!!!
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get the topic for the entry (five times)
        top = add_topic()  # retrieving new Topic object from the above method

        # create the fake data for that topic
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create the new webpage entry
        webp = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]

        # create AccessRecord, notice: name is ForeignKey of type webpage, so we need to pass webpage object
        acc_rec = AccessRecord.objects.get_or_create(name = webp, date = fake_date)[0]


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populate complete!!!")
