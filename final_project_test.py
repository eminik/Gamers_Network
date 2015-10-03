import final_project as fp

# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

net = fp.create_data_structure(example_input)

#print net
print net
print fp.get_connections(net, "Debra")
print fp.get_connections(net, "Mercedes")
print fp.get_games_liked(net, "John")
print fp.add_connection(net, "John", "Freda")
print fp.add_new_user(net, "Debra", []) 
print fp.add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
print fp.get_secondary_connections(net, "Mercedes")
print fp.connections_in_common(net, "Mercedes", "John")
print fp.path_to_friend(net, "John", "Ollie")

print "*******"
print "*******"

network = fp.create_data_structure('')
network = fp.add_new_user(network,'Alice',[])
network = fp.add_new_user(network,'Bob',[])
network = fp.add_new_user(network,'Carol',[])
network = fp.add_connection(network,'Alice','Bob')
network = fp.add_connection(network,'Bob','Carol')
network = fp.add_connection(network,'Carol','Bob')
print network
print fp.path_to_friend(network,'Bob','Alice')


print "*******"
print "*******"

network = fp.create_data_structure('')
network = fp.add_new_user(network,'Alice',[])
network = fp.add_new_user(network,'Bob',[])
network = fp.add_new_user(network,'Carol',[])
network = fp.add_connection(network,'Alice','Bob')
network = fp.add_connection(network,'Bob','Carol')
network = fp.add_connection(network,'Carol','Bob')
print network
fp.path_to_friend(network,'David','Carol')


