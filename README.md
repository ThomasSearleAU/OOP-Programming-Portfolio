# OOP-Programming-Portfolio
repository containing work for the Programming Portfolio assignment in object oriented programming


w4-1:
inside the necromancy project when modeling and implementing rituals and inventory (resource manager) i made the assumption that we already know all types of resource; and the inventory manager simply explains how many of the item you have (as well as controling the spending of such items). So, when modelling the rituals and inventory; i handled the checks for if the user had the correct quantity of a resource to perform a ritual within the inventory class. Hence, when asked to add this function to ritual - i performed a method call. 

w4-2:
not sure if this is how it was made to be implemented, but i implemented summoning for necromancer - because i am choosing to assosciate a list of summoned entities to a necromancer directly: as well as this, billy came into class and mentioned that my implementation for inventory was unique so it might be a good idea to discuss that. 

w6-2:
i made several errors and explained my debug process to arie: in this case, i was trying to instantiate an object with the following
" return self.type(self.unit_id_setter, self.type.NAME, str(self.type)) " and didnt realise that, the parameters i was passing were attributes of the object that I HAD YET TO INSTANTIATE!!!!!!!!!! and hence, wasnt working. i solved this by locating the issue, and line-by-line brainstorming about what may be going wrong until i found the issue. i fixed the issue by relocating information