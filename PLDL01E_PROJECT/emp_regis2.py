# emp_regis2.py
from emp_regis1 import DesignGUI
from tkinter import ttk
from tkinter import Tk


class DisplayGUI:
    def __init__(self, window):
        self.window = window
        self.gui = DesignGUI(window)

    def header(self):
        # Header
        self.gui.create_heading(40, 18, "SERI'S EMPLOYEE PERSONAL INFORMATION")

    def gui_firstframe(self):
        # First Frame
        self.gui.personal_frame = self.gui.create_frame(20, 125, 740, 145)


        self.gui.create_label(140, 140, 'First Name')
        self.gui.create_textbox(140, 163, width=26)
        self.gui.create_label(310, 140, 'Middle Name')
        self.gui.create_textbox(310, 163, width=26)
        self.gui.create_label(480, 140, 'Last Name')
        self.gui.create_textbox(480, 163, width=26)
        self.gui.create_label(650, 140, 'Suffix')
        self.gui.create_textbox(650, 163, width=15)

        self.gui.create_label(140, 193, 'Date of Birth')

        day_combo = ttk.Combobox(self.window, width=3, values=[str(i) for i in range(1, 32)])
        day_combo.place(x=140, y=216)

        month_combo = ttk.Combobox(self.window, width=10,
                                   values=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                                           'September', 'October', 'November', 'December'])
        month_combo.place(x=180, y=216)

        year_combo = ttk.Combobox(self.window, width=6, values=[str(i) for i in range(2025, 1899, -1)])
        year_combo.place(x=262, y=216)


        self.gui.create_label(332, 193, 'Gender')
        gender_combo = ttk.Combobox(self.window, width=17, values=['Male', 'Female', 'Other'])
        gender_combo.place(x=332, y=216)

        self.gui.create_label(468, 193, "Nationality")
        nationalities_combo = ttk.Combobox(self.window, width=20,  values=['Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguan', 'Argentine', 'Armenian', 'Australian', 'Austrian','Azerbaijani'])
        nationalities_combo.place(x=468, y=216)

        self.gui.create_label(622, 193, 'Civil Status')
        status_combo = ttk.Combobox(self.window, width=17, values=['Single', 'Married', 'Divorced', 'Widowed'])
        status_combo.place(x=622, y=216)

        self.gui.create_image('C:\\Users\\acer\\Desktop\\useraccount.png', 22, 77, 100, 100)

        self.gui.create_label(68, 184, 'No file chosen', font=('Segoe UI', 7), bg='#f8d8f8')

        self.gui.create_button(19, 183, 'Choose File', width=8, height=0, font=('Segoe UI', 7), fg='black',
                               bg='#ffccff')

    def gui_secondframe(self):
        # Second Frame
        self.gui.employment_frame = self.gui.create_frame(20, 290, 740, 150)

        self.gui.create_label(35, 305, 'Department')
        self.gui.create_textbox(35, 330, width=53)
        self.gui.create_label(368, 305, 'Designation')
        self.gui.create_textbox(368, 330, width=33)
        self.gui.create_label(580, 360, 'Employee Number')
        self.gui.create_textbox(580, 385, width=27)
        self.gui.create_label(35, 360, 'Employee Status')
        self.gui.create_textbox(35, 385, width=61)

        self.gui.create_label(580, 305, 'Qualified Dept. Status')
        qualified_combo = ttk.Combobox(self.window, width=24, values=['Qualified', 'Pending', 'Not Qualified'])
        qualified_combo.place(x=580, y=330)

        self.gui.create_label(415, 360, 'Paydate')

        month_combo_paydate = ttk.Combobox(self.window, width=5, values=[str(i) for i in range(1, 13)])
        month_combo_paydate.place(x=415, y=385)

        day_combo_paydate = ttk.Combobox(self.window, width=4, values=[str(i) for i in range(1, 32)])
        day_combo_paydate.place(x=467, y=385)

        year_combo_paydate = ttk.Combobox(self.window, width=6, values=[str(i) for i in range(2025, 1899, -1)])
        year_combo_paydate.place(x=513, y=385)

    def gui_thirdframe(self):
        self.gui.create_label(25, 450, 'Contact Info', bg='#f0e0f0', font=('Segoe UI', 11, 'bold'))
        self.gui.contact_frame = self.gui.create_frame(20, 475, 740, 150)

        self.gui.create_label(35, 485, 'Contact No.')
        self.gui.create_textbox(35, 515, width=50)
        self.gui.create_label(350, 490, 'Email')
        self.gui.create_textbox(350, 515, width=65)
        self.gui.create_label(350, 545, 'Social Media Account ID/No.')
        self.gui.create_textbox(350, 570, width=65)

        self.gui.create_label(35, 545, 'Other (Social Media)')
        socials_combo = ttk.Combobox(self.window, width=47, values=[
            'Facebook', 'Twitter (X)', 'Instagram', 'LinkedIn', 'Snapchat', 'Pinterest', 'Reddit', 'YouTube', 'TikTok',
            'WhatsApp'
        ])
        socials_combo.place(x=35, y=570)

    def gui_fourthframe(self):
        self.gui.create_label(25, 636, 'Address', bg='#f0e0f0', font=('Segoe UI', 11, 'bold'))
        self.gui.address_frame = self.gui.create_frame(20, 660, 740, 315)

        self.gui.create_label(35, 675, 'Address Line 1')
        self.gui.create_textbox(35, 700, width=117)
        self.gui.create_label(35, 730, 'Address Line 2')
        self.gui.create_textbox(35, 755, width=100)
        self.gui.create_label(35, 785, 'City/Municipality')
        self.gui.create_textbox(35, 810, width=58)
        self.gui.create_label(400, 785, 'State/Province')
        self.gui.create_textbox(400, 810, width=56)
        self.gui.create_label(400, 840, 'Zip Code')
        self.gui.create_textbox(400, 865, width=30)
        self.gui.create_label(35, 895, 'Picture Path')
        self.gui.create_textbox(35, 920, width=117)


        self.gui.create_label(35, 840, "Country")
        countries_combo = ttk.Combobox(self.window, width=55, values=[
            'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia',
            'Australia',
            'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize',
            'Benin',
            'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso',
            'Burundi',
            'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China',
            'Colombia',
            'Comoros', 'Congo', 'Congo (Democratic Republic)', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus',
            'Czech Republic',
            'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador',
            'Equatorial Guinea',
            'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia',
            'Germany',
            'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras',
            'Hungary',
            'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica',
            'Japan',
            'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea (North)', 'Korea (South)', 'Kuwait', 'Kyrgyzstan',
            'Laos', 'Latvia',
            'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar',
            'Malawi', 'Malaysia',
            'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia',
            'Moldova', 'Monaco',
            'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
            'New Zealand',
            'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama',
            'Papua New Guinea',
            'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda',
            'Saint Kitts and Nevis',
            'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe',
            'Saudi Arabia',
            'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands',
            'Somalia',
            'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria',
            'Taiwan',
            'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia',
            'Turkey',
            'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States',
            'Uruguay',
            'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
        ])
        countries_combo.place(x=35, y=865)


if __name__ == "__main__":
    window = Tk()
    display_gui = DisplayGUI(window)

    display_gui.header()
    display_gui.gui_firstframe()
    display_gui.gui_secondframe()
    display_gui.gui_thirdframe()
    display_gui.gui_fourthframe()

    window.mainloop()
