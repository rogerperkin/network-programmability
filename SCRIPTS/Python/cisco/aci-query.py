import requests, json

apic_url = 'sandboxapicdc.cisco.com'
apic_username = 'admin'
apic_password = 'ciscopsdt'

def apic_login(apic: str, username: str, password: str) -> dict:
    """ APIC login and return session cookie """
    apic_cookie = {}
    credentials = {'aaaUser': {'attributes': {'name': apic_username, 'pwd': apic_password }}}
    json_credentials = json.dumps(credentials)
    base_url = 'https://' + apic + '/api/aaaLogin.json'

    login_response = requests.post(base_url, data=json_credentials)

    login_response_json = json.loads(login_response.text)
    token = login_response_json['imdata'][0]['aaaLogin']['attributes']['token']
    apic_cookie['APIC-Cookie'] = token
    return apic_cookie

def apic_query(apic: str, path: str, cookie: dict) -> dict:
    """ APIC 'GET' query and return response """
    base_url = 'https://' + apic + path

    get_response = requests.get(base_url, cookies=cookie)

    return get_response

def apic_logout(apic: str, cookie:dict) -> dict:
    """ APIC logout and return response """
    base_url = 'https://' + apic + '/api/aaaLogout.json'

    post_response = requests.post(base_url, cookies=cookie)

    return post_response

apic_cookie = apic_login(apic=apic_url, username=apic_username, password=apic_password)
response = apic_query(apic=apic_url, path='/api/class/fabricHealthTotal.json', cookie=apic_cookie)
logout_response = apic_logout(apic=apic_url, cookie=apic_cookie)

response_json = json.loads(response.text)
fab_health_total = response_json['imdata'][0]['fabricHealthTotal']['attributes']['cur']

print(fab_health_total)