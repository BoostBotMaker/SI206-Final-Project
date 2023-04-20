from bs4 import BeautifulSoup as bs
import re

#in query input the longittude so can call DataPull(-110) to get data
# must download seleneium, go to anaconda, go to environ ment set sort
#  to not installed and click and install selenium

def DataPull(query):
    from selenium import webdriver
#-110 -100 -90 -80
    driver = webdriver.PhantomJS()
    driver.get("https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/40,"+query+"/land_ocean/all/1/2011-2013")

    # This will get the html after on-load javascript
    html = driver.execute_script("return document.documentElement.innerHTML;")
    #link_1 = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/40,-110/land_ocean/all/1/2011-2013'
    #neg110 = []
    #link_2 = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/40,-100/land_ocean/all/1/2011-2013'
    #neg100 =[]
    #link_3 = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/40,-90/land_ocean/all/1/2011-2013'
    #neg90 =[]
    #link_3 = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/40,-80/land_ocean/all/1/2011-2013'
    #neg80 =[]
    lst = []
    #<tbody aria-live="polite" aria-relevant="all"><tr role="row"><td class="left primary" data-sortval="25"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Jan 01">January 2013</a></td><td data-sortval="-1.71">-1.71°C</td><td data-sortval="3"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201301#all">3</a></td></tr><tr role="row"><td class="left primary" data-sortval="24"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Dec 01">December 2012</a></td><td data-sortval="0.13">0.13°C</td><td data-sortval="12"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201212#all">12</a></td></tr><tr role="row"><td class="left primary" data-sortval="23"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Nov 01">November 2012</a></td><td data-sortval="2.43">2.43°C</td><td data-sortval="23"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201211#all">23</a></td></tr><tr role="row"><td class="left primary" data-sortval="22"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Oct 01">October 2012</a></td><td data-sortval="-0.41">-0.41°C</td><td data-sortval="8"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201210#all">8</a></td></tr><tr role="row"><td class="left primary" data-sortval="21"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Sep 01">September 2012</a></td><td data-sortval="1.06">1.06°C</td><td data-sortval="18"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201209#all">18</a></td></tr><tr role="row"><td class="left primary" data-sortval="20"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Aug 01">August 2012</a></td><td data-sortval="0.93">0.93°C</td><td data-sortval="16"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201208#all">16</a></td></tr><tr role="row"><td class="left primary" data-sortval="19"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Jul 01">July 2012</a></td><td data-sortval="1.62">1.62°C</td><td data-sortval="20"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201207#all">20</a></td></tr><tr role="row"><td class="left primary" data-sortval="18"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Jun 01">June 2012</a></td><td data-sortval="2.32">2.32°C</td><td data-sortval="22"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201206#all">22</a></td></tr><tr role="row"><td class="left primary" data-sortval="17"><a href="/access/monitoring/climate-at-a-glance/global/mapping/May 01">May 2012</a></td><td data-sortval="0.68">0.68°C</td><td data-sortval="15"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201205#all">15</a></td></tr><tr role="row"><td class="left primary" data-sortval="16"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Apr 01">April 2012</a></td><td data-sortval="2.7">2.70°C</td><td data-sortval="24"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201204#all">24</a></td></tr><tr role="row"><td class="left primary" data-sortval="15"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Mar 01">March 2012</a></td><td data-sortval="3.47">3.47°C</td><td data-sortval="25"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201203#all">25</a></td></tr><tr role="row"><td class="left primary" data-sortval="14"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Feb 01">February 2012</a></td><td data-sortval="-0.27">-0.27°C</td><td data-sortval="10"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201202#all">10</a></td></tr><tr role="row"><td class="left primary" data-sortval="13"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Jan 01">January 2012</a></td><td data-sortval="2">2.00°C</td><td data-sortval="21"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201201#all">21</a></td></tr><tr role="row"><td class="left primary" data-sortval="12"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Dec 01">December 2011</a></td><td data-sortval="-0.28">-0.28°C</td><td data-sortval="9"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201112#all">9</a></td></tr><tr role="row"><td class="left primary" data-sortval="11"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Nov 01">November 2011</a></td><td data-sortval="-0.73">-0.73°C</td><td data-sortval="7"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201111#all">7</a></td></tr><tr role="row"><td class="left primary" data-sortval="10"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Oct 01">October 2011</a></td><td data-sortval="1.05">1.05°C</td><td data-sortval="17"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201110#all">17</a></td></tr><tr role="row"><td class="left primary" data-sortval="9"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Sep 01">September 2011</a></td><td data-sortval="0.66">0.66°C</td><td data-sortval="14"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201109#all">14</a></td></tr><tr role="row"><td class="left primary" data-sortval="8"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Aug 01">August 2011</a></td><td data-sortval="1.09">1.09°C</td><td data-sortval="19"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201108#all">19</a></td></tr><tr role="row"><td class="left primary" data-sortval="7"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Jul 01">July 2011</a></td><td data-sortval="0.39">0.39°C</td><td data-sortval="13"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201107#all">13</a></td></tr><tr role="row"><td class="left primary" data-sortval="6"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Jun 01">June 2011</a></td><td data-sortval="-1.05">-1.05°C</td><td data-sortval="6"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201106#all">6</a></td></tr><tr role="row"><td class="left primary" data-sortval="5"><a href="/access/monitoring/climate-at-a-glance/global/mapping/May 01">May 2011</a></td><td data-sortval="-2.63">-2.63°C</td><td data-sortval="2"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201105#all">2</a></td></tr><tr role="row"><td class="left primary" data-sortval="4"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Apr 01">April 2011</a></td><td data-sortval="-1.4">-1.40°C</td><td data-sortval="4"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201104#all">4</a></td></tr><tr role="row"><td class="left primary" data-sortval="3"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Mar 01">March 2011</a></td><td data-sortval="-0.19">-0.19°C</td><td data-sortval="11"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201103#all">11</a></td></tr><tr role="row"><td class="left primary" data-sortval="2"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Feb 01">February 2011</a></td><td data-sortval="-3.26">-3.26°C</td><td data-sortval="1"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201102#all">1</a></td></tr><tr role="row"><td class="left primary" data-sortval="1"><a href="/access/monitoring/climate-at-a-glance/global/mapping/Jan 01">January 2011</a></td><td data-sortval="-1.08">-1.08°C</td><td data-sortval="5"><a href="/access/monitoring/climate-at-a-glance/global/rankings/40,-110/land_ocean/201101#all">5</a></td></tr></tbody>
    soup = bs(html,'html.parser')
    for row in soup.find('table').find('tbody').find_all('tr'):
        date = row.find('a').text
        temp = float(re.findall('-?[0-9]+\.[0-9]+',row.find_all('td')[1].text)[0])
        tup = (date,temp)
        lst.append(tup)

    # data one loop
    return lst
#DataPull(str(-110))