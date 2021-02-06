'''
Given a string path, which is an absolute path (starting with a slash '/') 
to a file or directory in a Unix-style file system, convert it to the
 simplified canonical path.

In a Unix-style file system, a period '.' refers 
to the current directory, a double period '..' refers 
to the directory up a level, and any multiple consecutive slashes 
(i.e. '//') are treated as a single slash '/'. For this problem, 
any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

    The path starts with a single slash '/'.
    Any two directories are separated by a single slash '/'.
    The path does not end with a trailing '/'.
    The path only contains the directories on the path from 
    the root directory to the target file or directory 
    (i.e., no period '.' or double period '..')
    '''


class Path:
    def simplifyPath(self, path: str) -> str:
        strs = path.split('/')
        out = []
        for s in strs:
            if s == '..':
                if out:
                    out.pop()
            elif s.isalpha() or (s and s!='.'):
                out.append(s)
        return '/' + '/'.join(out)   
a="/home/"
b="/../"
c="/home//foo/"
d="/a/./b/../../c/"
print(Path().simplifyPath(a))
print(Path().simplifyPath(b))
print(Path().simplifyPath(c)) 
print(Path().simplifyPath(d))