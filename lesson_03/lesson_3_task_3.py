from address import Address
from mailing import Mailing

from_addr = Address("423160", "Kazan", "Vagapova", "3", "208")
to_addr = Address("675643", "Moscow", "Sovetskaya", "56", "32")

my_mailing = Mailing(to_addr, from_addr, 1000, "2346-76")

print(my_mailing)