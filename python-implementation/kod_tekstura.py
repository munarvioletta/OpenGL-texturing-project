from OpenGL.GL import * from OpenGL.GLUT import * from OpenGL.GLU import
* import pygame
 
# przypisanie znaku spacji do zmiennej Spacja    
Spacja = ' '

#zmienne pomocnicze 
window = 0
ID = 0

#DEKLARACJA KATOW OSI ROTACJI jako zmienne os_x,os_y,os_z
os_x = 0.0
os_y = 0.0
os_z = 0.0
 
DIRECTION = 1
 
#FUNKCJA INICJUJ¥CA okno,modelu, widoku, tekstury 
def Inicjacja(Width, Height): 
    glClearColor(0.0, 0.0, 0.0, 0.0) #kolor t³a      
    glMatrixMode(GL_PROJECTION)#macierz projekcji/rzutowania
    glLoadIdentity()
    # widok perspektywiczny
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    
    glMatrixMode(GL_MODELVIEW)#macierz modelu
    glClearDepth(1.0) 
    glDepthFunc(GL_LESS)#funkcja testu bufora glebokosci
    glEnable(GL_DEPTH_TEST)#wlaczanie bufora glebokosci
    glShadeModel(GL_SMOOTH)#w³aczna g³adkie cieniowanie
      
    
 
    # inicjalizowanie tworzenia textury
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    
    #GL_TEXTURE_ENV_MODE - okresla sposob miesznia
    #GL_DECAL - zastapienie slkadowych fragmentow obiektu skladowymi teksteli
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    
   
    
# aktywacja klawisza Spacja klawiatury FUNKCJ¥ keyPressed - zamykanie programu
def keyPressed(*args):
     if args[0] == Spacja:
        sys.exit()
 
#FUNCKCJA RYSUJ¥CA OBIEKT BRYLOWY
def Rysowanie():
    global os_x,os_y,os_z
    global DIRECTION #kierunek obrotu
    
    #czyszczenie buforow koloru i glebokosci
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()
    
    #aktywacja macierzy przesuniêcia-przesuniecie po osi z
    glTranslatef(0.0,0.0,-6.0)
    
    #rotacja kuli wokol osi, x,y,z
    glRotatef(os_x,1.0,0.0,0.0)
    glRotatef(os_y,0.0,1.0,0.0)
    glRotatef(os_z,0.0,0.0,1.0)
    
    # aktywuje obiekt tekstury 
    
    walec = gluNewQuadric() #tworzenie kwadryki
    
    #sposob generacji wektorow normalnych (w³acznie g³adkiego cieniowania)
    gluQuadricNormals(walec, GL_SMOOTH)
    
    #nalozenie tekstury na kwadryke
    gluQuadricTexture(walec, GL_TRUE)
    
    # generowanie kwadryki cylindra
    gluCylinder(walec, 1, 1, 2, 40, 40); 
    
    #rotacja realizowana jest za pomoc¹ zmiany k¹ta (dekrementacja wartosci)  
    os_x = os_x-0.02
    os_y = os_y-0.02
    os_z = os_z-0.02
    
    # zamiana buforów koloru 
    glutSwapBuffers()
 
 
def Ladowanietekstury():
    #ladowanie tekstury
    image = pygame.image.load("cratka.jpg") 

    ix = 256
    iy = 256
    image = pygame.image.tostring(image,"RGBA",1)

    #wyrownanie wiersza mapy pikselowej do jednego byte'a
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)

    #zaladowanie textury
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)

    #parametry tekstutury, sposób zawijania, 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)#wartoœci wspó³rzêdne tekstury s¹ obcinane do przedzialu <0,1>
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)#powielanie tekstury na obiekcie
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)#filtrowanie
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    #GL_TEXTURE_ENV-okresla parametry mieszania teksteli z fragmentami obiektu
    #GL_TEXTURE_ENV_MODE - okresla sposob miesznia
    #GL_DECAL - zastapienie slkadowych fragmentow obiektu skladowymi teksteli
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

#PROGRAM GLOWNY
def main():
    global window
    global ID 
    
    #tworzenie okna wyswietlania
    glutInit(sys.argv)#inicjalizacja biblioteki GLUT
    
    #inicjalizacja bufora ramki
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(640,480)# rozmiar wyswietlanego okna
    glutInitWindowPosition(200,200) #polozenie okna

    window = glutCreateWindow('Walec tekturowany')# tytul okna
    #wyswietlanie  funkcji DrawGLScene
    glutDisplayFunc(Rysowanie)
    
    # wywolanie funkcji RYSOWANIE podczas bezczynnosci systemu(stanu jalowego)
    glutIdleFunc(Rysowanie)
    
    # wywolanie funkcji keyPressed
    glutKeyboardFunc(keyPressed)
    
    #wywo³anie funkcji Inicjacja
    Inicjacja(640, 480)
    
    #wywo³anie funkcji Inicjacja
    Ladowanietekstury()
    
    glutMainLoop()
   
if __name__ == "__main__":
    main()
