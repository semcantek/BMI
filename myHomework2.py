from pywebcopy import save_website
my_link = 'http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec3'
dosya_yeri = ''
proje_adi = 'biyoinformatik python uygulaması'
save_website(
    url= my_link,
    project_folder= dosya_yeri,
    project_name= proje_adi,
    bypass_robots= True,
    debug= True,
    open_in_browser=True,
    delay=None,
    threaded=False,
)