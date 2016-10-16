# OpenGL texturing project
A project where the 3D object is created, textured and displayed on screen.

###Goals

1.	Stworzenie elementu bryłowego
1.	Korzystanie z bibliotek OpenGL
1.	Załadowanie obrazu tekstury
1.	Nałożenie Tekstury na Obiekt.
1.	Korzystanie z języków programowania - Phthon, C++
1.	Praca w środowisku programowania Python 2.7.7 
1.	Praca w środowisku programowania Visual Studio C++ 2010

###C++ implementation

####C++ code 

```cpp

#include <glut.h>
#include<gl.h>
#include<GL/glu.h>
#include <glu.h>
#include<math.h>


void Draw() 
{
    glEnable(GL_LIGHTING);//wlaczenie swiatla
    glEnable(GL_LIGHT0);//wlaczenie swiatla nr 1
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT); //czyszczenie buforów
    glEnable(GL_DEPTH_TEST); //WLACZENIE TESTU BUFORA GLEBOKOSCI
    
    glPushMatrix(); // odlozenie macierzy na stos
    glMatrixMode( GL_MODELVIEW ); //macierz modelu
    glLoadIdentity();
    glEnable(GL_POLYGON_OFFSET_FILL); //aktywacja rysowania wypełnionej bryły
    glPolygonOffset(1.0,1.0);  
    
    // parametry materiału(koloru kuli) I oświetlenia

    GLfloat qaBlack[] = {0.0, 0.0, 0.0, 1.0};// color swiatla
    GLfloat qaBlue[] = {0.0, 0.0, 1.0, 1.0};//color swiatla
    GLfloat qaWhite[] = {1.0, 1.0, 1.0, 1.0};//color swiatla
    glMaterialfv(GL_FRONT, GL_AMBIENT, qaBlue);// swiatlo otoczenia
    glMaterialfv(GL_FRONT, GL_DIFFUSE, qaBlue);//swiatlo rozproszone
    glMaterialfv(GL_FRONT, GL_SPECULAR, qaWhite);//światlo punktowe
    glMaterialf(GL_FRONT, GL_SHININESS, 70.0);

    //określenie wspolrzednych pozycji swiatla
    GLfloat LightPosition[]= {20.0, 30.0 , -30.0, -0.1};
    glLightfv(GL_LIGHT0, GL_POSITION, LightPosition);//pozycja swiatla
    
    
    //funkcje rotacji
    glRotatef(20,1.0,0.0,0.0);
    glRotatef(45,0.0,1.0,0.0);

    //kolor krawedzi obiektu
    glColor3f(0.0,0.0,1.0);
    glutSolidSphere(1.0, 60.0,60.0);//rysowanie kuli

    //GLUquadric* gluNewQuadric (int qobj);
    //walec =gluNewQuadric()    
    // gluQuadricNormals(walec, GL_SMOOTH)
    // gluQuadricTexture(walec, GL_TRUE)

    //gluCylinder(walec, 1, 1, 2, 40, 40);

        
    glDisable(GL_POLYGON_OFFSET_FILL); //wylaczenie trybu wypelnienia bryly
    glDisable(GL_LIGHTING);//wylaczenie swiatla 
    glDisable(GL_LIGHT0); //wylaczenie swiatla punktowego
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL); //wypelnienie obiektu
    glPopMatrix(); //zdjęcie macierzy modelowania ze stosu 

    glFlush();
    glutSwapBuffers();  // zamiana buforów koloru
}

void Initialize() 
{
    glClearColor(0.0, 0.0, 0.0, 0.0);// kolor tła
    glViewport(0,0,700,600); //dynamiczna modyfikacja obszaru renderingu
    glMatrixMode(GL_PROJECTION);// macierz rzutowania
    glLoadIdentity();//aktywacja macierzy rzutowania

    //bryla obcinania – rzutowanie prostokatne
    glOrtho(-2.0, 2.0, -2.0, 2.0, -2.0, 2.0);
}

int main(int argc, char** argv) 
{
    glutInit(&argc, argv);  //inicjalizacja biblioteki glut
    glutInitDisplayMode(GLUT_DEPTH |GLUT_DOUBLE| GLUT_RGBA); //bufor ramki
    glutInitWindowSize(700, 600); //rozmiar okna
    glutInitWindowPosition(120, -100);// pozycja okna
    glutCreateWindow("MOJ PROGRAM");//tytuł okna
    Initialize();
    glutDisplayFunc(Draw);// wywołanie funkcji Draw
    glutMainLoop();
    return 0;
}
```

###Python2 implementation

####Python2 code

```python

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
 
#FUNKCJA INICJUJĄCA okno,modelu, widoku, tekstury 
def Inicjacja(Width, Height): 
    glClearColor(0.0, 0.0, 0.0, 0.0) #kolor tła      
    glMatrixMode(GL_PROJECTION)#macierz projekcji/rzutowania
    glLoadIdentity()
    # widok perspektywiczny
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    
    glMatrixMode(GL_MODELVIEW)#macierz modelu
    glClearDepth(1.0) 
    glDepthFunc(GL_LESS)#funkcja testu bufora glebokosci
    glEnable(GL_DEPTH_TEST)#wlaczanie bufora glebokosci
    glShadeModel(GL_SMOOTH)#właczna gładkie cieniowanie
      
    
 
    # inicjalizowanie tworzenia textury
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    
    #GL_TEXTURE_ENV_MODE - okresla sposob miesznia
    #GL_DECAL - zastapienie slkadowych fragmentow obiektu skladowymi teksteli
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    
   
    
# aktywacja klawisza Spacja klawiatury FUNKCJĄ keyPressed - zamykanie programu
def keyPressed(*args):
     if args[0] == Spacja:
        sys.exit()
 
#FUNCKCJA RYSUJĄCA OBIEKT BRYLOWY
def Rysowanie():
    global os_x,os_y,os_z
    global DIRECTION #kierunek obrotu
    
    #czyszczenie buforow koloru i glebokosci
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()
    
    #aktywacja macierzy przesunięcia-przesuniecie po osi z
    glTranslatef(0.0,0.0,-6.0)
    
    #rotacja kuli wokol osi, x,y,z
    glRotatef(os_x,1.0,0.0,0.0)
    glRotatef(os_y,0.0,1.0,0.0)
    glRotatef(os_z,0.0,0.0,1.0)
    
    # aktywuje obiekt tekstury 
    
    walec = gluNewQuadric() #tworzenie kwadryki
    
    #sposob generacji wektorow normalnych (włacznie gładkiego cieniowania)
    gluQuadricNormals(walec, GL_SMOOTH)
    
    #nalozenie tekstury na kwadryke
    gluQuadricTexture(walec, GL_TRUE)
    
    # generowanie kwadryki cylindra
    gluCylinder(walec, 1, 1, 2, 40, 40); 
    
    #rotacja realizowana jest za pomocą zmiany kąta (dekrementacja wartosci)  
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
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)#wartości współrzędne tekstury są obcinane do przedzialu <0,1>
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
    
    #wywołanie funkcji Inicjacja
    Inicjacja(640, 480)
    
    #wywołanie funkcji Inicjacja
    Ladowanietekstury()
    
    glutMainLoop()
   
if __name__ == "__main__":
    main()
```
