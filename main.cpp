#include "Shapes.h"
#include <windows.h>
#include <cmath>

class Circle : public Shapes {
private:
    double Radius;
public:
    Circle(Point p, double radius, int r, int g, int b)
        : Shapes(p, 0.0, r, g, b), Radius(radius) {}

    void Draw(HDC h) override {
        int X = P.GetX();
        int Y = P.GetY();
        HPEN hPen = CreatePen(PS_SOLID, 2, RGB(R, G, B));
        SelectObject(h, hPen);
        Ellipse(h, X - (int)Radius, Y - (int)Radius,
                    X + (int)Radius, Y + (int)Radius);
        DeleteObject(hPen);
    }
};
