code review for module 5:

talked about usability of inventory manager: and identified reasons why it works better than a finite list of objects

several points to note are to:
    move the dictionary of all items into the inventory class, as the items an inventory contains is one of the attributes of an inventory, and hence belong to an inventory (perhaps add functionality to constructor to make initially moddable inventories (necromaner class?))

    it wouldnt be worth the effort to have a dynamic inventory, as searching through would take more time than the current build

    it is sensible to have the dictionary i made to contain possible resources; as it only becomes slow with large amounts of resources,
    and given the amount i currently have it isn't a problem

    ideally, the ritual cost would only contain quantities, and would eliminate the need to search for resources with a cost of zero, as it would dramatically reduce time costs.