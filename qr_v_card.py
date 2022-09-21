from segno import helpers
qrcode = helpers.make_vcard(name='Seth;Kunal', displayname='Kunal Seth',email='kseth@udcus.com', phone='9800080902',workphone="UDC Inc",street="Dallas Center",city="Hyderabad",zipcode=500081,country='India')
#qrcode = helpers.make_vcard(name='Doe;John', displayname='John Doe', email=('me@example.org', 'another@example.org'), url=['http://www.example.org', 'https://example.org/~joe'])  
qrcode.save('my-vcard.svg', scale=4)
