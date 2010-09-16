from plone.app.users.browser.personalpreferences import UserDataPanelAdapter

class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """
    def get_firstname(self):
        return self.context.getProperty('firstname', '')
    def set_firstname(self, value):
        return self.context.setMemberProperties({'firstname': value})
    firstname = property(get_firstname, set_firstname)

    def get_lastname(self):
        return self.context.getProperty('lastname', '')
    def set_lastname(self, value):
        return self.context.setMemberProperties({'lastname': value})
    lastname = property(get_lastname, set_lastname)

    def get_gender(self):
        return self.context.getProperty('gender', '')
    def set_gender(self, value):
        return self.context.setMemberProperties({'gender': value})
    gender = property(get_gender, set_gender)

    def get_mobile(self):
        return self.context.getProperty('mobile', '')
    def set_mobile(self, value):
        return self.context.setMemberProperties({'mobile': value})
    mobile = property(get_mobile, set_mobile)

    def get_officen(self):
        return self.context.getProperty('officen', '')
    def set_officen(self, value):
        return self.context.setMemberProperties({'officen': value})
    officen = property(get_officen, set_officen)

    def get_skype(self):
        return self.context.getProperty('skype', '')
    def set_skype(self, value):
        return self.context.setMemberProperties({'skype': value})
    skype = property(get_skype, set_skype)

    def get_birthdate(self):
        return self.context.getProperty('birthdate', '')
    def set_birthdate(self, value):
        return self.context.setMemberProperties({'birthdate': value})
    birthdate = property(get_birthdate, set_birthdate)

    def get_city(self):
        return self.context.getProperty('city', '')
    def set_city(self, value):
        return self.context.setMemberProperties({'city': value})
    city = property(get_city, set_city)

    def get_country(self):
        return self.context.getProperty('country', '')
    def set_country(self, value):
        return self.context.setMemberProperties({'country': value})
    country = property(get_country, set_country)

    def get_phone(self):
        return self.context.getProperty('phone', '')
    def set_phone(self, value):
        return self.context.setMemberProperties({'phone': value})
    phone = property(get_phone, set_phone)

    def get_newsletter(self):
        return self.context.getProperty('newsletter', '')
    def set_newsletter(self, value):
        return self.context.setMemberProperties({'newsletter': value})
    newsletter = property(get_newsletter, set_newsletter)

    def get_institution(self):
        return self.context.getProperty('institution', '')
    def set_institution(self, value):
        return self.context.setMemberProperties({'institution': value})
    institution = property(get_institution, set_institution)

    def get_instadd(self):
        return self.context.getProperty('instadd', '')
    def set_instadd(self, value):
        return self.context.setMemberProperties({'instadd': value})
    instadd = property(get_instadd, set_instadd)

    def get_position(self):
        return self.context.getProperty('position', '')
    def set_position(self, value):
        return self.context.setMemberProperties({'position': value})
    position = property(get_position, set_position)

    def get_profession(self):
        return self.context.getProperty('profession', '')
    def set_profession(self, value):
        return self.context.setMemberProperties({'profession': value})
    profession = property(get_profession, set_profession)

    def get_accept(self):
        return self.context.getProperty('accept', '')
    def set_accept(self, value):
        return self.context.setMemberProperties({'accept': value})
    accept = property(get_accept, set_accept)


