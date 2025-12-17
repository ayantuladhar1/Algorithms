```python
# Name: Ayan Tuladhar

import os
import sys
import stat
from stat import *

# The following function returns the full paths of all files containing the specified substring at the command line
# by recursively searching all the files and sub directories starting from the specified directory.
# The following function was compiled from the sources referenced below:
# https://man7.org/linux/man-pages/man1/find.1.html
# https://www.tutorialspoint.com/unix_commands/find.htm
# https://docs.python.org/3/library/stat.html
# https://docs.python.org/3/library/os.html#os.stat


path = "D:\CU_DENVER\CU-DENVER 2020(FALL SEM)"
count = 0
for root, directory, filename in os.walk(path):
    for a in filename:

        # To get a full path (which begins with top) to a file or directory in dirpath.

        func = os.path.join(root, a)
        details = os.stat(func)
        var = os.stat(path).st_mode

        # The following command Get the status of a file or a file descriptor. Perform the equivalent of a stat()
        # system call on the given path. path may be specified as either a string or bytes – directly or indirectly
        # through the PathLike interface – or as an open file descriptor. Return a stat_result object.

        os.stat(path, dir_fd=None, follow_symlinks=True)

        # Return non-zero if the mode is from a character special device file.

        if stat.S_ISDIR(var):

            # Size of the file in bytes, if it is a regular file or a symbolic link. The size of a symbolic link is
            # the length of the pathname it contains, without a terminating null byte.

            count = count + details.st_size

            if stat.S_ISREG(details.st_mode):
                print(a, details.st_size, 'bytes')

                # Size of the file in bytes, if it is a regular file or a symbolic link. The size of a symbolic link is
                # the length of the pathname it contains, without a terminating null byte.

                count = count + details.st_size
            else:
                print(a, '......')

            # Change the mode of path to the numeric mode. mode may take one of the following values
            # (as defined in the stat module) or bitwise ORed combinations of them:

            # os.chmod(path, mode, dir_fd=None, follow_symlinks=True)

            # Returns the current global process times. The return value is an object with five attributes:

            (os.times())

print("")
print("The following displays the total number of files and their total size:")
print("Therefore the total files size is :", count, "bytes")

# Exit the process with status n, without calling cleanup handlers, flushing stdio buffers, etc

exit()

```

    DangFinalData.pdf 5560022 bytes
    Data Design.docx 142758 bytes
    Team members CSCI 2421.docx 13163 bytes
    Tuladhar Ayan HW_2.zip 4073 bytes
    tuladharAyanHW6.zip 3962 bytes
    tuladharAyanHW_5.zip 1934 bytes
    tuladharHW_4.zip 3414 bytes
    Tuladhar_FinalProject.zip 294994 bytes
    Carwash.sln 1478 bytes
    .suo 20480 bytes
    Browse.VC.db 6909952 bytes
    SOURCE.ipch 46596096 bytes
    000.testlog 924 bytes
    testlog.manifest 24 bytes
    arrival_time.txt 502 bytes
    ConsoleApplication1.cpp 0 bytes
    ConsoleApplication1.vcxproj 7346 bytes
    ConsoleApplication1.vcxproj.filters 1222 bytes
    ConsoleApplication1.vcxproj.user 168 bytes
    Header.h 0 bytes
    Header1.h 621 bytes
    Source.cpp 6171 bytes
    ConsoleApplication1.exe.recipe 296 bytes
    ConsoleApplication1.log 277 bytes
    ConsoleApplication1.obj 877 bytes
    CL.command.1.tlog 1794 bytes
    CL.write.1.tlog 2100 bytes
    ConsoleApplication1.lastbuildstate 186 bytes
    link.command.1.tlog 1420 bytes
    link.read.1.tlog 3626 bytes
    link.write.1.tlog 706 bytes
    ConsoleApplication1.exe.recipe 300 bytes
    ConsoleApplication1.log 140 bytes
    Source.obj 634406 bytes
    vc142.idb 158720 bytes
    vc142.pdb 454656 bytes
    CL.command.1.tlog 840 bytes
    CL.read.1.tlog 20728 bytes
    CL.write.1.tlog 756 bytes
    ConsoleApplication1.lastbuildstate 184 bytes
    link.command.1.tlog 1460 bytes
    link.read.1.tlog 3874 bytes
    link.write.1.tlog 738 bytes
    ConsoleApplication1.exe 182272 bytes
    ConsoleApplication1.ilk 959812 bytes
    ConsoleApplication1.pdb 716800 bytes
    function.cpp 1195 bytes
    main.cpp 2791 bytes
    makefile 696 bytes
    readme.txt 1724 bytes
    setInput.txt 71 bytes
    Sets.h 402 bytes
    Oscar nominations.sln 1472 bytes
    -DESKTOP-O0F7OEN.suo 59904 bytes
    .suo 63488 bytes
    Browse.VC-DESKTOP-O0F7OEN.db 7241728 bytes
    Browse.VC.db 17743872 bytes
    DATABSE.ipch 43712512 bytes
    OSCAR NOMINATIONS.ipch 35717120 bytes
    MAIN.ipch 44564480 bytes
    MAIN.ipch 44040192 bytes
    BSTREEPICTURE.ipch 44630016 bytes
    BSTREE.ipch 44498944 bytes
    BSTREE.ipch 45219840 bytes
    DATABSE.ipch 44040192 bytes
    USER.ipch 35717120 bytes
    DATABASE.ipch 44564480 bytes
    DATABASE.ipch 44040192 bytes
    DATABASE.ipch 47579136 bytes
    PICTURES.ipch 35848192 bytes
    BSTREEPICTURES.ipch 38404096 bytes
    ACTOR.ipch 35848192 bytes
    BSTREE.ipch 37486592 bytes
    BSTEEACTORS.ipch 45219840 bytes
    BSTREEACTORS.ipch 38404096 bytes
    Oscar nominations.exe 378368 bytes
    Oscar nominations.ilk 2049892 bytes
    Oscar nominations.pdb 1544192 bytes
    Actor-actresses-DESKTOP-O0F7OEN.h 0 bytes
    Actor-actresses.h 14 bytes
    Actor.h 2995 bytes
    Actornode-DESKTOP-O0F7OEN.h 2571 bytes
    Actornode.h 2550 bytes
    BSTeeActors.cpp 15868 bytes
    BSTREE-DESKTOP-O0F7OEN.cpp 15868 bytes
    BSTREE-DESKTOP-O0F7OEN.h 3076 bytes
    BSTREE.h 3055 bytes
    BSTREEActor-DESKTOP-O0F7OEN.h 3076 bytes
    BSTREEActor.h 3055 bytes
    BSTreeActors.cpp 0 bytes
    BSTREEPicture-DESKTOP-O0F7OEN.cpp 18534 bytes
    BSTREEPicture-DESKTOP-O0F7OEN.h 3330 bytes
    BSTREEPicture.h 3311 bytes
    BSTreePictures.cpp 0 bytes
    Database-DESKTOP-O0F7OEN.h 1930 bytes
    Database.cpp 0 bytes
    Database.h 1909 bytes
    Databse-DESKTOP-O0F7OEN.cpp 66084 bytes
    main-DESKTOP-O0F7OEN.cpp 257 bytes
    main.cpp 238 bytes
    Oscar nominations-DESKTOP-O0F7OEN.vcxproj 7941 bytes
    Oscar nominations.vcxproj 7896 bytes
    Oscar nominations.vcxproj-DESKTOP-O0F7OEN.filters 2504 bytes
    Oscar nominations.vcxproj.filters 2406 bytes
    Oscar nominations.vcxproj.user 168 bytes
    Picturenode-DESKTOP-O0F7OEN.h 3813 bytes
    Picturenode.h 3792 bytes
    Pictures.h 4738 bytes
    BSTREE.obj 616041 bytes
    BSTREEPicture.obj 648583 bytes
    Databse.obj 1017212 bytes
    main.obj 160025 bytes
    Oscar nominations.exe.recipe 304 bytes
    Oscar nominations.log 8296 bytes
    vc142.idb 297984 bytes
    vc142.pdb 651264 bytes
    CL.command.1.tlog 3634 bytes
    CL.read.1.tlog 85984 bytes
    CL.write.1.tlog 4954 bytes
    link.command.1.tlog 2216 bytes
    link.read.1.tlog 4888 bytes
    link.write.1.tlog 1382 bytes
    Oscar nominations.lastbuildstate 196 bytes
    BSTeeActors.obj 823098 bytes
    BSTREE.obj 823073 bytes
    BSTREEPicture.obj 881203 bytes
    Databse.obj 1318872 bytes
    main.obj 186434 bytes
    Oscar nominations.exe.recipe 308 bytes
    Oscar nominations.log 359 bytes
    vc142.idb 306176 bytes
    vc142.pdb 634880 bytes
    CL.command.1.tlog 1754 bytes
    CL.read.1.tlog 43174 bytes
    CL.write.1.tlog 3272 bytes
    link-cvtres.read.1.tlog 2 bytes
    link-cvtres.write.1.tlog 2 bytes
    link-rc.read.1.tlog 2 bytes
    link-rc.write.1.tlog 2 bytes
    link.23516-cvtres.read.1.tlog 2 bytes
    link.23516-cvtres.write.1.tlog 2 bytes
    link.23516-rc.read.1.tlog 2 bytes
    link.23516-rc.write.1.tlog 2 bytes
    link.23516.read.1.tlog 2 bytes
    link.23516.write.1.tlog 2 bytes
    link.command.1.tlog 2304 bytes
    link.read.1.tlog 5184 bytes
    link.write.1.tlog 1438 bytes
    Oscar nominations.lastbuildstate 194 bytes
    unsuccessfulbuild 0 bytes
    Oscar nominations.pdb 67584 bytes
    Postfix Airthmatic Expression.sln 1508 bytes
    .suo 18432 bytes
    Browse.VC.db 16285696 bytes
    Postfix Airthmatic Expression.cpp 3409 bytes
    Postfix Airthmatic Expression.sln 1508 bytes
    Postfix Airthmatic Expression.vcxproj 7235 bytes
    Postfix Airthmatic Expression.vcxproj.filters 1002 bytes
    Postfix Airthmatic Expression.vcxproj.user 168 bytes
    Postfix Airthmatic Expression.Build.CppClean.log 1676 bytes
    Postfix Airthmatic Expression.exe.recipe 328 bytes
    Postfix Airthmatic Expression.log 626 bytes
    Postfix Airthmatic Expression.vcxproj.FileListAbsolute.txt 0 bytes
    CL.command.1.tlog 1092 bytes
    CL.write.1.tlog 1080 bytes
    link.command.1.tlog 1772 bytes
    link.read.1.tlog 4078 bytes
    link.write.1.tlog 1008 bytes
    Postfix Airthmatic Expression.lastbuildstate 208 bytes
    main.cpp 0 bytes
    Postfix Airthmatic Expression.cpp 1012 bytes
    Postfix Airthmatic Expression.vcxproj 7235 bytes
    Postfix Airthmatic Expression.vcxproj.filters 1002 bytes
    Postfix Airthmatic Expression.vcxproj.user 168 bytes
    Source.cpp 1461 bytes
    Postfix Airthmatic Expression.Build.CppClean.log 2036 bytes
    Postfix Airthmatic Expression.exe.recipe 358 bytes
    Postfix Airthmatic Expression.log 456 bytes
    Postfix Airthmatic Expression.vcxproj.FileListAbsolute.txt 0 bytes
    CL.command.1.tlog 1212 bytes
    CL.write.1.tlog 1320 bytes
    link.command.1.tlog 2012 bytes
    link.read.1.tlog 3962 bytes
    link.write.1.tlog 1248 bytes
    Postfix Airthmatic Expression.lastbuildstate 238 bytes
    main.cpp 2294 bytes
    makefile 699 bytes
    readme.txt 1174 bytes
    Project1.sln 1445 bytes
    .suo 33280 bytes
    Browse.VC.db 6111232 bytes
    main.cpp 2650 bytes
    Project1.vcxproj 7421 bytes
    Project1.vcxproj.filters 1419 bytes
    Project1.vcxproj.user 168 bytes
    Rectangle.cpp 1108 bytes
    Rectangle.h 778 bytes
    RectangleAreaComparator.h 1174 bytes
    RectanglePerimeterComparator.h 1279 bytes
    Source.cpp 0 bytes
    Project1.exe.recipe 271 bytes
    Project1.log 716 bytes
    Rectangle.obj 5058 bytes
    CL.command.1.tlog 1546 bytes
    CL.write.1.tlog 1458 bytes
    link.command.1.tlog 1394 bytes
    link.read.1.tlog 4032 bytes
    link.write.1.tlog 642 bytes
    Project1.lastbuildstate 172 bytes
    Sets.sln 1433 bytes
    function.cpp 722 bytes
    main.cpp 2514 bytes
    makefile 696 bytes
    setInput.txt 71 bytes
    Sets.h 400 bytes
    Sets.vcxproj 7364 bytes
    Sets.vcxproj.filters 1308 bytes
    Sets.vcxproj.user 168 bytes
    Sets.Build.CppClean.log 855 bytes
    Sets.exe.recipe 263 bytes
    Sets.log 191 bytes
    Sets.vcxproj.FileListAbsolute.txt 0 bytes
    CL.command.1.tlog 1478 bytes
    CL.write.1.tlog 1384 bytes
    link.command.1.tlog 1310 bytes
    link.read.1.tlog 3732 bytes
    link.write.1.tlog 560 bytes
    Sets.lastbuildstate 168 bytes
    Student.sln 1442 bytes
    .suo 39936 bytes
    Browse.VC-DESKTOP-O0F7OEN.db 6672384 bytes
    MAIN.ipch 39714816 bytes
    STUDENT.ipch 36438016 bytes
    STUDENT.ipch 393216 bytes
    SOURCE.ipch 35717120 bytes
    STUDENT.ipch 36372480 bytes
    main.cpp 668 bytes
    Student.cpp 449 bytes
    Student.h 496 bytes
    Student.vcxproj 7365 bytes
    Student.vcxproj.filters 1306 bytes
    Student.vcxproj.user 168 bytes
    Text.txt 348 bytes
    Torinoscar.sln 1451 bytes
    .suo 73216 bytes
    Browse.VC.db 16404480 bytes
    PICTREE.ipch 36962304 bytes
    MAIN.ipch 36962304 bytes
    FUNCTION.ipch 42598400 bytes
    FUNCTION.ipch 42598400 bytes
    TORINOSCAR.ipch 35717120 bytes
    FUNCTION.ipch 36962304 bytes
    FUNCTION.ipch 35979264 bytes
    AANTREE.ipch 36962304 bytes
    Torinoscar.exe 178688 bytes
    Torinoscar.ilk 975872 bytes
    Torinoscar.pdb 774144 bytes
    aantree.cpp 7666 bytes
    aantree.h 1584 bytes
    function.cpp 19688 bytes
    function.h 1114 bytes
    main.cpp 644 bytes
    pictree.cpp 18937 bytes
    pictree.h 2034 bytes
    Torinoscar.vcxproj 7594 bytes
    Torinoscar.vcxproj.filters 1792 bytes
    Torinoscar.vcxproj.user 168 bytes
    aantree.obj 324104 bytes
    function.obj 385267 bytes
    main.obj 218969 bytes
    pictree.obj 344622 bytes
    Torinoscar.exe.recipe 290 bytes
    Torinoscar.log 5389 bytes
    vc142.idb 322560 bytes
    vc142.pdb 847872 bytes
    CL.command.1.tlog 2 bytes
    link.command.1.tlog 2004 bytes
    link.read.1.tlog 4880 bytes
    link.write.1.tlog 1178 bytes
    Torinoscar.lastbuildstate 189 bytes
    unsuccessfulbuild 0 bytes
    turwindefaultoscar.sln 1475 bytes
    .suo 95232 bytes
    Browse.VC.db 17842176 bytes
    PICTREE.ipch 37027840 bytes
    FUCNTION.ipch 35848192 bytes
    RECTANGLEPERIMETERCOMPARATOR.ipch 393216 bytes
    FUCNTION.ipch 37093376 bytes
    SUBPROGRAM.ipch 39583744 bytes
    PICTURES.ipch 37093376 bytes
    AANTREE.ipch 35848192 bytes
    FUNCTION.ipch 39583744 bytes
    MAIN.ipch 42663936 bytes
    ACTORS.ipch 43122688 bytes
    MAIN.ipch 37093376 bytes
    FUNCTION.ipch 35979264 bytes
    MAIN.ipch 38993920 bytes
    FUNCTION.ipch 42598400 bytes
    MAIN.ipch 37093376 bytes
    AANTREE.ipch 35979264 bytes
    FUCNTION.ipch 37093376 bytes
    FUNCTION.ipch 35979264 bytes
    MAIN.ipch 39583744 bytes
    PICTREE.ipch 37093376 bytes
    AANTREE.ipch 37093376 bytes
    PICTREE.ipch 35979264 bytes
    RECTANGLE.ipch 393216 bytes
    FUNCTION.ipch 35979264 bytes
    PICTREE.ipch 35848192 bytes
    AANTREE.ipch 37027840 bytes
    FUCNTION.ipch 37093376 bytes
    FUNCTION.ipch 35979264 bytes
    FUCNTION.ipch 37093376 bytes
    MAIN.ipch 42663936 bytes
    ACTOR.ipch 43122688 bytes
    PICTREE.ipch 37093376 bytes
    TURWINDEFAULTOSCAR.ipch 35717120 bytes
    ACTOR.ipch 43778048 bytes
    FUCNTION.ipch 37093376 bytes
    turwindefaultoscar.exe 175616 bytes
    turwindefaultoscar.ilk 1115532 bytes
    turwindefaultoscar.pdb 1077248 bytes
    actor-actress-new.csv 109164 bytes
    actor-actress.csv 109203 bytes
    Actors.cpp 12354 bytes
    Actors.h 1964 bytes
    main.cpp 843 bytes
    main.h 0 bytes
    Pictures.cpp 24978 bytes
    pictures.csv 16855 bytes
    Pictures.h 2594 bytes
    Subprogram.cpp 25101 bytes
    Subprogram.h 1452 bytes
    turwindefaultoscar.vcxproj 7624 bytes
    turwindefaultoscar.vcxproj.filters 1867 bytes
    turwindefaultoscar.vcxproj.user 168 bytes
    Actors.obj 247067 bytes
    main.obj 219653 bytes
    Pictures.obj 278747 bytes
    Subprogram.obj 337689 bytes
    turwindefaultoscar.Build.CppClean.log 1702 bytes
    turwindefaultoscar.exe.recipe 337 bytes
    turwindefaultoscar.log 183 bytes
    turwindefaultoscar.vcxproj.FileListAbsolute.txt 0 bytes
    vc142.idb 289792 bytes
    vc142.pdb 528384 bytes
    CL.command.1.tlog 3658 bytes
    CL.read.1.tlog 82362 bytes
    CL.write.1.tlog 6062 bytes
    link.command.1.tlog 2236 bytes
    link.read.1.tlog 4676 bytes
    link.write.1.tlog 1406 bytes
    turwindefaultoscar.lastbuildstate 197 bytes
    exam1.pdf 377859 bytes
    final exam.pdf 772984 bytes
    math quiz2.pdf 363893 bytes
    midterm 2 discrete math.pdf 1036820 bytes
    quiz1 .pdf 171649 bytes
    quiz3.pdf 348781 bytes
    quiz5.pdf 432147 bytes
    Battleship dummy.zip 1030194 bytes
    Battleship.zip 1324847 bytes
    BattleshipAyan.zip 1467878 bytes
    TuladharFinalProject.zip 795842 bytes
    tuladharHW2.zip 2403 bytes
    TuladharHW4.zip 6684 bytes
    Battle.sln 1439 bytes
    -DESKTOP-O0F7OEN-2.suo 26624 bytes
    -DESKTOP-O0F7OEN-3.suo 27136 bytes
    -DESKTOP-O0F7OEN-4.suo 76288 bytes
    -DESKTOP-O0F7OEN-5.suo 26624 bytes
    -DESKTOP-O0F7OEN-6.suo 75776 bytes
    -DESKTOP-O0F7OEN.suo 75264 bytes
    .suo 82944 bytes
    Browse.VC-DESKTOP-O0F7OEN-2.db 6062080 bytes
    Browse.VC-DESKTOP-O0F7OEN-3.db 6418432 bytes
    Browse.VC-DESKTOP-O0F7OEN-4.db 38801408 bytes
    Browse.VC-DESKTOP-O0F7OEN-5.db 6340608 bytes
    Browse.VC-DESKTOP-O0F7OEN-6.db 38801408 bytes
    Browse.VC-DESKTOP-O0F7OEN.db 38801408 bytes
    Browse.VC.db 16510976 bytes
    MAIN.ipch 40960000 bytes
    PLAYER.ipch 35651584 bytes
    SMARTCOMPUTER.ipch 35717120 bytes
    MAIN.ipch 40960000 bytes
    GAME.ipch 40960000 bytes
    PLAYER-DESKTOP-O0F7OEN.ipch 39518208 bytes
    MAIN.ipch 40960000 bytes
    USER1.ipch 35717120 bytes
    MAIN.ipch 35717120 bytes
    WATERVEHICLE.ipch 35717120 bytes
    MAIN.ipch 40763392 bytes
    MAIN.ipch 35717120 bytes
    BATTLE.ipch 35717120 bytes
    GRID1.ipch 35717120 bytes
    GRID10_10.ipch 35717120 bytes
    MAIN.ipch 40960000 bytes
    WATERWAR-DESKTOP-O0F7OEN-2.ipch 35717120 bytes
    BOARD.ipch 35717120 bytes
    USER.ipch 35717120 bytes
    MAIN.ipch 40960000 bytes
    Battle-DESKTOP-O0F7OEN.vcxproj 7510 bytes
    Battle.vcxproj 7677 bytes
    Battle.vcxproj-DESKTOP-O0F7OEN.filters 1611 bytes
    Battle.vcxproj.filters 1970 bytes
    Battle.vcxproj.user 168 bytes
    Board-DESKTOP-O0F7OEN-2.cpp 7112 bytes
    Board-DESKTOP-O0F7OEN.cpp 7112 bytes
    Board-DESKTOP-O0F7OEN.h 7849 bytes
    Board.cpp 6018 bytes
    Board.h 9344 bytes
    filName.txt 77 bytes
    Game.h 14 bytes
    Grid10_10-DESKTOP-O0F7OEN-2.cpp 6789 bytes
    Grid10_10-DESKTOP-O0F7OEN-2.h 744 bytes
    Grid10_10-DESKTOP-O0F7OEN-3.h 7650 bytes
    Grid10_10-DESKTOP-O0F7OEN.cpp 6789 bytes
    Grid10_10-DESKTOP-O0F7OEN.h 744 bytes
    Grid10_10.cpp 5747 bytes
    Grid10_10.h 7521 bytes
    main-DESKTOP-O0F7OEN-2.cpp 7303 bytes
    main-DESKTOP-O0F7OEN-3.cpp 7064 bytes
    main-DESKTOP-O0F7OEN.cpp 7306 bytes
    main.cpp 7246 bytes
    Player-DESKTOP-O0F7OEN-2.cpp 1520 bytes
    Player-DESKTOP-O0F7OEN.cpp 1520 bytes
    Player-DESKTOP-O0F7OEN.h 2448 bytes
    Player.cpp 1841 bytes
    Player.h 2494 bytes
    Smartcomputer-DESKTOP-O0F7OEN-2.cpp 3576 bytes
    Smartcomputer-DESKTOP-O0F7OEN-2.h 726 bytes
    Smartcomputer-DESKTOP-O0F7OEN-3.h 4121 bytes
    Smartcomputer-DESKTOP-O0F7OEN.cpp 3576 bytes
    Smartcomputer-DESKTOP-O0F7OEN.h 726 bytes
    Smartcomputer.cpp 3502 bytes
    Smartcomputer.h 4112 bytes
    tata.csv 77 bytes
    tata1.txt 75 bytes
    tata2.txt 75 bytes
    tata3.txt 75 bytes
    tata4.txt 75 bytes
    Waterwar-DESKTOP-O0F7OEN-2.cpp 1815 bytes
    Waterwar-DESKTOP-O0F7OEN.cpp 1830 bytes
    Waterwar-DESKTOP-O0F7OEN.h 2492 bytes
    Waterwar.cpp 1802 bytes
    Waterwar.h 2189 bytes
    Battle-DESKTOP-O0F7OEN-2.log 535 bytes
    Battle-DESKTOP-O0F7OEN-3.log 108 bytes
    Battle-DESKTOP-O0F7OEN-4.log 665 bytes
    Battle-DESKTOP-O0F7OEN.log 163 bytes
    Battle.Build.CppClean-DESKTOP-O0F7OEN-2.log 1819 bytes
    Battle.Build.CppClean-DESKTOP-O0F7OEN-3.log 1660 bytes
    Battle.Build.CppClean-DESKTOP-O0F7OEN.log 1754 bytes
    Battle.Build.CppClean.log 2897 bytes
    Battle.exe.recipe 295 bytes
    Battle.log 568 bytes
    Battle.vcxproj.FileListAbsolute.txt 0 bytes
    Board-DESKTOP-O0F7OEN-2.obj 423017 bytes
    Board-DESKTOP-O0F7OEN.obj 36474 bytes
    Grid10_10-DESKTOP-O0F7OEN-2.obj 307926 bytes
    Grid10_10-DESKTOP-O0F7OEN.obj 33225 bytes
    main-DESKTOP-O0F7OEN.obj 664735 bytes
    main.obj 672943 bytes
    Player-DESKTOP-O0F7OEN-2.obj 202634 bytes
    Player-DESKTOP-O0F7OEN.obj 33409 bytes
    Smartcomputer-DESKTOP-O0F7OEN-2.obj 211362 bytes
    Smartcomputer-DESKTOP-O0F7OEN.obj 35010 bytes
    vc142-DESKTOP-O0F7OEN-2.idb 281600 bytes
    vc142-DESKTOP-O0F7OEN-2.pdb 626688 bytes
    vc142-DESKTOP-O0F7OEN.idb 281600 bytes
    vc142-DESKTOP-O0F7OEN.pdb 626688 bytes
    vc142.idb 166912 bytes
    vc142.pdb 495616 bytes
    Waterwar-DESKTOP-O0F7OEN-2.obj 145365 bytes
    Waterwar-DESKTOP-O0F7OEN.obj 31796 bytes
    Battle.lastbuildstate 198 bytes
    CL.command.1-DESKTOP-O0F7OEN-2.tlog 5234 bytes
    CL.command.1-DESKTOP-O0F7OEN.tlog 5234 bytes
    CL.command.1.tlog 860 bytes
    CL.read.1-DESKTOP-O0F7OEN-DESKTOP-O0F7OEN.tlog 20932 bytes
    CL.write.1-DESKTOP-O0F7OEN-DESKTOP-O0F7OEN.tlog 716 bytes
    link.command.1-DESKTOP-O0F7OEN.tlog 1404 bytes
    link.command.1.tlog 1404 bytes
    link.read.1-DESKTOP-O0F7OEN-DESKTOP-O0F7OEN.tlog 3614 bytes
    link.write.1-DESKTOP-O0F7OEN-DESKTOP-O0F7OEN.tlog 694 bytes
    Battle-DESKTOP-O0F7OEN-2.exe 199168 bytes
    Battle-DESKTOP-O0F7OEN-2.ilk 908180 bytes
    Battle-DESKTOP-O0F7OEN-2.pdb 757760 bytes
    Battle-DESKTOP-O0F7OEN-3.exe 187392 bytes
    Battle-DESKTOP-O0F7OEN-3.ilk 1108480 bytes
    Battle-DESKTOP-O0F7OEN-3.pdb 872448 bytes
    Battle-DESKTOP-O0F7OEN.exe 200192 bytes
    Battle-DESKTOP-O0F7OEN.ilk 1123056 bytes
    Battle-DESKTOP-O0F7OEN.pdb 880640 bytes
    Battle.exe 201216 bytes
    Battle.ilk 2463168 bytes
    Battle.pdb 1732608 bytes
    Battleship.sln 1451 bytes
    -DESKTOP-O0F7OEN-2.suo 92160 bytes
    -DESKTOP-O0F7OEN.suo 90624 bytes
    .suo 97280 bytes
    Browse.VC-DESKTOP-O0F7OEN-2.db 6434816 bytes
    Browse.VC-DESKTOP-O0F7OEN-3.db 39247872 bytes
    Browse.VC-DESKTOP-O0F7OEN.db 39247872 bytes
    WATERVEHICLE.ipch 35717120 bytes
    BATTLESHIP.ipch 2424832 bytes
    COMPUTER.ipch 35717120 bytes
    PLAYER.ipch 38993920 bytes
    GRID10_10.ipch 39124992 bytes
    PLAYER.ipch 39124992 bytes
    SMARTCOMPUTER.ipch 35717120 bytes
    GRID10_10.ipch 39124992 bytes
    GRID10_10.ipch 39124992 bytes
    GRID10_10.ipch 76021760 bytes
    GRID1.ipch 35717120 bytes
    MAIN.ipch 35717120 bytes
    BATTLESHIP.ipch 39583744 bytes
    GRID10_10.ipch 76021760 bytes
    PLAYER.ipch 39124992 bytes
    MAIN.ipch 35717120 bytes
    GRID10_10.ipch 39124992 bytes
    COMPUTER.ipch 35717120 bytes
    BATTLESHIP.ipch 39583744 bytes
    GRID1.ipch 35717120 bytes
    USER.ipch 35717120 bytes
    MAIN.ipch 35717120 bytes
    USER.ipch 35717120 bytes
    WATERVEHICLE.ipch 35717120 bytes
    GRID10_10.ipch 76021760 bytes
    Battleship.aps 1460 bytes
    Battleship.cpp 3949 bytes
    Battleship.rc 1333 bytes
    Battleship.vcxproj 7728 bytes
    Battleship.vcxproj.filters 2143 bytes
    Battleship.vcxproj.user 168 bytes
    Computer.cpp 2731 bytes
    Computer.h 478 bytes
    filName.txt 75 bytes
    game.h 303 bytes
    Grid.cpp 3557 bytes
    grid.h 877 bytes
    Grid1.cpp 5525 bytes
    Grid1.h 737 bytes
    Header.h 14 bytes
    main.cpp 2258 bytes
    name.txt 77 bytes
    Player.cpp 1432 bytes
    Player.h 725 bytes
    resource.h 404 bytes
    Texture.dds 1920128 bytes
    User.cpp 5920 bytes
    User.h 495 bytes
    utils.h 244 bytes
    WaterVehicle.cpp 1647 bytes
    WaterVehicle.h 745 bytes
    Battleship.Build.CppClean.log 1066 bytes
    Battleship.exe.recipe 303 bytes
    Battleship.log 133 bytes
    Battleship.vcxproj.FileListAbsolute.txt 0 bytes
    Computer.obj 212528 bytes
    Grid1.obj 307509 bytes
    main.obj 205374 bytes
    Player.obj 204129 bytes
    User.obj 407551 bytes
    vc142.idb 281600 bytes
    vc142.pdb 626688 bytes
    WaterVehicle.obj 145186 bytes
    Battleship.lastbuildstate 202 bytes
    CL.command.1-DESKTOP-O0F7OEN.tlog 5402 bytes
    CL.command.1.tlog 3586 bytes
    CL.read.1.tlog 118850 bytes
    CL.write.1-DESKTOP-O0F7OEN.tlog 7646 bytes
    CL.write.1.tlog 3702 bytes
    link.command.1.tlog 2658 bytes
    link.read.1.tlog 5652 bytes
    link.write.1.tlog 1758 bytes
    Battleship.exe 184832 bytes
    Battleship.ilk 1061256 bytes
    Battleship.pdb 856064 bytes
    DummyBattleChegg1.sln 1472 bytes
    -DESKTOP-O0F7OEN.suo 80384 bytes
    .suo 69632 bytes
    Browse.VC.db 38821888 bytes
    CHECK_DIR.ipch 35717120 bytes
    MAIN.ipch 36438016 bytes
    OTHER.ipch 36306944 bytes
    GEN_SHIP.ipch 35913728 bytes
    RUN.ipch 36372480 bytes
    RUN.ipch 36438016 bytes
    BRIEF.ipch 35717120 bytes
    IS_DEAD.ipch 35717120 bytes
    CHECK_DIR.ipch 35717120 bytes
    BOARD.ipch 42598400 bytes
    OTHER.ipch 36438016 bytes
    IS_DEAD.ipch 35717120 bytes
    GEN_SHIP.ipch 35717120 bytes
    DummyBattleChegg1.exe 107520 bytes
    DummyBattleChegg1.ilk 697136 bytes
    DummyBattleChegg1.pdb 708608 bytes
    brief.cpp 908 bytes
    brief.h 104 bytes
    check_dir.cpp 1333 bytes
    check_dir.h 298 bytes
    DummyBattleChegg1.vcxproj 7793 bytes
    DummyBattleChegg1.vcxproj-DESKTOP-O0F7OEN.filters 2254 bytes
    DummyBattleChegg1.vcxproj.filters 2254 bytes
    DummyBattleChegg1.vcxproj.user 168 bytes
    gen_ship.cpp 2224 bytes
    gen_ship.h 182 bytes
    is_dead.cpp 609 bytes
    is_dead.h 129 bytes
    main.cpp 937 bytes
    other.cpp 1808 bytes
    other.h 203 bytes
    run.cpp 2468 bytes
    run.h 165 bytes
    brief.obj 54836 bytes
    check_dir.obj 34815 bytes
    DummyBattleChegg1-DESKTOP-O0F7OEN.log 154 bytes
    DummyBattleChegg1.exe.recipe 317 bytes
    DummyBattleChegg1.log 153 bytes
    DummyBattleChegg1.obj 294733 bytes
    dummybattlechegg1.obj.enc 113776 bytes
    gen_ship.obj 37187 bytes
    is_dead.obj 32767 bytes
    main.obj 55032 bytes
    other.obj 108513 bytes
    run.obj 271511 bytes
    vc142.idb 281600 bytes
    vc142.pdb 593920 bytes
    CL.command.1-DESKTOP-O0F7OEN.tlog 7674 bytes
    CL.command.1.tlog 7674 bytes
    CL.read.1.tlog 134654 bytes
    CL.write.1.tlog 7990 bytes
    DummyBattleChegg1.lastbuildstate 209 bytes
    link.command.1.tlog 3156 bytes
    link.read.1-DESKTOP-O0F7OEN.tlog 6426 bytes
    link.read.1.tlog 6430 bytes
    link.write.1.tlog 2228 bytes
    Homework 4.sln 1451 bytes
    .suo 64512 bytes
    Browse.VC.db 6438912 bytes
    ELF.ipch 35717120 bytes
    HOMEWORK 4.ipch 35717120 bytes
    WATERWAR.ipch 35717120 bytes
    BOARD.ipch 40697856 bytes
    WATERWAR.ipch 35717120 bytes
    MAIN.ipch 35717120 bytes
    WATERWAR.ipch 35717120 bytes
    CYBERDEMON.ipch 35717120 bytes
    SMARTCOMPUTER.ipch 39124992 bytes
    HUMAN.ipch 35717120 bytes
    ELF.ipch 35717120 bytes
    BARLOG.ipch 35717120 bytes
    HUMAN.ipch 35717120 bytes
    MAIN.ipch 35717120 bytes
    BARLOG.ipch 35848192 bytes
    DEMON.ipch 35717120 bytes
    CREATURE.ipch 35848192 bytes
    PLAYER.ipch 39124992 bytes
    CYBERDEMON.ipch 35717120 bytes
    GRID10_10.ipch 39124992 bytes
    Homework 4.exe 82944 bytes
    Homework 4.ilk 1495488 bytes
    Homework 4.pdb 1069056 bytes
    Barlog.cpp 1063 bytes
    Barlog.h 313 bytes
    Creature.cpp 1200 bytes
    Creature.h 522 bytes
    Cyberdemon.cpp 930 bytes
    Cyberdemon.h 338 bytes
    Demon.cpp 794 bytes
    Demon.h 318 bytes
    Elf.cpp 942 bytes
    Elf.h 328 bytes
    Homework 4.vcxproj 7693 bytes
    Homework 4.vcxproj.filters 2114 bytes
    Homework 4.vcxproj.user 168 bytes
    Human.cpp 443 bytes
    Human.h 299 bytes
    main.cpp 1204 bytes
    Barlog.obj 159013 bytes
    Creature.obj 160482 bytes
    Cyberdemon.obj 158272 bytes
    Demon.obj 158370 bytes
    Elf.obj 158402 bytes
    Homework 4.Build.CppClean.log 1910 bytes
    Homework 4.exe.recipe 303 bytes
    Homework 4.log 132 bytes
    Homework 4.vcxproj.FileListAbsolute.txt 0 bytes
    Human.obj 137941 bytes
    main.obj 100564 bytes
    vc142.idb 281600 bytes
    vc142.pdb 585728 bytes
    CL.command.1.tlog 6284 bytes
    CL.read.1.tlog 136314 bytes
    CL.write.1.tlog 9686 bytes
    Homework 4.lastbuildstate 202 bytes
    link.command.1.tlog 2876 bytes
    link.read.1.tlog 5802 bytes
    link.write.1.tlog 1948 bytes
    Homework 3(Battleship).docx 89596 bytes
    UML.jpg 413974 bytes
    Programming_assignment1.sln 1490 bytes
    main.cpp 1992 bytes
    Point.cpp 211 bytes
    Point.h 242 bytes
    Programming_assignment1.vcxproj 7384 bytes
    Programming_assignment1.vcxproj.filters 1368 bytes
    Programming_assignment1.vcxproj.user 168 bytes
    REC.cpp 222 bytes
    Rec.h 320 bytes
    Point.obj 4989 bytes
    Programming_assignment1.exe.recipe 272 bytes
    Programming_assignment1.log 160 bytes
    REC.obj 4209 bytes
    CL.command.1.tlog 2300 bytes
    CL.write.1.tlog 1820 bytes
    link.command.1.tlog 1548 bytes
    link.read.1.tlog 4286 bytes
    link.write.1.tlog 774 bytes
    Programming_assignment1.lastbuildstate 158 bytes
    Programming_assignment2.sln 1490 bytes
    .suo 46080 bytes
    Browse.VC.db 6103040 bytes
    GRIDCLASS.ipch 38928384 bytes
    Programming_assignment2.exe 97792 bytes
    gridclass.cpp 1012 bytes
    Header.h 452 bytes
    Programming_assignment2.cpp 1049 bytes
    Programming_assignment2.vcxproj 7336 bytes
    Programming_assignment2.vcxproj.filters 1214 bytes
    Programming_assignment2.vcxproj.user 168 bytes
    Programming_assignment2.Build.CppClean.log 1811 bytes
    Programming_assignment2.exe.recipe 329 bytes
    Programming_assignment2.log 229 bytes
    Programming_assignment2.vcxproj.FileListAbsolute.txt 0 bytes
    CL.command.1.tlog 2086 bytes
    CL.write.1.tlog 2590 bytes
    link.command.1.tlog 2050 bytes
    link.read.1.tlog 4336 bytes
    link.write.1.tlog 1260 bytes
    Programming_assignment2.lastbuildstate 215 bytes
    
    The following displays the total number of files and their total size:
    Therefore the total files size is : 11945991292 bytes
    


```python

```
