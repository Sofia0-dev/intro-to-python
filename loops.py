# for loops
# while
from arrays import people

# for nums in range(0,11):
#     print(nums)

# num = 0
# while num <= 10:
#     print(num)
#     num += 1  # num + 1

scores = [67, 98, 32, 90, 12, 100, 84, 35, 59]
# for s in scores:
#     if s >= 50 and s <= 70 or s > 90:
#         print(s)

people = [
  {
    "name": "Kato Kinney",
    "email": "risus.quis@outlook.ca",
    "country": "Russian Federation",
    "age": 23
  },
  {
    "name": "Desirae Hatfield",
    "email": "erat@icloud.net",
    "country": "Spain",
    "age": 19
  },
  {
    "name": "Abel Odom",
    "email": "eget.nisi@hotmail.ca",
    "country": "Austria",
    "age": 21
  },
  {
    "name": "Chancellor O'connor",
    "email": "nullam.suscipit@hotmail.edu",
    "country": "Sweden",
    "age": 43
  },
  {
    "name": "Upton Harvey",
    "email": "tellus@outlook.org",
    "country": "Italy",
    "age": 50
  },
  {
    "name": "Whitney Leon",
    "email": "ut@aol.ca",
    "country": "Vietnam",
    "age": 64
  },
  {
    "name": "Mason Mays",
    "email": "cursus@yahoo.com",
    "country": "Mexico",
    "age": 69
  },
  {
    "name": "Malachi Bradley",
    "email": "tellus.non@aol.edu",
    "country": "Pakistan",
    "age": 17
  },
  {
    "name": "Aladdin Vincent",
    "email": "egestas.hendrerit@yahoo.couk",
    "country": "Netherlands",
    "age": 35
  },
  {
    "name": "Ira Sears",
    "email": "ante.maecenas@aol.net",
    "country": "Turkey",
    "age": 59
  },
  {
    "name": "Ralph Allen",
    "email": "sit.amet@hotmail.com",
    "country": "Spain",
    "age": 43
  },
  {
    "name": "Keiko Hensley",
    "email": "pretium.et.rutrum@hotmail.com",
    "country": "Sweden",
    "age": 53
  },
  {
    "name": "Lane Garcia",
    "email": "nibh@outlook.net",
    "country": "Turkey",
    "age": 52
  },
  {
    "name": "Akeem Delgado",
    "email": "arcu.iaculis@google.com",
    "country": "Pakistan",
    "age": 49
  },
  {
    "name": "Germane Blackburn",
    "email": "dolor.donec@hotmail.com",
    "country": "Chile",
    "age": 38
  },
  {
    "name": "Grant Mayer",
    "email": "aliquam.gravida.mauris@aol.org",
    "country": "Pakistan",
    "age": 51
  },
  {
    "name": "Lamar Boone",
    "email": "iaculis@aol.couk",
    "country": "Ukraine",
    "age": 69
  },
  {
    "name": "Ezra Cotton",
    "email": "dis.parturient@outlook.ca",
    "country": "Belgium",
    "age": 21
  },
  {
    "name": "Abdul Castro",
    "email": "nonummy.ut@yahoo.ca",
    "country": "Colombia",
    "age": 54
  },
  {
    "name": "Emi Allison",
    "email": "nunc.sed@icloud.org",
    "country": "Netherlands",
    "age": 18
  },
  {
    "name": "TaShya Cooke",
    "email": "fusce.aliquet.magna@google.com",
    "country": "Sweden",
    "age": 35
  },
  {
    "name": "Lee Haney",
    "email": "rhoncus.id@outlook.edu",
    "country": "Austria",
    "age": 58
  },
  {
    "name": "Octavius Lopez",
    "email": "eu@protonmail.edu",
    "country": "Italy",
    "age": 57
  },
  {
    "name": "Sheila Battle",
    "email": "facilisis.suspendisse@google.edu",
    "country": "France",
    "age": 56
  },
  {
    "name": "Shellie Powers",
    "email": "nunc.sit@aol.couk",
    "country": "Vietnam",
    "age": 38
  },
  {
    "name": "Dean Hensley",
    "email": "pede.cum.sociis@google.couk",
    "country": "Pakistan",
    "age": 34
  },
  {
    "name": "Gabriel Cline",
    "email": "nulla@yahoo.net",
    "country": "Chile",
    "age": 48
  },
  {
    "name": "Curran Cooke",
    "email": "nascetur.ridiculus@hotmail.com",
    "country": "Belgium",
    "age": 68
  },
  {
    "name": "Travis Thomas",
    "email": "donec.nibh@aol.ca",
    "country": "Turkey",
    "age": 18
  },
  {
    "name": "Ishmael Morales",
    "email": "sed.nec@hotmail.com",
    "country": "Indonesia",
    "age": 20
  },
  {
    "name": "Ulysses Mcdowell",
    "email": "magna.sed.dui@outlook.couk",
    "country": "Norway",
    "age": 29
  },
  {
    "name": "Hop Clark",
    "email": "mi.enim@google.edu",
    "country": "Turkey",
    "age": 24
  },
  {
    "name": "Wanda Ballard",
    "email": "lorem@aol.couk",
    "country": "South Africa",
    "age": 42
  },
  {
    "name": "Patrick Atkins",
    "email": "lorem.donec.elementum@outlook.couk",
    "country": "Germany",
    "age": 19
  },
  {
    "name": "Rana Good",
    "email": "euismod.et@yahoo.org",
    "country": "Germany",
    "age": 33
  },
  {
    "name": "Melvin Burnett",
    "email": "adipiscing.lacus.ut@aol.net",
    "country": "Brazil",
    "age": 58
  },
  {
    "name": "Trevor Cook",
    "email": "fringilla.mi.lacinia@outlook.com",
    "country": "Germany",
    "age": 47
  },
  {
    "name": "Kerry Mooney",
    "email": "est.mauris@google.com",
    "country": "United States",
    "age": 32
  },
  {
    "name": "Emi Preston",
    "email": "quis.diam@hotmail.com",
    "country": "Peru",
    "age": 60
  },
  {
    "name": "Murphy Good",
    "email": "velit.pellentesque.ultricies@google.org",
    "country": "Poland",
    "age": 60
  },
  {
    "name": "Renee Riggs",
    "email": "mauris.elit.dictum@google.net",
    "country": "Australia",
    "age": 35
  },
  {
    "name": "Ina Norton",
    "email": "eget.metus@outlook.ca",
    "country": "Norway",
    "age": 37
  },
  {
    "name": "Jasmine Fischer",
    "email": "nam.ac.nulla@yahoo.net",
    "country": "France",
    "age": 61
  },
  {
    "name": "Indira Bowers",
    "email": "nunc.ut@icloud.org",
    "country": "Philippines",
    "age": 53
  },
  {
    "name": "Yoko Middleton",
    "email": "curabitur.consequat@yahoo.org",
    "country": "Australia",
    "age": 48
  },
  {
    "name": "Mari Green",
    "email": "sed.dolor@protonmail.couk",
    "country": "Sweden",
    "age": 68
  },
  {
    "name": "Amir Scott",
    "email": "mi@icloud.org",
    "country": "United States",
    "age": 53
  },
  {
    "name": "Travis Mays",
    "email": "nulla.semper@icloud.net",
    "country": "New Zealand",
    "age": 17
  },
  {
    "name": "Wang Peterson",
    "email": "nibh.aliquam@yahoo.net",
    "country": "Singapore",
    "age": 32
  },
  {
    "name": "Lucy Yang",
    "email": "pede.sagittis.augue@yahoo.edu",
    "country": "Ukraine",
    "age": 34
  },
  {
    "name": "Nerea Cain",
    "email": "accumsan.sed@aol.net",
    "country": "United States",
    "age": 48
  },
  {
    "name": "Cassandra Mack",
    "email": "at@google.edu",
    "country": "Germany",
    "age": 68
  },
  {
    "name": "Chadwick Dawson",
    "email": "id.ante.nunc@icloud.com",
    "country": "Norway",
    "age": 51
  },
  {
    "name": "Farrah Lawrence",
    "email": "consequat@hotmail.net",
    "country": "United Kingdom",
    "age": 34
  },
  {
    "name": "Jordan Mcdaniel",
    "email": "mus.aenean@hotmail.ca",
    "country": "Chile",
    "age": 65
  },
  {
    "name": "Fredericka Sweet",
    "email": "ut.tincidunt@outlook.com",
    "country": "South Korea",
    "age": 58
  },
  {
    "name": "Adam Mcdonald",
    "email": "mauris@yahoo.edu",
    "country": "Ukraine",
    "age": 58
  },
  {
    "name": "Jolene Dickson",
    "email": "ac.sem.ut@google.net",
    "country": "Spain",
    "age": 31
  },
  {
    "name": "Kuame Conway",
    "email": "nunc@aol.ca",
    "country": "Ireland",
    "age": 42
  },
  {
    "name": "Gillian Webster",
    "email": "eget@google.edu",
    "country": "Netherlands",
    "age": 62
  },
  {
    "name": "Gabriel Riley",
    "email": "at.nisi@google.couk",
    "country": "France",
    "age": 31
  },
  {
    "name": "Reuben Wilcox",
    "email": "lobortis.nisi@outlook.couk",
    "country": "Costa Rica",
    "age": 57
  },
  {
    "name": "Calista Rich",
    "email": "bibendum.ullamcorper.duis@protonmail.ca",
    "country": "Singapore",
    "age": 42
  },
  {
    "name": "Jonah Petersen",
    "email": "ridiculus.mus.proin@outlook.org",
    "country": "Sweden",
    "age": 32
  },
  {
    "name": "Erich Hutchinson",
    "email": "lectus.convallis@icloud.com",
    "country": "Pakistan",
    "age": 38
  },
  {
    "name": "Benjamin Shepard",
    "email": "magna.malesuada.vel@icloud.ca",
    "country": "Mexico",
    "age": 33
  },
  {
    "name": "Mark Ferguson",
    "email": "volutpat.nulla@hotmail.edu",
    "country": "Nigeria",
    "age": 35
  },
  {
    "name": "Alma Ferguson",
    "email": "lorem@yahoo.net",
    "country": "India",
    "age": 36
  },
  {
    "name": "Madonna Lucas",
    "email": "eget.ipsum@yahoo.couk",
    "country": "Ireland",
    "age": 59
  },
  {
    "name": "Denton Weber",
    "email": "posuere.vulputate.lacus@google.couk",
    "country": "Germany",
    "age": 37
  },
  {
    "name": "Palmer Tran",
    "email": "eu.sem.pellentesque@outlook.org",
    "country": "Singapore",
    "age": 49
  },
  {
    "name": "Anne Blankenship",
    "email": "nibh@google.couk",
    "country": "Austria",
    "age": 34
  },
  {
    "name": "Noelani Emerson",
    "email": "hendrerit@google.ca",
    "country": "Peru",
    "age": 49
  },
  {
    "name": "Yen Valencia",
    "email": "malesuada.fringilla@yahoo.net",
    "country": "Ukraine",
    "age": 33
  },
  {
    "name": "Anthony Puckett",
    "email": "aenean.gravida.nunc@hotmail.ca",
    "country": "Chile",
    "age": 28
  },
  {
    "name": "Dane Henson",
    "email": "non.leo.vivamus@icloud.com",
    "country": "Netherlands",
    "age": 19
  },
  {
    "name": "Destiny Bowen",
    "email": "pellentesque.sed@protonmail.net",
    "country": "Brazil",
    "age": 16
  },
  {
    "name": "Maya Estrada",
    "email": "euismod.mauris.eu@icloud.edu",
    "country": "Pakistan",
    "age": 47
  },
  {
    "name": "Haley Mcknight",
    "email": "lobortis.ultrices.vivamus@outlook.edu",
    "country": "Norway",
    "age": 38
  },
  {
    "name": "Aline House",
    "email": "consequat@outlook.net",
    "country": "Poland",
    "age": 33
  },
  {
    "name": "Farrah French",
    "email": "lacinia.at.iaculis@aol.net",
    "country": "Vietnam",
    "age": 46
  },
  {
    "name": "Reuben Nolan",
    "email": "lorem.sit.amet@outlook.com",
    "country": "Peru",
    "age": 62
  },
  {
    "name": "Lucas Sellers",
    "email": "neque@protonmail.ca",
    "country": "Sweden",
    "age": 36
  },
  {
    "name": "Mallory Harding",
    "email": "leo@yahoo.ca",
    "country": "India",
    "age": 21
  },
  {
    "name": "Ignatius Bright",
    "email": "feugiat@hotmail.ca",
    "country": "Poland",
    "age": 68
  },
  {
    "name": "Kibo Brooks",
    "email": "eleifend@hotmail.net",
    "country": "Colombia",
    "age": 55
  },
  {
    "name": "Lara Diaz",
    "email": "massa.quisque@yahoo.ca",
    "country": "Singapore",
    "age": 19
  },
  {
    "name": "Emmanuel Hodge",
    "email": "sapien.cras.dolor@outlook.ca",
    "country": "Vietnam",
    "age": 64
  },
  {
    "name": "Frances Baker",
    "email": "odio.etiam@protonmail.couk",
    "country": "Australia",
    "age": 54
  },
  {
    "name": "Dai Gilmore",
    "email": "felis@yahoo.com",
    "country": "Brazil",
    "age": 35
  },
  {
    "name": "Xandra Reyes",
    "email": "integer.vitae@protonmail.com",
    "country": "Costa Rica",
    "age": 36
  },
  {
    "name": "Buckminster Lowery",
    "email": "ante@hotmail.edu",
    "country": "Russian Federation",
    "age": 43
  },
  {
    "name": "Brandon Cohen",
    "email": "blandit@hotmail.ca",
    "country": "France",
    "age": 27
  },
  {
    "name": "Carlos Nolan",
    "email": "commodo.hendrerit@icloud.couk",
    "country": "Netherlands",
    "age": 58
  },
  {
    "name": "Kelsey Gibson",
    "email": "at@yahoo.org",
    "country": "Australia",
    "age": 46
  },
  {
    "name": "Ishmael Padilla",
    "email": "pede.et.risus@outlook.org",
    "country": "Sweden",
    "age": 63
  },
  {
    "name": "Mallory Fuentes",
    "email": "a.ultricies@outlook.ca",
    "country": "Spain",
    "age": 33
  },
  {
    "name": "Lyle House",
    "email": "tristique.aliquet.phasellus@aol.com",
    "country": "Russian Federation",
    "age": 53
  },
  {
    "name": "Hoyt Hickman",
    "email": "in.condimentum@outlook.ca",
    "country": "Ukraine",
    "age": 52
  },
  {
    "name": "Wayne Wells",
    "email": "eu.dui@outlook.couk",
    "country": "Peru",
    "age": 56
  }
]
#print details
for person in people:
    name = person["name"]
    age = person["age"]
    country = person["country"]
    if country == "Australia" and age>30:
     print(f"Name is {name}, Age is {age}, Country is {country}")

#TODO  Sort by age
