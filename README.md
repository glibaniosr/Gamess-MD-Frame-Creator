# dynamics_fmn
Python code for joining multiple files/ from a molecular dynamics, that contains frames in xyz coordinates.

  This little code, was made by a very noob and new programmer, who is actually a Computational and Theoretical Chemist.
It was made with a incomensurable help from a real coder. It is one of some small codes, all made with great joy, that I
hope will make life of Computational Chemists easier. Despite coming a bit too late for when it was needed, i finished it anyways.
I think it will be useful for me and more people in the future.

  This program was a request of a friend and coworker, who had multiple .xyz files of a single molecular dynamics computated on
the program Gamess. This .xyz files contained the coordinates (obviously) of each frame of the dynamics. So, all the coordinates
made a movie of the process happening. The problem was that a single movie was divided into two or more files, and the frame number
of each file was independent, starting with Frame 1. So he wanted to stick all the coordinates togheter, and change the frames
numbers to become a continuous numeration single numeration in a single file.

  So this is what this program has to do. Read all the .xyz files which contains the number of atoms, tile (Frame number) and xyz
coordinates. Then it change the title of the Frames after the first file to become a sequence of this first file, and put all
togheter in a single file, whithout changing the original ones.

  I hope we all made good use of it.
