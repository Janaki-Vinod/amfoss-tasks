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











                               COMMANDS FOR PUSHING INTO GIT
                               
                               
                               
                               
                               
                               
                               
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ cd ~/Coordinates-Location
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git config

Command 'git' not found, but can be installed with:

sudo apt install git

janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ sudo apt install git
[sudo] password for janaki: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  git-man liberror-perl
Suggested packages:
  git-daemon-run | git-daemon-sysvinit git-doc git-el git-email git-gui gitk
  gitweb git-cvs git-mediawiki git-svn
The following NEW packages will be installed:
  git git-man liberror-perl
0 upgraded, 3 newly installed, 0 to remove and 117 not upgraded.
Need to get 5,465 kB of archives.
After this operation, 38.4 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://in.archive.ubuntu.com/ubuntu focal/main amd64 liberror-perl all 0.17029-1 [26.5 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu focal-updates/main amd64 git-man all 1:2.25.1-1ubuntu3.2 [884 kB]
Get:3 http://in.archive.ubuntu.com/ubuntu focal-updates/main amd64 git amd64 1:2.25.1-1ubuntu3.2 [4,554 kB]
Fetched 5,465 kB in 3s (1,592 kB/s)
Selecting previously unselected package liberror-perl.
(Reading database ... 146683 files and directories currently installed.)
Preparing to unpack .../liberror-perl_0.17029-1_all.deb ...
Unpacking liberror-perl (0.17029-1) ...
Selecting previously unselected package git-man.
Preparing to unpack .../git-man_1%3a2.25.1-1ubuntu3.2_all.deb ...
Unpacking git-man (1:2.25.1-1ubuntu3.2) ...
Selecting previously unselected package git.
Preparing to unpack .../git_1%3a2.25.1-1ubuntu3.2_amd64.deb ...
Unpacking git (1:2.25.1-1ubuntu3.2) ...
Setting up liberror-perl (0.17029-1) ...
Setting up git-man (1:2.25.1-1ubuntu3.2) ...
Setting up git (1:2.25.1-1ubuntu3.2) ...
Processing triggers for man-db (2.9.1-1) ...
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git config
usage: git config [<options>]

Config file location
    --global              use global config file
    --system              use system config file
    --local               use repository config file
    --worktree            use per-worktree config file
    -f, --file <file>     use given config file
    --blob <blob-id>      read config from given blob object

Action
    --get                 get value: name [value-regex]
    --get-all             get all values: key [value-regex]
    --get-regexp          get values for regexp: name-regex [value-regex]
    --get-urlmatch        get value specific for the URL: section[.var] URL
    --replace-all         replace all matching variables: name value [value_regex]
    --add                 add a new variable: name value
    --unset               remove a variable: name [value-regex]
    --unset-all           remove all matches: name [value-regex]
    --rename-section      rename section: old-name new-name
    --remove-section      remove a section: name
    -l, --list            list all
    -e, --edit            open an editor
    --get-color           find the color configured: slot [default]
    --get-colorbool       find the color setting: slot [stdout-is-tty]

Type
    -t, --type <>         value is given this type
    --bool                value is "true" or "false"
    --int                 value is decimal number
    --bool-or-int         value is --bool or --int
    --path                value is a path (file or directory name)
    --expiry-date         value is an expiry date

Other
    -z, --null            terminate values with NUL byte
    --name-only           show variable names only
    --includes            respect include directives on lookup
    --show-origin         show origin of config (file, standard input, blob, command line)
    --default <value>     with --get, use default value when missing entry

janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git --config
unknown option: --config
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ Git config --global user.name "Janaki-Vinod
> bash: unexpected EOF while looking for matching `"'
bash: syntax error: unexpected end of file
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ Git config --global user.name "Janaki-Vinod"

Command 'Git' not found, did you mean:

  command 'wit' from deb wit (3.01a-2)
  command 'git' from deb git (1:2.25.1-1ubuntu3.2)
  command 'vit' from deb vit (2.0.0-1)

Try: sudo apt install <deb name>

janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git config --global user.name "Janaki-Vinod"
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ it config --global user.email siddam.bharat@simplilearn.net
it: command not found
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ 
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git config --global user.email amenu4cse21428@am.students.amrita.edu
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git config -list
error: did you mean `--list` (with two dashes)?
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git config --list
user.name=Janaki-Vinod
user.email=amenu4cse21428@am.students.amrita.edu
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git init
Initialized empty Git repository in /home/janaki/Coordinates-Location/.git/
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git add -a
error: unknown switch `a'
usage: git add [<options>] [--] <pathspec>...

    -n, --dry-run         dry run
    -v, --verbose         be verbose

    -i, --interactive     interactive picking
    -p, --patch           select hunks interactively
    -e, --edit            edit current diff and apply
    -f, --force           allow adding otherwise ignored files
    -u, --update          update tracked files
    --renormalize         renormalize EOL of tracked files (implies -u)
    -N, --intent-to-add   record only the fact that the path will be added later
    -A, --all             add changes from all tracked and untracked files
    --ignore-removal      ignore paths removed in the working tree (same as --no-all)
    --refresh             don't add, only refresh the index
    --ignore-errors       just skip files which cannot be added because of errors
    --ignore-missing      check if - even missing - files are ignored in dry run
    --chmod (+|-)x        override the executable bit of the listed files
    --pathspec-from-file <file>
                          read pathspec from file
    --pathspec-file-nul   with --pathspec-from-file, pathspec elements are separated with NUL character

janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git add --a
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git commit -m "solution"
[master (root-commit) 8755c9c] solution
 2 files changed, 107 insertions(+)
 create mode 100644 task-02/SOLUTION.md
 create mode 100644 task-02/Screenshot from 2021-11-12 00-16-35.png
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git status
On branch master
nothing to commit, working tree clean
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git loh
git: 'loh' is not a git command. See 'git --help'.

The most similar command is
	log
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git log
commit 8755c9c31136dcb3f7c67edbc4b186a4b0db3e69 (HEAD -> master)
Author: Janaki-Vinod <amenu4cse21428@am.students.amrita.edu>
Date:   Fri Nov 12 01:51:28 2021 +0530

    solution
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git remote add origin https://github.com/Janaki-Vinod/amfoss-tasks.git
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git push -u origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/Janaki-Vinod/amfoss-tasks.git'
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git pull --rebase origin main
warning: no common commits
remote: Enumerating objects: 14, done.
remote: Counting objects: 100% (14/14), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 14 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (14/14), 139.46 KiB | 816.00 KiB/s, done.
From https://github.com/Janaki-Vinod/amfoss-tasks
 * branch            main       -> FETCH_HEAD
 * [new branch]      main       -> origin/main
First, rewinding head to replay your work on top of it...
Applying: solution
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git push -u origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/Janaki-Vinod/amfoss-tasks.git'
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git branch -mv origin master
fatal: A branch named 'master' already exists.
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git branch -mv origin main
error: refname refs/heads/origin not found
fatal: Branch rename failed
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git push origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/Janaki-Vinod/amfoss-tasks.git'
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git remote add origin https://github.com/Janaki-Vinod/amfoss-tasks.git
fatal: remote origin already exists.
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ git push -u origin master
Username for 'https://github.com': Janaki-Vinod
Password for 'https://Janaki-Vinod@github.com': 
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 12 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 1.01 MiB | 24.66 MiB/s, done.
Total 5 (delta 0), reused 0 (delta 0)
To https://github.com/Janaki-Vinod/amfoss-tasks.git
   297ae84..c6eb807  master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
janaki@janaki-HP-Laptop-14s-fq1xxx:~/Coordinates-Location$ 


