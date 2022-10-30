# Name: Ricky Williams
# Date: 10-29-2022
# Description: Uses "HaveIBeenPwned.com" API to check if passwords have appeared in a data breach.
# Rather than checking the passwords directly through the website, this provides an a more
# secure way of checking passes against data breaches by only providing first 5 characters of HASH
# password to api request call and returning a list of all password HASHES that begin with those 5 
# characters which allows us to locally check the full password HASH key against the returned list 
# (K-Anonymity)

# To run command in terminal: 
    # python checkmypass.py (password)

import requests
import hashlib 
import sys 

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check the API and try again")
    else:
        return res

def get_password_leaks_count(hashes, hash_to_check):
    # ^ Checks API response to get number of times each HASH in the list has appeared in a data breach ^
    hashes = ( line.split(':') for line in hashes.text.splitlines())
        # ^ Creates tuple with HASH pass and leak count ^
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0
    
def pwned_api_check(password):
    # ^ Checks if password exists in API response ^
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() 
        # ^ Creates HASH using SHA-1 Algorithm ^
    first5_char, tail = sha1password[:5], sha1password[5:]
        # ^ Separates first 5 characters that will be passed in API call ^
    response = request_api_data(first5_char)

    return get_password_leaks_count(response, tail)



def main(args):
    # Stores arguments passed in from command line
    # To run command: python checkmypass.py (password) 
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'\n{password} was found {count} times. You should change your password!\n')
        else:
            print(f'\n{password} was NOT found. Carry on!\n')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

