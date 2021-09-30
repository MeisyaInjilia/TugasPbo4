class Indonesia():

    def capital(self):

        print("DKI Jakarta adalah ibu kota Indonesia.")
 

    def bahasa(self):

        print("Bahasa Indonesia adalah bahasa yang paling banyak digunakan di Indonesia.")
 

    def type(self):

        print("Indonesia adalah negara yang kaya akan keindahan alam.")
 

class USA():

    def capital(self):

        print("Washington, DC adalah ibu kota Amerika Serikat.")
 

    def bahasa(self):

        print("Bahasa Inggris adalah bahasa utama Amerika Serikat.")
 

    def type(self):

        print("Amerika Serikat adalah negara maju.")
 

obj_ind = Indonesia()

obj_usa = USA()

for country in (obj_ind, obj_usa):

    country.capital()

    country.bahasa()

    country.type()