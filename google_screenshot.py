#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from fillpdf import fillpdfs
#import pyscreenshot
#import time

def take_screenshot(localisation) :
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.google.fr/maps/')

    # Passer l"étape des cookies en cliquer sur accepter via le lien XPath du bouton
    cookie = driver.find_elements(By.XPATH, "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/span")
    cookie[0].click()

    # Trouver la barre de recherche et cliquer dessus afin de pouvoir input le lieu a chercher
    search = driver.find_element(By.ID, "searchboxinput")
    search.click()
    search.send_keys(localisation)
    search.send_keys(Keys.ENTER)


    # pour laisser le temps de charger a la page au cas ou
    time.sleep(3)

    driver.find_element(By.ID, "widget-zoom-out").click()

    driver.find_element(By.CSS_SELECTOR, '[jsaction="minimap.main;contextmenu:minimap.main;focus:minimap.main;mousemove:minimap.main;mouseover:minimap.main;mouseout:minimap.main"]').click()


    time.sleep(2)

    # permet de prendre un screenshot d'une zone de l"écran
    image = pyscreenshot.grab(bbox=(775,400,1645,800))
    image.save("Temp.png")
    # Fermer la page internet dès que c'est fini
    driver.quit()

print("hhoollleeee")