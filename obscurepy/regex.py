class_re =              r'class (.*):'              #regex for getting class names
func_re =               r'^def\s(.+)\((.*)\)'       #regex for getting function names and parameters
param_re =              r'\((.+)\)'                 #regex for getting function parameters
var_re =                r'.*(\S+)\s='               #regex for getting variable names from assignment
literal_re =            r"'(.+)'"                   #regex for getting string literals
class_assignment_re =   r'=\s(.*)\((.*)\)'          #regex for matching class assignments
function_call_re =      r'(.*)\.(.*)\('             #regex for getting function calls
class_method_re =       r'\s{1,4}def (.*)\((.*)\):'  #regex for getting class methods and parameters
class_body_re =         r'SomeRandomClass:\n(.*?)^[d,c]' #regex for getting class body can be used for class methods and global funcs too