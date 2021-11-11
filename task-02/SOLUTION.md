janaki@janaki-HP-Laptop-14s-fq1xxx:~$ mkdir Coordinates-Location
janaki@janaki-HP-Laptop-14s-fq1xxx:~$ cd ~/Coordinates-Location
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ mkdir North
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ cd North
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location/North$ cat >NDegree.txt
9°
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location/North$ cat >NMinutes.txt
5'
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location/North$ cat >NSeconds.txt
38.1"
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location/North$ cat NDegree.txt NMinutes.txt NSeconds.txt >NorthCoordinate.txt
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location/North$ cd
janaki@janaki-HP-Laptop-14s-fq1xxx:~$ cp ~/Coordinates-Location/North/NorthCoordinate.txt ~/Coordinate-Locations
janaki@janaki-HP-Laptop-14s-fq1xxx:~$ mv ~/Coordinates-Location/NorthCoordinate.txt ~/Coordinates-Location/North.txt
mv: cannot stat '/home/janaki/Coordinates-Location/NorthCoordinate.txt': No such file or directory
janaki@janaki-HP-Laptop-14s-fq1xxx:~$ cp ~/Coordinates-Location/North/NorthCoordinate.txt ~/Coordinate-Locations
janaki@janaki-HP-Laptop-14s-fq1xxx:~$ cp ~/Coordinates-Location/North/NorthCoordinate.txt ~/Coordinate-Locations/
cp: failed to access '/home/janaki/Coordinate-Locations/': Not a directory
janaki@janaki-HP-Laptop-14s-fq1xxx:~$ cp ~/Coordinates-Location/North/NorthCoordinate.txt ~/Coordinates-Location
janaki@janaki-HP-Laptop-14s-fq1xxx:~$ rm -i cp ~/Coordinates-Location/North/NorthCoordinate.txt
rm: cannot remove 'cp': No such file or directory
rm: remove regular file '/home/janaki/Coordinates-Location/North/NorthCoordinate.txt'? y
janaki@janaki-HP-Laptop-14s-fq1xxx:~$ cd ~/Coordinates-Location
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ mkdir East
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ cd east
bash: cd: east: No such file or directory
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ cd ~/Coordinates-Location/East
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location/East$ cat EDegree.txt
cat: EDegree.txt: No such file or directory
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location/East$ cat >EDegree.txt
76°
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location/East$ cat >EMinutes.txt
29'
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location/East$ cat >ESeconds.txt
30.8"
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location/East$ cat EDegrre.txt EMinutes.txt ESeconds.txt >EastCoordinate.txt
cat: EDegrre.txt: No such file or directory
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location/East$ cat EDegrre.txt EMinutes.txt ESeconds.txt >EastCoordinate.txt
cat: EDegrre.txt: No such file or directory
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location/East$ cat EDegree.txt EMinutes.txt ESeconds.txt >EastCoordinate.txt
cat: EDegree.txt: No such file or directory
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location/East$ cat EDegree.txt EMinutes.txt ESeconds.txt >EastCoordinate.txt
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location/East$ cp ~/Coordinates-Location/East/EastCoordinate.txt ~/Coordinates-Location/
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location/East$ rm -r ~/Coordinates-Location/East/EastCoordinate.txt
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location/East$ mv ^C
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location/East$ mv ~/Coordinates-Location/EastCoordinate.txt ~/Coordinates-Location/East.txt
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location/East$ 
anaki@janaki-HP-Laptop-14s-fq1xxx:~$ cd Coordinates-Location
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ cat North.txt East.txt >Location-Coordinate.txt
cat: North.txt: No such file or directory
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ mv NorthCoordinate.txt North.txt
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ cat North.txt East.txt >Location-Coordinate.txt
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ 
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ paste -sd '' North.txt
9°5'38.1"
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ paste -sd '' East.txt
76°29'30.8"
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ sed ':a; N; $!ba; s/\n//g' North.txt
9°5'38.1"
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ sed ':a; N; $!ba; s/\n//g' East.txt
76°29'30.8"
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ Noth.txt | tr '\n' ' '
Noth.txt: command not found
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ tr '\n' ' ' NOrth.txt
tr: extra operand ‘NOrth.txt’
Try 'tr --help' for more information.
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ grep North.txt | tr '\n' ' '
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ awk '{print}' ORS='" '
^C
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ tr '\n' ' ' NOrth.txt
tr: extra operand ‘NOrth.txt’
Try 'tr --help' for more information.
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ tr: extra operand ‘NOrth.txt’

Command 'tr:' not found, did you mean:

  command 'tr' from deb coreutils (8.30-3ubuntu2)
  command 'trn' from deb trn4 (4.0-test77-12)
  command 'trs' from deb konwert (1.8-13build1)

Try: sudo apt install <deb name>

janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ tr '\n' ' ' NOrth.txt
tr: extra operand ‘NOrth.txt’
Try 'tr --help' for more information.
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ tr: extra operand ‘NOrth.txt’

Command 'tr:' not found, did you mean:

  command 'tr' from deb coreutils (8.30-3ubuntu2)
  command 'trs' from deb konwert (1.8-13build1)
  command 'trn' from deb trn4 (4.0-test77-12)

Try: sudo apt install <deb name>

janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ grep North.txt | tr '\n' ' '
  
   
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ tr "\n" " " < North.txt
9°#5'#38.1"#janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ 
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ tr "\n" " " < North.txt> north.txt
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ tr "\n" " " < North.txt> North.txt
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ tr "\n" " " <Eas t.txt> east.txt
bash: Eas: No such file or directory
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ tr "\n" " " <East.txt> east.txt
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ cat north.txt east.txt >Location-Coordinate.txt
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ cat <SOLUTION.md
