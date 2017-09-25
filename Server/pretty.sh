#!/bin/bash
#Background Colors
E=$(tput sgr0);    R=$(tput setab 1); G=$(tput setab 2); Y=$(tput setab 3);
B=$(tput setab 4); M=$(tput setab 5); C=$(tput setab 6); W=$(tput setab 7);
function e() { echo -e "$E"; }
function x() { echo -n "$E  "; }
function r() { echo -n "$R  "; }
function g() { echo -n "$G  "; }
function y() { echo -n "$Y  "; }
function b() { echo -n "$B  "; }
function m() { echo -n "$M  "; }
function c() { echo -n "$C  "; }
function w() { echo -n "$W  "; }

#putpixels
function u() {
    h="$*";o=${h:0:1};v=${h:1};
    for i in `seq $v`
    do
        $o;
    done
}

img="\
x25 m13 x2 e1 x25 r13 x2 e1 x25 r1 w3 r1 y1 r1 c1 r3 c1 r1 x2 e1 x16 m3 x1 m3 x2 r1 w1 r1 y1 g1 y1 g1 c2 r1 c2 r1 x2 e1 x15 y1 m1 r1 x1 m2 w1 m1 x2 r1 w1 r1 y3 g1 c1 r1 c1 r1 c1 r1 x2 e1 x15 y4 m1 x1 m2 x2 r1 w3 g1 y1 g1 c1 r1 c1 r1 c1 r1 x2 e1 x15 y1 w1 g1 y1 r1 m2 x3 r3 y1 g3 r6 x2 e1 x15 y2 g4 x1 m1 x2 r13 x2 e1 x15 m1 x1 g1 w1 b1 g1 r1 m1 x3 r2 x1 r1 x2 r1 x1 r2 x1 r1 x2 e1 x16 m1 g2 b4 x2 r2 x3 y1 r1 x3 r1 x4 e1 x15 m1 x1 m1 x1 b1 w2 b1 x3 r1 x1 r2 x1 r1 x1 r1 x1 b1 x1 r1 x2 e1 x13 m2 x1 m1 x1 m1 b4 x6 r1 x4 r1 x2 g1 x2 e1 x13 m1 x1 m1 x9 r1 g1 r1 x2 r1 w1 r1 x3 r2 x2 e1 x12 m1 x1 m2 x10 r1 x2 r1 x3 r1 x6 e1 x11 w1 m2 x15 y1 x3 b1 r1 x1 r1 x3 e1 x10 w1 m1 w1 x12 r1 b1 r1 x1 r1 x3 r1 x6 e1 x10 m1 w1 x13 r1 x4 r1 x1 r1 x1 r1 x1 r2 x2 e1 x27 r2 x1 r1 g1 r1 x4 r1 x2 e1 x27 r1 x2 r2 x3 r1 x4 e1 x26 r1 x1 y1 x4 r3 y1 x3 e1 x25 r1 x3 r1 x7 r1 x2 e1 x31 r1 x2 r1 x2 r1 x2 e1 x25 m1 r1 m1 r1 m1 r1 m1 r1 m1 r1 m1 r1 m1 x2"

for n in $img
do
    u $n
done
e;
exit 0;