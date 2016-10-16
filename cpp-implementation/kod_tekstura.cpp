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
