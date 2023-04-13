from bs4 import BeautifulSoup
import requests
import time
'''
with open('Home.html','r') as html_file:
    content=html_file.read()
    #print(content)
    soup=BeautifulSoup(content,'lxml')
    #print(soup.prettify())
    #to find some specific tags
    courses_html_tags=soup.find_all('h5')
    for courses in courses_html_tags:
        print((courses.text))
    course_cards=soup.find_all('div',class_='card')
    for course in course_cards:
        course_name=course.h5.text
        course_price=course.a.text.split()[-1]

        print(f'{course_name} Costs {course_price}')
        #print(course_price) '''
unfamiliar = input('>')
print(f'Filtering out {unfamiliar}')

def findjob():
    # taking the html text
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup=BeautifulSoup(html_text,'lxml')
    #the findall will bring all the job on the first page and only find will takes the first job
    '''job=soup.find('li',class_='clearfix job-bx wht-shd-bx')
    company_name=soup.find('h3',class_='joblist-comp-name')
    skills=soup.find('span',class_='srp-skills')
    print(skills.text.replace(',',''))
    posted=job.find('span',class_='sim-posted').span.text
    #two span takes the text from the span
    print(posted)
    
    print(company_name.text.replace(' ','')) '''

    #-----------------------------------------------------#
    #for all jobs
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    print('Put some skills that you are not familiar with it')

    '''a=int(input('enter how many skills you want to search'))
    list=[]
    for i in range(0,a):
        unfamiliar=input('>')
        list.append(unfamiliar)
    print(list)'''
    for index,job in enumerate(jobs):
        posted = job.find('span', class_='sim-posted').span.text
        if posted=='Posted few days ago': #or if 'few' in posted:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace('  ','')
            skills = job.find('span', class_='srp-skills').text.replace('  ','')
            #print(skills)

            #print(skills.text.replace(',', ''))
            posted = job.find('span', class_='sim-posted').span.text
            more_info=job.header.h2.a['href']
            # two span takes the text from the span
            #print(posted)
            #print(company_name.text.replace(' ', ''))


            if unfamiliar not in skills:
                with open(f'Posts/{index}.text', 'w') as f:
                    f.write(f'Company_Name: {company_name.strip()}\n')
                    f.write(f'Required_skills: {skills.strip()}\n')
                    f.write(f'Published_date: {posted}\n')
                    f.write(f'more_info{more_info}\n')
                print(f'File saved:{index}')



if __name__ =="__main__":
    while True:
        findjob()
        time_wait=10
        print(f'wating {time_wait} minutes...')
        time.sleep(time_wait*60)