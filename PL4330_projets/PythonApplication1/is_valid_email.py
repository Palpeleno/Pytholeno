import re


def is_valid_flotingP(str):
	floatingPointPattern = r'^[+-]?(\d+\.\d*)|\.\d+)([eE]\d+)?$'
	return bool(re.match(floatingPointPattern, str))


def is_valid_integerConstant(str):
	integerconstantpattern = r'^[+-]?\d+$'
	return bool(re.match(integerconstantpattern, str))

#returns true if regular expression patter match 
def is_valid_email(email):
	emailpattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Za-z]$'
	if not re.match(emailpattern, email):
		return False
	
	if ".." in email.split("@")[0]:
	    return False
	  
	local_part = email.split("@")[0]
	if local_part.startswith(".") or local_part.endswith:
		return False
	  
	local_part_pattern = r'^[A-Za-z0-9#%!$‘&+*\-/=?^_`{|}~]'
	if not re.match(local_part_pattern):
		return False
	  
	domain_pattern = r'^[A-Za-z0-9-]+(\.[A-Za-z0-9-])*$'
	domain_name = email.split("@")[1]
	if not re.match(domain_pattern, domain_name):
	    return False
	return True
