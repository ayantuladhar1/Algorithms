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
