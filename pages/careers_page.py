from selenium.webdriver.common.by import By


class CareersPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    jobs_list = ["Customer Success",
                 "Sales",
                 "Product & Engineering",
                 "Finance & Business Support",
                 "Marketing",
                 "CEO’s Executive Office",
                 "Purchasing & Operations",
                 "People and Culture",
                 "Business Intelligence",
                 "Security Engineering",
                 "Partnership",
                 "Quality Assurance",
                 "Mobile Business Unit",
                 "Partner Support Development",
                 "Product Design"
                 ]
    locations_list = ["New York",
                      "Sao Paulo",
                      "London",
                      "Paris",
                      "Amsterdam",
                      "Barcelona",
                      "Helsinki",
                      "Warsaw",
                      "Kiev",
                      "Moscow",
                      "Sydney",
                      "Dubai",
                      "Tokyo",
                      "Seoul",
                      "Singapore",
                      "Bangkok",
                      "Jakarta",
                      "Taipei",
                      "Manila",
                      "Kuala Lumpur",
                      "Ho Chi Minh City",
                      "Istanbul",
                      "Ankara",
                      "Mexico City",
                      "Lima",
                      "Buenos Aires",
                      "Bogota",
                      "Santiago"]
    careers_jobs = (By.XPATH, "//*[contains(@class, 'job-title')]")
    careers_locations = (By.XPATH, "//*[contains(@class, 'location-info')]")
    careers_life_at_Insider = (By.XPATH, "//*[@data-id='21cea83']")
    company_careers = (By.XPATH, "//*[@class='dropdown-sub' and contains(text(), 'Careers')]")
