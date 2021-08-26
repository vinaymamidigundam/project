class Facebook_create:
    """
    in this class we have to find the x_path for
    each and very element to create the new facebook account
    as given below
    """
    createnew_xpath = "//a[text()='Create New Account']"
    firstname_xpath = "//input[@name='firstname']"
    surename_xpath = "//input[@name='lastname']"
    mobileno_xpath = "//input[@name='reg_email__']"
    newpassword_xpath = "//input[@data-type='password']"
    day_xpath = "//select[@id='day']"
    mounth_xpath = "//select[@id='month']"
    year_xpath = "//select[@id='year']"
    gender_xpath = "//input[@value='2']"
    sigin_xpath = "//button[@name='websubmit']"
