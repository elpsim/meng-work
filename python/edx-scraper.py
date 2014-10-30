from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import json
import pprint
import re
pp = pprint.PrettyPrinter(indent=4)

jsonfile = open('all_courses.json', 'r')
course_info = json.load(jsonfile)

driver = webdriver.Firefox()
driver.get('https://courses.edx.org/login')

raw_input('log in yourself')

# input('Click "Archived" on the side tab')

# list_of_course_links = driver.find_elements_by_class_name("course-link")

for course in course_info:
    pp.pprint(course)
    driver.get(course['url'])
    driver.switch_to_frame(driver.find_element_by_class_name('iframe-register'))

    avail = ""
    if 'Availability' in course:
        avail = course['Availability']
    elif 'availability' in course:
        avail = course['availability']


    if avail != 'Starting Soon':
        # if we are already registered, just access the courseware
        try:
            # driver.find_element_by_class_name("access-courseware")
            driver.find_element_by_class_name("access-courseware").click()

            raw_input('press enter to continue')
        except:
            if 'has-option-verified' in driver.find_element_by_class_name("action-register").get_attribute('class'):
                # enroll in a verified course under honor system
                driver.find_element_by_class_name("action-register").click()
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "honor_mode"))
                )
                driver.find_element_by_name("honor_mode").click()

                # driver.find_element_by_class_name("access-courseware").click()
            else:
                # enroll in a regular course
                driver.find_element_by_class_name("action-register").click()

        try:
            # driver.find_element_by_class_name("access-courseware").click()

            # access to the courseware
            driver.find_element_by_link_text('Courseware').click()

            # TODO: wait for page to load
            raw_input('press enter to continue')

            cousreware_url = driver.current_url
            # TODO: click each side link
            nav = driver.find_element_by_xpath('//nav[@aria-label="Course Navigation"]') # (find the course navigation)
            # click each chapter in course navigation
            chapters = nav.find_elements_by_class_name("chapter")
            # in each chapter, click each a inside the list element (or maybe just click each list element)
            chapter_count = 0
            for chapter_index in range(len(chapters)):
                nav = driver.find_element_by_xpath('//nav[@aria-label="Course Navigation"]')
                chapters = nav.find_elements_by_class_name("chapter")
                chapter = chapters[chapter_index]

                chapter.find_element_by_tag_name('h3').find_element_by_tag_name('a').click()
                links = chapter.find_elements_by_tag_name('li')

                raw_input('press enter to continue')

                link_count = 0
                for link_index in range(len(links)):
                    nav = driver.find_element_by_xpath('//nav[@aria-label="Course Navigation"]')
                    chapters = nav.find_elements_by_class_name("chapter")
                    chapter = chapters[chapter_index]

                    chapter.find_element_by_tag_name('h3').find_element_by_tag_name('a').click()

                    raw_input('press enter to continue')

                    links = chapter.find_elements_by_tag_name('li')
                    link = links[link_index]
                    link.find_element_by_tag_name('a').click()
                    
                    # videos within one clicked link
                    raw_input('press enter to continue')

                    vid_elems = driver.find_elements_by_class_name('seq_video')
                    vid_count = 0
                    for vid_elem_index in range(len(vid_elems)):
                        vid_elem = vid_elems[vid_elem_index]
                        vid_elem.click()

                        raw_input('press enter to continue')
                        # TODO: IT BROKE HERE AND I DON'T KNOW WHY. NEED TO RE-STEP THROUGH THIS EXAMPLE

                        full_url = driver.find_element_by_tag_name('iframe').get_attribute('src')
                        m = re.search('/embed/(?P<id>.*)', b.split('?')[0])
                        # youtube video ID
                        print m.group('id')

                        vid_count += 1


                    link_count += 1

                chapter_count += 1

                    
            # TODO: when done with clicking around, navigate back to course ware page in courseware_url?

        except:
            print "something happened"
            raw_input('press enter to continue')

        raw_input('press enter to continue')