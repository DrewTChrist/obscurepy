class_re = r'class (.*):'  # regex for getting class names
# regex for getting function names and parameters
func_re = r'^def\s(.+)\((.*)\)'
param_re = r'\((.+)\)'  # regex for getting function parameters
var_re = r'.*(\S+)\s='  # regex for getting variable names from assignment
literal_re = r"'(.+)'"  # regex for getting string literals
# regex for matching class assignments
class_assignment_re = r'=\s(.*)\((.*)\)'
function_call_re = r'(.*)\.(.*)\('  # regex for getting function calls
# regex for getting class methods and parameters
class_method_re = r'\s{1,4}def (.*)\((.*)\):'
# regex for getting class body can be used for class methods and global funcs too
class_body_re = r'SomeRandomClass:\n(.*?)^[d,c]'
